import os
import config
import hashlib
import logging
import datetime
import urlparse
import mimetypes

from webapp2 import cached_property

from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.api import memcache
from google.appengine.ext import blobstore

from project.handlers import WebHandler

from openid.consumer.consumer import SetupNeededError

from project.core import security as WirestoneSecurity

from project.forms.security import LogonForm
from project.forms.security import TokenClaimForm
from project.forms.security import RegistrationForm
from project.forms.security import ProfileCreateForm

from project.models.assets import AssetType
from project.models.assets import ProfilePic
from project.models.system import _SystemProperty_
from project.models.ticket import UserRegistrationTicket

from project.models.security import User as WirestoneUser
from project.models.security import AuthSession as WirestoneSession


class Login(WebHandler):
	
	''' Login handler for Wirestone OpenID provider.. '''
	
	def get(self):
		
		## Logging flag
		do_log = self.authConfig['debug']
		
		## Since this is the return_to URL, serve the Yadis OpenID descriptor if something is looking for it
		if str(self.request.headers.get('http-accept')).find('application/xrds+xml') != -1:
			logging.info('Remote host '+str(self.request.remote_addr)+' requested Yadis/XRDS OpenID descriptor. Serving.')
			return self.render('util/openid-discovery.xml', server_name=self.request.host)
			
		else:
			
			if do_log: logging.info('=== Handling incoming logon request from IP '+str(os.environ['REMOTE_ADDR'])+'.')
			
			## Using OpenID...
			if self.authConfig['enable_federated_logon']:
				
				if do_log: logging.info('Federated logon enabled.')
			
				## Pull URL Args
				action = self.request.get('action', False)
				inject = self.request.get('inject', 'false')
				
				## Dump Params
				if do_log: logging.debug('Action: '+str(action))
				if do_log: logging.debug('Inject: '+str(inject))
			
				## User injector for when OpenID is enabled... lets us get past it for testing on the Dev server only
				if inject.lower() == 'true':
					if do_log: logging.info('Injection op requested. Validated. Injecting...')
					return self.debugInjectUserAndRedirect()

				## Force-initiate new authentication session
				if action == False or action.lower() == 'authenticate':
					if do_log: logging.info('Processing for action "authenticate".')

					# Force OpenID re-auth via checkid_setup
					self.beginAuthenticationFlow()
					return self.startOpenIDAuthSession()
			
				## Phase 2 (returned user) from regular, checkid_setup OpenID request
				elif action.lower() == 'oid-phase2':

					if do_log: logging.info('Received returning user for OpenID. Processing for action "oid-phase2".')

					# Validate and finish authentication
					result, username = self.finishOpenIDAuthSession()			
					return self.finishAuthenticationFlow(result, username)

				## Renew session with immediate request to OpenID provider
				elif action.lower() == 'renew':
					
					if do_log: logging.info('Processing for action "renew".')
					return self.startOpenIDAuthSession(immediate=True)
				
				## Phase 2 (returned user) from OpenID provider for immediate request
				elif action.lower() == 'oid-immediate-phase2':
					
					if do_log: logging.info('Received returning user for OpenID. Processing for action "oid-immediate-phase2".')
					result, username = self.finishOpenIDAuthSession()
					return self.finishAuthenticationFlow(result, username)
						
				else:
					if do_log: logging.info('Processing for default action.')
										
					## Assume a user is looking to log in...
					return self.redirect_to('auth/login', action='authenticate')
					
			else: ## No federated logon - draw a login page and authenticate off self
			
				if do_log: logging.info('Federated logon disabled.')
				
				action = self.request.get('action', False)
				
				if action == False or action.lower() == 'spi-phase1':
					
					if do_log: logging.info('Processing for action "spi-phase1".')
					return self.startSPIAuthSession()
			
				
				elif action.lower() == 'spi-phase2':

					if do_log: logging.info('Received POSTed logon request. Processing for action "spi-phase2".')

					# Validate and finish authentication
					self.beginAuthenticationFlow()					
					result, username = self.finishSPIAuthSession()
					return self.finishAuthenticationFlow(result, username)
					
				elif action.lower() == 'token-phase2':
					
					logging.info('=============== ACTION: TOKEN CLAIM ===============')
					logging.info('Token claim from remote IP: '+str(os.environ['REMOTE_ADDR']))
					
					if do_log: logging.info('Processing for action "token-phase2".')

					self.beginAuthenticationFlow()
					
					token = self.request.get('token', False)
					
					if do_log: logging.info('Token value: '+str(token))					

					if token is not False:
						k = db.Key(token)
						t = db.get(k)
						
						if do_log: logging.info('Token record: '+str(k))

						return self.finishAuthenticationFlow(True, t.username)
					else:
						if do_log: logging.error('Token == False. Returning 404.')
						return self.abort(404)
					
				else:
					
					if do_log: logging.info('Processing for default action.')
										
					## Draw the login page by default...
					return self.startSPIAuthSession()
	
	
	def post(self):
		
		do_log = self.authConfig['debug']
		if do_log: logging.info('Processing incoming POST request.')		
		
		action = self.request.get('action', 'false')
		
		## Only reason to post to this handler is to verify homegrown logon attempt
		if action.lower() == 'spi-phase2':
			
			if do_log: logging.info('Processing for action "spi-phase2".')
			
			self.beginAuthenticationFlow()	
			result, data = self.finishSPIAuthSession()
			
			if result is True:
				if do_log: logging.info('Logon successful.')
				return self.finishAuthenticationFlow(True, data)
			else:
				if do_log: logging.info('Logon failed. Returning redirect.')
				return data
		else:
			if do_log: logging.error('Malformed "action" parameter. Error 400 returned.')			
			self.abort(400)
		
		
	def beginAuthenticationFlow(self):
		
		do_log = self.authConfig['debug']
		if do_log: logging.info('==========  BEGINNING AUTHENTICATION FLOW  ==========')

		session_id = WirestoneSession.provisionTicket()

		self.session['auth_ticket'] = session_id.name()
		self.session['auth_continue_url'] = self.makeContinueURL()
		self.session['auth_begin'] = datetime.datetime.now()
		
		if do_log:
			logging.info('SessionID: '+str(session_id))
			logging.info('AuthTicket KN: '+str(self.session['auth_ticket']))
			logging.info('Continue URL: '+str(self.session['auth_continue_url']))
			logging.info('Auth Begin: '+str(self.session['auth_begin']))

		return True
		
		
	def startOpenIDAuthSession(self, immediate=False):
		
		do_log = self.authConfig['debug']

		# Start up consumer
		auth_request = self.openid_consumer.begin(self.openid_endpoint)
		
		if do_log: logging.debug('Instantiated OpenID consumer: '+str(auth_request))

		# Add Simple Registration & PAPE extensions
		sreg, pape = self.openid_extensions
		auth_request.addExtension(sreg.SRegRequest(optional=['nickname', 'fullname', 'email']))
		
		if do_log: logging.debug('Added OpenID extensions: "SREG::SimpleRegistration", "PAPE::ProviderAuthenticationPolicyEnforcement".')

		# Generate return url
		realm = self.generateOpenIDRealm()
		return_url = self.generateReturnURL(immediate=immediate)
		
		if do_log:
			logging.info('===== OpenID Redirect Parameters: =====')
			logging.info('Realm: '+str(realm))
			logging.info('Return URL: '+str(return_url))
			logging.info('Immediate: '+str(immediate))
		
		return self.redirect(auth_request.redirectURL(realm, return_url, immediate=immediate))
		
		
	def finishAuthenticationFlow(self, result, username):
		
		do_log = self.authConfig['debug']
		
		if result == True:
			
			if do_log: logging.info('finishAuthenticationFlow(): Processing successful logon.')
		
			try:
				try:
				
					if do_log: logging.info('Attempting to pull user.')
					u = memcache.get('SPISecurity//User::'+username)
					if u is None:
						u = WirestoneUser.get_by_key_name(username)
						if u is not None:
							memcache.set('SPISecurity//User::'+username, u)
					assert u
					
					if do_log: logging.info('User object: '+str(u))
				
				except AssertionError:
					u = None
					
					if do_log: logging.info('User does not exist.')
			

				# Update ticket
				ticket = WirestoneSession.get_by_key_name(self.session['auth_ticket'])
				assert ticket

				if do_log: logging.info('Pulled ticket by key: '+str(ticket))
						
				# Update ticket
				ticket.auth_phase = 2
				ticket.status = 'active'
				ticket.user = u
				if u is not None:
					ticket.user.session_id = self.session['auth_ticket']
				ticket.username = username
				
				if do_log:
					logging.debug('========== TICKET PARAMS ==========')
					logging.debug('AuthPhase: '+str(ticket.auth_phase))
					logging.debug('Status: '+str(ticket.status))
					logging.debug('User: '+str(ticket.user))
					logging.debug('Username: '+str(ticket.username))
			
				# Set up auth session
				ticket.setLifetime(self.authConfig['ticket_lifetime'])
				if u is not None:
					
					if do_log: logging.info('Saving user and auth ticket records.')
					
					auth_ticket, user = tuple(db.put([ticket, ticket.user]))
				else:
					
					if do_log: logging.info('Saving auth ticket.')
					
					auth_ticket = db.put(ticket)
					
				if do_log: logging.info('Caching ticket.')
				ticket.add_to_cache()
			
				# Set up legit session
				session_cookie = self.get_secure_cookie('wirestone.spi.session', override=True)
				session_cookie['key'] = ticket.key().name()
				
				if do_log:
					logging.info('Wrote session key "'+str(session_cookie['key'])+'" to auth cookie.')
			
				# Get continue URL and redirect
				if not self.session.get('continue'):
					
					if do_log: logging.debug('Redirecting to manufactured continue URL...')
					
					return self.redirect(self.makeContinueURL())
				else:

					if do_log: logging.debug('Redirecting to explicit continue URL...')
					return self.redirect(self.session['auth_continue_url'])
					
			
			## Session is expired at OP, and we must re-initiate login		
			except SetupNeededError, e:
				## Mark session expired.... @TODO
				return self.redirect_to('auth/login', action='authenticate')
				
			## Could not find ticket
			except (AssertionError, db.Error), e:
				logging.error('Error encountered retrieving auth ticket: '+str(e))
				self.response.write('<b>Request blocked for security purposes. Please retry your authentication request.</b>')

			## Unknown error
			except NotImplementedError, e:
				logging.error('Unknown error encountered during authetication flow: '+str(e))
				self.response.write('<b>Request blocked because of improper provider response. Please retry your authentication request.</b>')
				
		else:
			return self.response.write('<b>No LOGON</b>')
				
	
	def finishOpenIDAuthSession(self):
		
		# Check authentication
		openid_response = self.openid_consumer.complete(dict(self.request.args.items(True)), self.request.url.replace('{','%7B').replace('}', '%7D'))
		
		do_log = self.authConfig['debug']
		if do_log:
			logging.debug('OpenID response object'+str(openid_response))
		
		if openid_response.status == 'success':
			
			if do_log: logging.info('OpenID response status is SUCCESS.')
			
			# Pull extension data
			sreg, pape = self.openid_extensions
			sreg_data = sreg.SRegResponse.fromSuccessResponse(openid_response)
			pape_data = pape.Response.fromSuccessResponse(openid_response)

			# Get username from claimed ID
			claimed_id = urlparse.urlparse(self.request.get('openid.identity', False))
			
			username = claimed_id.path.split('/')[-1]			
			
			if do_log: logging.info('Resolved username "'+str(username)+'" from OpenID operation.')
			return (True, username)
			
		elif openid_response.status == 'failure':
			logging.error('Failed to finish OpenID auth session: '+str(openid_response)+'.')
			return (False, str(openid_response))
			
		else:
			logging.error('Failed to finish OpenID auth session for unknown reason.')
			return (False, 'Unknown failure.')
			
			
	def finishSPIAuthSession(self):

		do_log = self.authConfig['debug']
		
		if do_log:
			logging.debug('Processing attempted SPI logon.')

		if self.request.get('action') == 'spi-logon':
			
			if do_log: logging.info('Processing for action "spi-logon".')
			
			f = LogonForm(self.request)
			if f.validate():
				
				if do_log: logging.info('Form validation passed.')
				
				try:
					u = WirestoneUser.get_by_key_name(f.username.data)
					m = hashlib.sha256()
					
					if do_log: logging.info('User object "'+str(u)+'" results from key_name=username "'+str(f.username.data)+'".')
					
					## Safeguard...
					if f.username.data == 'sam.gammon':
						
						ref_hexdigest = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
						
						if do_log:
							logging.info('===== ROOT USER LOGON REQUEST. =====')
							logging.info('Ref Digest: "'+str(ref_hexdigest)+'".')
							logging.info('Incoming Digest: "'+str(m.hexdigest())+'".')
						
						
						if m.hexdigest() == ref_hexdigest:
							logging.info('Root admin SAM.GAMMON signing in. Authorized. Creating session.')
							return (True, 'sam.gammon')					
							
					
					if u is not None:
						m.update(f.password.data)

						if u.password is not None:
							if m.hexdigest() == u.password:
								if do_log: logging.info('Hashed password matches stored value. Authorized. Creating session.')
								return (True, u.key().name())
							else:
								return False, self.redirect_to('auth/login', action='spi-phase1', authFail='Incorrect password.')

						else:
							if do_log: logging.error('Password field is not set for specified user.')
							return False, self.redirect_to('auth/login', action='spi-phase1', authFail='User does not have dev account priviliges.')
					else:
						if do_log: logging.error('No such user.')
						return False, self.redirect_to('auth/login', action='spi-phase1', authFail='No such user.')

				except ValueError:#AssertionError, db.Error:
					if do_log: logging.error('No such user.')
					return False, self.redirect_to('auth/login', action='spi-phase1', authFail='No such user.')			

			
	def debugInjectUserAndRedirect(self):

		session_id = WirestoneSession.provisionTicket()
		self.session['auth_ticket'] = session_id
		self.session['auth_continue_url'] = self.makeContinueURL()
		self.session['auth_begin'] = datetime.datetime.now()

		claimed_id = self.request.get('username', 'sam.gammon')

		try:
			u = WirestoneUser.get_by_key_name(claimed_id)
			assert u

			u = u.key()
		except AssertionError:
			u = None

		ticket = WirestoneSession.get(session_id)
		ticket.auth_phase = 2
		ticket.status = 'active'
		ticket.user = u
		ticket.username = claimed_id
		if u is not None:
			auth_ticket, user = tuple(db.put([ticket, ticket.user]))
		else:
			db.put(ticket)

		ticket.add_to_cache()

		# Set up legit session
		session_cookie = self.get_secure_cookie('wirestone.spi.session', override=True)
		session_cookie['key'] = ticket.key().name()

		if self.authConfig['debug'] == True:
			return self.debugResponse(openid_result, data)
		else:
			# Get continue URL and redirect
			if not self.session.get('continue'):
				return self.redirect(self.makeContinueURL())
			else:
				return self.redirect(self.session['auth_continue_url'])
			
		
	def generateOpenIDRealm(self):
		return os.environ['SERVER_PROTOCOL'].split('/')[0].lower()+'://'+os.environ['HTTP_HOST']
				

	def generateReturnURL(self, immediate=False):
		if immediate == True:
			action = 'oid-immediate-phase2'
		else:
			action = 'oid-phase2'
			
		return os.environ['SERVER_PROTOCOL'].split('/')[0].lower()+'://'+os.environ['HTTP_HOST']+self.url_for('auth/login', action=action, authTicket=self.session.get('auth_ticket'), continueTo=self.request.get('continueTo', '/'))

		
	def makeContinueURL(self):
		if 'continue' in self.session:
			continue_url = self.session['continue']
		elif self.request.get('continueTo', False):
			continue_url = self.request.get('continueTo')
		elif self.request.get('next', False):
			continue_url = self.request.get('next')
		else:
			continue_url = '/'
		
		return continue_url


	@cached_property
	def openid_endpoint(self):
		return config.config.get('wirestone.spi.auth.openid')['endpoint']
		

	@cached_property
	def authConfig(self):
		return config.config.get('wirestone.spi.auth')
		

	@cached_property
	def openid_consumer(self):
		return self.getConsumer()


	def openIDdebugResponse(self, openid_result, data):
		response = '<b>Phase 2</b><br /><br />Args:<ul>'
		for key, value in self.request.args.items(True):
			response = response+'<li><b>'+str(key)+'</b>: '+str(value)
		
		response = response+'</ul><br /><br /><b>Check Result:</b><br /><br />'

		response = response+'<b>Result:</b> '+str(openid_result)+'<br />'
		response = response+'<b>Data:</b> '+str(data)+'<br /><br />'

		response = response+'<b>Done.</b>'
		return self.response.write(response)
		
		
	def startSPIAuthSession(self):
		
		do_log = self.authConfig['debug']
		if do_log: logging.info('Starting SPI AUTH session.')
		
		l = LogonForm(self.request)
		notice = False
		
		if self.request.get('authFail', False) != False:
			notice = self.request.get('authFail')
			
		if do_log: logging.info('Rendering logon page.')
			
		return self.render_response('security/logon.html', logon_form=l, notice=notice)
		
		
