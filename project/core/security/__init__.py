import os
import urllib
import base64
import config
import logging
import datetime
import simplejson as json

from tipfy import abort
from tipfy import Tipfy
from tipfy import redirect
from tipfy import redirect_to
from tipfy import cached_property

from openid import fetchers as OpenIDFetchers
from openid.extensions import pape as OpenIDPAPE
from openid.extensions import sreg as OpenIDSREG
from openid.consumer import consumer as OpenIDConsumer

from google.appengine.ext import db
from google.appengine.api import memcache

from wirestone.spi.models.security import User as WirestoneUser
from wirestone.spi.models.security import AuthSession as WirestoneSession

from wirestone.spi.core.security.store import DatastoreStore
from wirestone.spi.core.security.fetcher import UrlfetchFetcher

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
		return OpenIDConsumer.Consumer(self.session, DatastoreStore())


class WirestoneUserRequiredMiddleware(WirestoneSecurityMiddleware):

	def pre_dispatch(self, handler):
		return _ws_enforce_security(handler, 'user', self.authConfig)
	

class WirestoneLoginRequiredMiddleware(WirestoneSecurityMiddleware):

	def pre_dispatch(self, handler):
		return _ws_enforce_security(handler, 'login', self.authConfig)
	

def _ws_enforce_security(handler, level, config):
	
	# Set up logging
	if config['debug'] == True:
		do_log = True
		logging.info('=============== WIRESTONE SECURITY MIDDLEWARE ===============')
		logging.info('--Beginning security enforcement.')
	else:
		do_log = False
	
	# Retrieve session cookie
	session_cookie = handler.get_secure_cookie('wirestone.spi.session')
	
	# If there's no cookie, there's no session. Redirect to login.
	if not session_cookie.get('key') and 'auth_ticket' not in handler.session:
		if do_log: logging.info('--No session ID from cookie or session. Redirecting to login.')
		handler.session['continue'] = '?'.join([handler.request.path, handler.request.query_string])
		return handler.redirect_to('auth/login', continueTo='?'.join([handler.request.path, handler.request.query_string]))
	
	# If there is a cookie, validate session...
	else:
		
		if 'auth_ticket' not in handler.session:
			session_id = session_cookie.get('key')
		else:
			session_id = handler.session['auth_ticket']
				
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
				assert session_record

			except (AssertionError, db.Error):
				# If there's nothing in the datastore, there's no session... redirect to login
				if do_log: logging.info('--Could not find DB session. Redirecting to logon.')
				return handler.redirect_to('auth/login')
		else:
			cache_record = False


		if do_log: logging.info('--Session record valid.')
		
		# Make sure user completed the authentication flow
		if session_record.auth_phase != 2:
			if do_log: logging.info('--Auth phase is less than 2 (received "'+str(session_record.auth_phase)+'"). Redirecting to logon.')
			return handler.redirect_to('auth/login')
			
		if do_log: logging.info('--Auth phase valid.')
		
		# Check session expiration
		if session_record.expires < datetime.datetime.now():

			if do_log: logging.info('--Session is expired. Clearing from cache + DB and redirecting to logon.')

			try:
				session_record.evict_from_cache()
				db.delete(session_record)

			except:
				pass
				
			return handler.redirect_to('auth/login')
			
		else:
			if do_log:
				logging.info('--Session is not expired. Setting handler auth parameters.')
				logging.info('------WS_AUTH_COOKIE: '+str(session_cookie))
				logging.info('------WS_AUTH_SESSION: '+str(session_record))
				logging.info('------WS_AUTH_USER: '+str(session_record.user))
				logging.info('------WS_AUTH_USERNAME: '+str(session_record.username))
			
			## Re-cache record
			if cache_record == True: session_record.add_to_cache()
			
			## Map to handler properties
			handler.ws_auth_cookie = session_cookie
			handler.ws_auth_session = session_record
			handler.ws_auth_user = session_record.user
			handler.ws_auth_username = session_record.username
			
			## Map to environ
			os.environ['WS_AUTH_COOKIE'] = str(session_cookie)
			os.environ['WS_AUTH_SESSION'] = str(session_record.key())
			os.environ['WS_AUTH_USER'] = str(session_record)
			os.environ['WS_AUTH_USERNAME'] = str(session_record.username)
			
			## Add to instance memory
			_auth_obj[os.environ['WS_AUTH_SESSION']] = {'cookie':str(session_cookie), 'session': session_record, 'user': session_record.user, 'username': session_record.username, 'expiration': session_record.expires}
			
			
		# Forward to signup if user is unregistered and user is required
		if level == 'user':
			
			if do_log: logging.info('--Handler requests user-level enforcement.')
			
			if session_record.user == None:
				if do_log: logging.info('--User is unregistered. Redirecting to signup.')
				return handler.redirect_to('auth/signup')
				
				
def get_current_user():
	if 'WS_AUTH_SESSION' in os.environ:
		return _auth_obj[os.environ['WS_AUTH_SESSION']]['session'].user
			
			
def is_sys_admin():
	if 'WS_AUTH_SESSION' in os.environ:
		return _auth_obj[os.environ['WS_AUTH_SESSION']]['session'].user.perm_sys_admin
			
			
def is_sys_admin():
	if 'WS_AUTH_SESSION' in os.environ:
		return _auth_obj[os.environ['WS_AUTH_SESSION']]['session'].user.perm_dev_admin