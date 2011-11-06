# -*- coding: utf-8 -*-

import os
import config
import logging

from webapp2 import cached_property
from webapp2_extras import sessions

## AppTools Imports
from apptools.core import BaseHandler

from project.core import security
from project.core.security import _ws_enforce_security
from project.models.content import Repository

from project.models.social import SocialNotification


class WebHandler(BaseHandler, security.WirestoneOpenIDAuthMixin):
	
	''' Handler for desktop web requests. '''
	
	logging = logging

	## Authentication Config ##
	skipAuth = False
	adminOnly = False

	## Authentication State ##
	ws_auth_user = None
	ws_auth_session = {}	
	ws_auth_username = None
	ws_auth_is_user_admin = False
	ws_auth_is_user_developer = False

	universal_dependencies = ['jQuery', 'main']
	
	@cached_property
	def session(self):
		return self.session_store.get_session()
	
	def dispatch(self):
		self.session_store = sessions.get_store(request=self.request)
		
		if self.adminOnly:
			auth_result, redirect_or_session = _ws_enforce_security(self, 'admin', self.authConfig)
		else:
			auth_result, redirect_or_session = _ws_enforce_security(self, 'user', self.authConfig)

		authComplete = False
		if self.skipAuth != True:
			if auth_result is False: ## user failed authentication tests somewhere
				logging.info('Returning redirect, user is not logged in...')
				return self.redirect(redirect_or_session, abort=True)
			else:
				authComplete = True
		else:
			authComplete = True

		if authComplete == True: ## just a silly safeguard...
			try:
				return super(WebHandler, self).dispatch()
			finally:
				self.session_store.save_sessions(self.response)

	## Cached Properties
	@cached_property
	def OutputConfig(self):
		return config.config.get('wirestone.spi.output')
	
	@cached_property
	def HandlerConfig(self):
		return config.config.get('wirestone.spi.output.request_handler')
	
	@cached_property
	def DependenciesConfig(self):
		return config.config.get('wirestone.spi.output.request_handler')['dependencies']

	@cached_property
	def ServicesConfig(self):
		return config.config.get('apptools.project.services')
		
	@cached_property
	def GlobalServicesConfig(self):
		return config.config.get('apptools.services')
	
	def _bindRuntimeTemplateContext(self, context):
		
		context['page'] = {
		
			'ie': False, ## are we serving to IE?
			'mobile': False, ## are we serving to mobile?
			'appcache': {
				'enabled': False, ## enable/disable appcaching
				'location': None, ## location for appcache manifest
			},
			'services': {
				'services_manifest': self.make_services_manifest(),
				'global_config': self.GlobalServicesConfig
			}, ## enable API services
		
		}
		
		if self.uagent is not None and len(self.uagent) > 0:
			## Detect if we're handling a request from IE, and if we are, tell the template context
			if self.uagent['browser']['name'] == 'MSIE':
				context['page']['ie'] = True
		
		return context
	
	def _resolve_and_run_dependency(self, name):
		
		''' Finds and runs a requested dependency package (i.e. jQuery) from config, runs it and returns the result. '''
		
		cfg = self.DependenciesConfig		
		
		if name in cfg['packages']:
			path = cfg['packages'][name]['module'].split('.')
			try:
				_m = __import__('.'.join(path[0:-1]), globals(), locals(), [path[-1]])
				package = getattr(_m, path[-1])
			except:
				return False
			north_dependencies, south_dependencies = package(self).get_sections()
			dependency = {'name':name,'module':cfg['packages'][name]['module'],'north':north_dependencies, 'south':south_dependencies}
			return dependency
		else:
			return False
		
	
	## Load dependencies
	def load_dependencies(self, local):

		''' Parses dependencies list and compiles it into a system var that is passed to __north and __south. '''

		_dependency_cache = self.api.memcache.get('SPIRuntime//Dependencies')
		if _dependency_cache is None:
			_dependency_cache = {}

		cfg = self.DependenciesConfig

		cmp_html = {'north':'', 'south':''}
		cmp_dependencies = cfg['always_include']+local
		if isinstance(cmp_dependencies, list) and len(cmp_dependencies) > 0:

			for dependency in cmp_dependencies:

				## Check cache first
				if dependency in _dependency_cache:
					cmp_html['north'] += "\n".join(_dependency_cache[dependency]['north'])
					cmp_html['south'] += "\n".join(_dependency_cache[dependency]['south'])

				else:
					dep_content = self._resolve_and_run_dependency(str(dependency).lower())
					if dep_content is False:
						logging.warning('Template dependency "'+str(dependency)+'" failed to load.')
					else:
						## Add to cache
						_dependency_cache[dependency] = dep_content

						## Compile for current page
						cmp_html['north'] += "\n".join(dep_content['north'])
						cmp_html['south'] += "\n".join(dep_content['south'])

		## Cache compiled dependencies
		self.api.memcache.set('SPIRuntime//Dependencies', _dependency_cache)

		## Return compiled dependency HTML for north and south
		return (cmp_html['north'], cmp_html['south'])

	
	def make_services_manifest(self):

		## Generate list of services to expose to user
		svcs = []
		opts = {}

		jsapi_cache = self.api.memcache.get('apptools//services_manifest')
		if jsapi_cache is not None:
			return jsapi_cache
		else:
			for name, config in self.ServicesConfig['services'].items():
				if config['enabled'] is True:

					security_profile = self.GlobalServicesConfig['middleware_config']['security']['profiles'].get(config['config']['security'], None)

					caching_profile = self.GlobalServicesConfig['middleware_config']['caching']['profiles'].get(config['config']['caching'], None)

					if security_profile is None:

						## Pull default profile if none is specified
						security_profile = self.GlobalServicesConfig['middleware_config']['security']['profiles'][self.GlobalServicesConfig['defaults']['service']['config']['security']]

					if caching_profile is None:
						caching_profile = self.GlobalServicesConfig['middleware_config']['caching']['profiles'][self.GlobalServicesConfig['defaults']['service']['config']['caching']]

					## Add caching to local opts
					opts['caching'] = caching_profile['activate'].get('local', False)

					## Grab prefix
					service_action = self.ServicesConfig['config']['url_prefix'].split('/')

					## Add service name
					service_action.append(name)

					## Join into endpoint URL
					service_action_url = '/'.join(service_action)

					## Expose depending on security profile
					if security_profile['expose'] == 'all':
						svcs.append((name, service_action_url, config, opts))

					elif security_profile['expose'] == 'admin':
						if users.is_current_user_admin():
							svcs.append((name, service_action_url, config, opts))

					elif security_profile['expose'] == 'none':
						continue

			self.api.memcache.set('apptools//services_manifest', svcs)
			return svcs

		
	def render(self, template, vars={}, dependencies=[], **kwargs):
		
		''' Wrapper to AppTools' render function. '''
		
		ext_north, ext_south = self.load_dependencies(dependencies)
		superbar_values = {'navigation': []}
		superbar_config = config.config.get('wirestone.spi.output.elements.superbar')
		
		for element in superbar_config['navigation']:
			
			if element['label'] == 'Repositories':
				subnav = []
				r = self.api.memcache.get('RepositoriesList', namespace='SPIRuntime')
				if r is None:
					r = Repository.all().fetch(config.config.get('wirestone.spi.datamodel.repository')['max_repositories'])
					self.api.memcache.set('RepositoriesList', r, namespace='SPIRuntime')
				if r == []:
					subnav.append(('Create the first Repository', 'Create the first repository', self.url_for('repository-create')))
				else:
					for repo in r:
						subnav.append((repo.name, repo.description, self.url_for('repository-content', repo=repo.key().name())))

			else:
				if element['subnav'] != False:
					subnav = []
					for sub_element in element['subnav']:
						subnav.append((sub_element['label'], sub_element['title'], self.url_for(sub_element['endpoint'])))
				else:
					subnav = False

			superbar_values['navigation'].append((element['label'], element['title'], self.url_for(element['endpoint']), subnav))

		# UserOps
		if self.ws_auth_user is not None:
			channel_id = self.api.memcache.get('channel-id-'+str(self.ws_auth_user.key()))
			if channel_id is None:
				try:
					channel_id = self.api.channel.create_channel('channel-id-'+str(self.ws_auth_user.key()))
					memcache.set('channel-id-'+str(self.ws_auth_user.key()), channel_id, time=3600)
				except:
					channel_id = None

			notifications = SocialNotification.all().ancestor(self.ws_auth_user).filter('is_read =', False)
			n_count = notifications.count()
			if n_count == 0:
				notifications = False
			else:
				all_notifications = notifications.order('-createdAt').fetch(10)

				notifications = {'uploads': [], 'actions': [], 'count': n_count}
				for notification in all_notifications:
					if notification.class_name() == 'QueueNotification':
						notifications['uploads'].append(notification)
					else:
						notifications['actions'].append(notification)

				logging.info('FINAL NOTIFICATIONS: '+str(notifications))
		else:
			channel_id = None
			notifications = False

		# Generate 'sys' variable
		sys = {

			'zones':{
				'admin':False,
				'dev':False
			},
			'session':self.session,
			'request':self.request,
			'security':{
				'user':self.ws_auth_user
			},
			'env':os.environ,
			'request':self.request,
			'config':config.config,
			'elements': {
				'appcache': {},
				'superbar':superbar_values,
				'makeChannel': config.config.get('wirestone.spi.notifications')['make_channel']
			}

		}

		## Load appcache settings
		sys['elements']['appcache'] = {'enabled': self.OutputConfig['enable_appcache'], 'location': self.OutputConfig['appcache_location']}

		# Generate 'user' variable
		social = {
			'notifications': notifications
		}

		# Populate Dev/Admin zones
		if hasattr(self, 'adminZone'):
			sys['zones']['admin'] = True
		if hasattr(self, 'devZone'):
			sys['zones']['dev'] = True

		try:
			u = self.auth_current_user()
			sys['security']['user'] = u
		except Exception, e:
			pass

		# sys kwarg is discarded to prevent injection
		if 'sys' in kwargs:
			del kwargs['sys']
		if 'makeChannel' in kwargs:
			sys['elements']['makeChannel'] = kwargs['makeChannel']

		# Generate 'tpl' variable
		tpl = {

			'channel_id':channel_id,

			'dependencies': {

				'north':ext_north, ## Compiled HTML for dependencies using north
				'south':ext_south ## Compiled HTML for dependencies using south

			}

		}

		# tpl kwarg is discarded to prevent injection
		if 'tpl' in kwargs:
			del kwargs['tpl']

		# 'vars' entries override conflicts with kwargs...
		if isinstance(vars, list) and len(vars) > 0:
			for var in vars:
				kwargs[var] = vars[var]
				
		context = {'sys': sys, 'tpl': tpl, 'social': social}
		for k, v in vars.items():
			context[k] = v
		for k, v in kwargs.items():
			context[k] = v

		# Add sys context, return rendered Jinja2 template
		return super(WebHandler, self).render(template, **context)
	
	
class MobileHandler(BaseHandler):
	
	''' Handler for mobile web requests. '''
	
	def _bindRuntimeTemplateContext(self, context):
		
		context['page'] = {
		
			'ie': False,
			'mobile': True
		
		}
		
		return context