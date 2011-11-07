import os
import urllib
import base64
import config
import logging
import datetime

try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		try:
			from django.utils import simplejson as json
		except ImportError:
			logging.critical('Valid JSON adapter could not be found.')

import webapp2
from webapp2 import abort
from webapp2 import redirect
from webapp2 import redirect_to
from webapp2 import cached_property

from openid import fetchers as OpenIDFetchers
from openid.extensions import pape as OpenIDPAPE
from openid.extensions import sreg as OpenIDSREG
from openid.consumer import consumer as OpenIDConsumer

from google.appengine.ext import db
from google.appengine.api import memcache

from project.models.security import User as WirestoneUser
from project.models.security import AuthSession as WirestoneSession

from project.core.security.store import DatastoreStore
from project.core.security.fetcher import UrlfetchFetcher

_auth_obj = {}


class WirestoneSecurityMiddleware(object):
	
	@cached_property
	def authConfig(self):
		return config.config.get('wirestone.spi.auth')


class WirestoneOpenIDAuthMixin(WirestoneSecurityMiddleware):

	# Wirestone Auth Properties
	ws_auth_user = None
	ws_auth_cookie = None
	ws_auth_session = False
	ws_auth_username = None
	
	# OpenID Properties
	@cached_property
	def openid_extensions(self):
		return (OpenIDSREG, OpenIDPAPE)

	def __init__(self):
		self.ws_auth_session_args = {}

	def getConsumer(self):
		
		OpenIDFetchers.setDefaultFetcher(UrlfetchFetcher())
		return OpenIDConsumer.Consumer(self.request.environ, DatastoreStore())
		

def _ws_enforce_security(handler, level, config):
	
	# Set up logging
	if config['debug'] == True:
		do_log = True
		logging.info('=============== WIRESTONE SECURITY MIDDLEWARE ===============')
		logging.info('--Beginning security enforcement.')
	else:
		do_log = False
		
	# If there's no cookie, there's no session. Redirect to login.
	if not handler.cookie_session.get('key') and 'auth_ticket' not in handler.cookie_session:
		if do_log: logging.info('--No session ID from cookie or session. Redirecting to login.')
		handler.cookie_session['continue'] = '?'.join([handler.request.path, handler.request.query_string])
		return (False, handler.url_for('auth/login', continueTo='?'.join([handler.request.path, handler.request.query_string])))
	
	# If there is a cookie, validate session...
	else:
		
		session_id = handler.cookie_session['auth_ticket']
		
		# Check memcache for the session record...
		session_record = WirestoneSession.get_from_cache(session_id)

		if do_log: logging.info('--Pulled Session ID from cookie or Tipfy session: '+str(session_id))
		if do_log: logging.info('--Cached session result: '+str(session_record))

		# If there's nothing in memcache, check the datastore...
		if session_record is None:
			try:
				cache_record = True
				session_record = WirestoneSession.get_by_key_name(session_id)

				if do_log: logging.info('--DB session result: '+str(session_record))

			except (AssertionError, db.Error):
				# If there's nothing in the datastore, there's no session... redirect to login
				if do_log: logging.info('--Could not find DB session. Redirecting to logon.')
				return (False, handler.url_for('auth/login'))
		else:
			cache_record = False


		if do_log: logging.info('--Session record valid.')
		
		# Make sure user completed the authentication flow
		if session_record.auth_phase != 2:
			if do_log: logging.info('--Auth phase is less than 2 (received "'+str(session_record.auth_phase)+'"). Redirecting to logon.')
			return (False, handler.url_for('auth/login'))
			
		if do_log: logging.info('--Auth phase valid.')
		
		# Check session expiration
		if session_record.expires < datetime.datetime.now():

			if do_log: logging.info('--Session is expired. Clearing from cache + DB and redirecting to logon.')

			try:
				session_record.evict_from_cache()
				db.delete(session_record)

			except:
				pass
				
			return (False, handler.url_for('auth/login'))
			
		else:
			if do_log:
				logging.info('--Session is not expired. Setting handler auth parameters.')
				logging.info('------WS_AUTH_COOKIE: '+str(handler.cookie_session['auth_ticket']))
				logging.info('------WS_AUTH_SESSION: '+str(session_record))
				logging.info('------WS_AUTH_USER: '+str(session_record.user))
				logging.info('------WS_AUTH_USERNAME: '+str(session_record.username))
			
			## Re-cache record
			if cache_record == True: session_record.add_to_cache()
			
			## Map to handler properties
			handler.ws_auth_cookie = handler.cookie_session['auth_ticket']
			handler.ws_auth_session = session_record
			handler.ws_auth_user = session_record.user
			handler.ws_auth_username = session_record.username

			handler.request.environ['WS_AUTH_COOKIE'] = handler.cookie_session['auth_ticket']
			handler.request.environ['WS_AUTH_SESSION'] = session_record
			handler.request.environ['WS_AUTH_USER'] = session_record.user
			
			if session_record.user is None:
				handler.ws_auth_is_user_admin = False
				handler.ws_auth_is_user_developer = False
				handler.request.environ['WS_AUTH_USERNAME'] = session_record.username
				handler.request.environ['WS_AUTH_IS_ADMIN'] = False
				handler.request.environ['WS_AUTH_IS_DEVELOPER'] = False
				return (False, handler.url_for('auth/signup'))
			else:
				handler.ws_auth_is_user_admin = session_record.user.perm_sys_admin
				handler.ws_auth_is_user_developer = session_record.user.perm_dev_admin			
				handler.request.environ['WS_AUTH_USERNAME'] = session_record.username
				handler.request.environ['WS_AUTH_IS_ADMIN'] = session_record.user.perm_sys_admin
				handler.request.environ['WS_AUTH_IS_DEVELOPER'] = session_record.user.perm_dev_admin
				return (True, (handler.ws_auth_cookie, handler.ws_auth_session, handler.ws_auth_user, handler.ws_auth_username, handler.ws_auth_is_user_admin, handler.ws_auth_is_user_developer))
									
		# Forward to signup if user is unregistered and user is required
		if level == 'user':
			
			if do_log: logging.info('--Handler requests user-level enforcement.')
			
			if session_record.user == None:
				if do_log: logging.info('--User is unregistered. Redirecting to signup.')
				return (False, handler.url_for('auth/signup'))
				
				
def get_current_user():
	request = webapp2.get_request()
	if 'WS_AUTH_SESSION' in request.environ and request.environ('WS_AUTH_SESSION') == handler.ws_auth_session:
		return request.ws_auth_user
			
			
def is_sys_admin():
	request = webapp2.get_request()
	if 'WS_AUTH_SESSION' in request.environ and request.environ.get('WS_AUTH_SESSION') == handler.ws_auth_session:
		return request.ws_auth_is_user_admin
	else:
		return False
				
def is_dev_admin():
	request = webapp2.get_request()	
	if 'WS_AUTH_SESSION' in request.environ and request.environ('WS_AUTH_SESSION') == handler.ws_auth_session:
		return request.ws_auth_is_user_developer