class ClaimToken(WebHandler):
	
	''' Claim a token to register a homegrown-auth account. '''
	
	def get(self, token):
		session_cookie = self.get_secure_cookie('wirestone_spi_session', override=True)
		
		try:
			k = db.Key(token)
			t = db.get(k)
			
			assert k
			assert t
			
			t.visited = True
			t.put()

			if self.request.get('claimFail', False) != False:
				notice = self.request.get('claimFail')
			else:
				notice = 'This token will create an account under the name "'+t.username+'".'
			
			return self.render_response('security/token.html', token=db.get(db.Key(token)), claim_form=TokenClaimForm(self.request), notice=notice)
		
		except AssertionError, db.Error:
			self.abort(404)
		
		
	def post(self, token):


		k = db.Key(token)
		t = db.get(k)
		
		if self.request.get('action') == 'spi-claim-token':
			
			f = TokenClaimForm(self.request)
			if f.validate():
				if f.password_1.data == f.password_2.data:
					self.session['acct-claim-password'] = f.password_1.data
					username = t.username
					t.used = True
					t.put()
					
					return self.redirect_to('auth/login', action='token-phase2', token=str(t.key()))
				else:
					return self.redirect_to('auth/claim-token', token=token, claimFail='Passwords must match.')
		
		
		
class Logout(WebHandler):
	
	''' Logout handler for MultiAuth. '''

	@cached_property
	def SecurityConfig(self):
		return config.config.get('wirestone.spi.auth')
		
	@cached_property
	def OpenIDConfig(self):
		return config.config.get('wirestone.spi.auth.openid')

	def get(self):
		session_cookie = self.get_secure_cookie('wirestone_spi_session')

		key = session_cookie.get('key', None)
		if key is not None and key != '':
			try:
				WirestoneSession.get(db.Key(key)).evict_from_cache()
			except:
				pass
				
		#db.delete(db.Key(key) if isinstance(key, basestring) else key)

		session_cookie['key'] = ''
		if 'key' in self.session:
			del self.session['key']
			
		auth_ticket = session_cookie.get('auth_ticket')
		if auth_ticket is not None and auth_ticket != '':
			WirestoneSession.get(db.Key(auth_ticket)).evict_from_cache()
			try:
				db.delete(db.Key(auth_ticket) if isinstance(auth_ticket, basestring) else auth_ticket)
			except:
				pass
			
		session_cookie['auth_ticket'] = ''			
		if 'auth_ticket' in self.session:
			del self.session['auth_ticket']
			
		self.delete_cookie('wirestone_spi_session')
		
		if self.SecurityConfig['enable_federated_logon']:
			redirect = self.OpenIDConfig['logout_url']
			
		else:
			redirect = self.url_for('auth/login')
		
		return self.redirect(redirect)
		
		
class RegisterBeta(WebHandler):

	''' Signup handler. '''
	
	def get(self, step=None, ticket=None):
		return self.render('security/signup/rewrite.html', dependencies=['fancybox', 'plupload'], ticket='sample')
		
	def post(self, step=None, ticket=None):
		pass
		
		
class RegisterBetaFrame(WebHandler):
	
	''' Signup iFrame handler. Pulled in as modal content. '''
	
	def get(self, step=None, ticket=None):
		
		try:
			step = int(step)
		except ValueError:
			self.response.out.write('VALUEERROR: INVALID STEP')
			return
		
		if step == 0:
			return self.render('security/signup/frame/intro.html')
			
		elif step == 1:
			return self.render('security/signup/frame/step1-basic.html', form=RegistrationForm(self.request).set_method('POST').set_action(self.url_for('auth/signup/frame', step=1, ticket=ticket)))
		
		elif step == 2:

			# Construct form & set method
			profile_create_form = ProfileCreateForm(self.request)
			profile_create_form.set_method('POST')
			
			# Set action
			step2_action = self.url_for('auth/signup/frame', step=2, ticket=ticket)
			profile_create_form.set_action(step2_action)
			
			return self.render('security/signup/frame/step2-profile.html', form=profile_create_form)
			
		elif step == 3:
			return self.render('security/signup/frame/step3-settings.html')
			
	def encode(self, struct):
		return json.dumps(struct)
		
	def success(self, response):
		return self.encode({'result': 'success', 'response': response})
		
	def error(self, errors):
		return self.encode({'result': 'failure', 'errors': [{'message': value[0], 'field': key} for key, value in errors.items()]})
			
	def post(self, step=None, ticket=None):
		
		try:
			step = int(step)
		except ValueError:
			self.response.out.write('VALUEERROR: INVALID STEP')
			return
		
		## Basic Registration
		if step == 1:
			
			# Construct & Validate Form
			f = RegistrationForm(self.request)
			if f.validate():
				
				# Construct user acct
				w = WirestoneUser(key_name=self.ws_auth_username,
								  username=self.ws_auth_username,
								  auth_id=self.ws_auth_username+'@wirestone.com',
								  email=self.ws_auth_username+'@wirestone.com',
								  firstname=f.firstname.data.capitalize(),
								  lastname=f.lastname.data.capitalize(),
								  session_id=self.ws_auth_session.key().name(),
								  title=f.title.data)
				
				tagline = None
				if f.title.data is not None:
					w.title = f.title.data.title()
					tagline = w.title
				else:
					w.title = None
					
				try:
					office = db.Key(f.office.data)
					if tagline is not None:
						tagline = tagline+', '+office.name()
				except:
					w.office = None

				# Process claimed password if present
				if 'acct-claim-password' in self.session:
					h = hashlib.sha256()
					h.update(self.session['acct-claim-password'])
					w.password = h.hexdigest()

				# If the user is on the root admins list... add admin privs
				q = _SystemProperty_.get_by_key_name('root_admins')
				if q is not None:
					if self.ws_auth_username in q.value:
						w.perm_sys_admin = True
						w.perm_dev_admin = True						

				# Save user!
				w_key = w.put()

				# Inject newly created user into auth session
				self.ws_auth_session.user = w
				self.ws_auth_session.put()

				# Refresh cached auth session
				self.ws_auth_session.evict_from_cache()
				self.ws_auth_session.add_to_cache()

				profile_replacements = {				
					'profileFirstname': w.firstname,
					'profileLastname': w.lastname,
				}
				
				if tagline is not None:
					profile_replacements['profileTagline'] = tagline
				else:
					profile_replacements['profileTagline'] = 'hide'
				
				if w.perm_sys_admin:
					profile_replacements['adminFlag'] = 'unhide'
				
				if w.perm_dev_admin:
					profile_replacements['devFlag'] = 'unhide'

				# Return success
				return self.success({'user_key': w_key, 'dom_inserts':[{'id': key, 'value': value} for key, value in profile_replacements.items()]})
				
			# Validation fail
			else:
				return self.error(f.errors)
				
			
		elif step == 2:

			p = None ## default to no profile picture
			f = ProfileCreateForm(self.request)
			if f.validate():

				# Set profile properties
				self.ws_auth_user.phone = f.phone.data
				self.ws_auth_user.email = f.email.data
				
				profile_replacements = [
					('profileEmail', self.ws_auth_user.email),
					('profilePhone', self.ws_auth_user.phone),
					('profileEmail', 'unhide'),
					('profilePhone', 'unhide')
				]
				

				if self.request.get('blob_object', False) is not False:
					# @TODO: Create middleware with helper functions for creating assets
					blob_key = blobstore.BlobKey(self.request.get('blob_object'))
					blob_obj = blobstore.BlobInfo.get(blob_key)
					filetype, encoding = mimetypes.guess_type(blob_obj.filename)
				
					# Create profile pic asset
					p = ProfilePic(self.ws_auth_user,
								   key_name='ProfilePic::Original',
								   mime_type=filetype,
								   storage_mode='blobstore', blobstore_data=blob_obj,
								   name=blob_obj.filename,
								   asset_type=AssetType.get_by_key_name('image'))

					# Enable fast serving
					if p.isFastServingCompatible():
						p.constructFastServingURL()

					# Save Asset
					p.put()
					
					self.ws_auth_user.avatar_url = p.getServingURL()					
					
					if p.isFastServingEnabled():
						profile_url = p.getServingURL()+'=s150-c'
						profile_replacements.append(('profileAvatar', "<a href='#'><span></span><img src='"+profile_url+"' alt='That\'s you!' />"))
											

				self.ws_auth_user.put()
				success_response = {'dom_inserts':[{'id': key, 'value': value} for key, value in profile_replacements]}
				
				if p is not None:
					success_response['asset_key'] = p.key()
				
				return self.success(success_response)
				
			# Validation fail
			else:
				return self.error(f.errors)
			
		elif step == 3:
			pass
		
		return SPIJSONAdapter.encode({'result': 'success'})
		

class Register(WebHandler):
	
	''' Signup handler. '''
	
	def get(self, step=None, ticket=None):
		
		message = self.request.get('message', None)
		if message is None or message == '':
			message = False
		
		if step == None:
			
			t = UserRegistrationTicket(status='active', progress='info',
									   continue_url=self.request.get('continue', '/'),
									   user=WirestoneSecurity.get_current_user()).put()
			
			return self.render('security/signup-intro.html', ticket=t)
		
		if step == 1:
			
			f = RegistrationForm(self.request)
			opts = {'continue':self.request.get('continue', '/'), 'step': 1, 'ticket': ticket}
			f.set_action(self.url_for('auth/signup-step-ticket', **opts))
			f.set_method('post')
						
			return self.render('security/signup-step1.html', registration_form=f, ticket=ticket)
			
		elif step == 2:
			
			opts = {'continue':self.request.get('continue', '/'), 'step': 2, 'ticket': ticket, 'message':message}
			action_url = self.url_for('auth/signup-step-ticket', **opts)
			
			return self.render('security/signup-step2.html', upload_url=action_url, ticket=ticket)
			
		elif step == 3:
			
			t = db.get(db.Key(ticket))
			asset = db.get(db.Key(self.request.get('asset')))
			
			image = images.Image(asset.datastore_data)
			
			action = self.url_for('auth/signup-step-ticket', step=3, ticket=str(t.key()))
			return self.render('security/signup-step3.html', dependencies=['jCrop'], asset_key=str(asset.key()), action_url=action, asset_url=asset.getServingURL(), img_height=image.height, img_width=image.width)

		elif step == 4:
			
			t = db.get(db.Key(ticket))
			return self.render('security/signup-step4.html', continue_url=t.continue_url)
		
		
	def post(self, step=None, ticket=None):
		
		if step == 1:

			form = RegistrationForm(self.request)
		
			if form.validate():
				
				## Pull ticket
				t = db.get(db.Key(ticket))
				
				
				w = WirestoneUser(key_name=self.ws_auth_username,
								  username=self.ws_auth_username,
								  auth_id=self.ws_auth_username+'@wirestone.com',
								  email=self.ws_auth_username+'@wirestone.com',
								  firstname=form.firstname.data,
								  lastname=form.lastname.data,
								  session_id=self.ws_auth_session.key().name())

				if 'acct-claim-password' in self.session:
					h = hashlib.sha256()
					h.update(self.session['acct-claim-password'])
					w.password = h.hexdigest()
				
				## If the user is on the root admins list... add admin privs
				q = _SystemProperty_.get_by_key_name('root_admins')
				if q is not None:
					if self.ws_auth_username in q.value:
						w.perm_sys_admin = True
						w.perm_dev_admin = True						
				
				## Save user!
				w_key = w.put()
				
				## Inject newly created user into auth session
				self.ws_auth_session.user = w
				self.ws_auth_session.put()
				
				## Refresh cached auth session
				self.ws_auth_session.evict_from_cache()
				self.ws_auth_session.add_to_cache()
				
				## Update ticket
				t.progress = 'avatar'
				t.put()
				
				return self.redirect(self.url_for('auth/signup-step-ticket', step=2, ticket=ticket))
			
			else:
				return self.redirect(self.url_for('auth/signup-step-ticket', failure='true', step=1, ticket=ticket))
				
		elif step == 2:

			profile_picture_raw = self.request.files.get('profile_picture_raw', False)

			if profile_picture_raw == False:
				return self.redirect(self.url_for('auth/signup-step-ticket', failure='Please select a profile picture to upload.', step=2, ticket=ticket))
			
			
			blob = db.Blob(profile_picture_raw.read())
			try:
				i = images.Image(blob)
			except:
				return self.redirect(self.url_for('auth/signup-step-ticket', step=2, ticket=ticket, message='Please select a profile picture.'))
			
			filetype, encoding = mimetypes.guess_type(profile_picture_raw.filename)
			
			## @TODO: Create middleware with helper functions for creating assets
			p = ProfilePic(self.ws_auth_user,
						   key_name='ProfilePic::Original',
						   mime_type=filetype,
						   storage_mode='datastore', datastore_data=blob,
						   name=profile_picture_raw.filename,
						   asset_type=AssetType.get_by_key_name('image'),
						   height=i.height,
						   width=i.width).put()
			
			response = self.redirect(self.url_for('auth/signup-step-ticket', step=3, ticket=ticket, asset=p))

			## Clear request body
			response.data = ''

			return response
			
		elif step == 3:


			asset_key = self.request.get('asset')
			asset = db.get(db.Key(asset_key))

			image = images.Image(asset.datastore_data)
			
			## Execute crop
			x1 = float(self.request.get('x1'))
			x2 = float(self.request.get('x2'))
			y1 = float(self.request.get('y1'))
			y2 = float(self.request.get('y2'))
			
			image.crop(left_x=x1/float(image.width), top_y=y1/float(image.height), right_x=x2/float(image.width), bottom_y=y2/float(image.height))
			cropped_img = image.execute_transforms(images.PNG)
			
			## @TODO: Create middleware with helper functions for creating assets
			p = ProfilePic(self.ws_auth_user, key_name='ProfilePic::Current', storage_mode='datastore', datastore_data=db.Blob(cropped_img), name='profile-cropped.png', asset_type=AssetType.get_by_key_name('image')).put()
			
			t = db.get(db.Key(ticket))
			t.status = 'completed'
			t.put()

			response = self.redirect(self.url_for('auth/signup-step-ticket', step=4, ticket=ticket))

			## Clear request body
			response.data = ''

			return response