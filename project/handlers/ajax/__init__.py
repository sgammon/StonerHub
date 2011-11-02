import config
import logging

from google.appengine.api import quota
from project.handlers import WebHandler

try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		try:
			from django.utils import simplejson as json
		except ImportError:
			logging.critical('No valid JSON adapter found.')


class SPIAjaxHandler(WebHandler):
	
	''' Renders a given template variable set as a JSON response. '''
	
	response_params = {}
	
	def _build_meta_obj(self):
		
		## Retrieve config
		main_config = config.config.get('wirestone.spi')
		dev_config = config.config.get('wirestone.spi.dev')
		
		## Build meta object
		meta_obj = {
		
			'platform':{
				
				'version':{
					'version_major':main_config['version_major'],
					'version_minor':main_config['version_minor'],
					'version_micro':main_config['version_micro'],
					'version_phase':main_config['version_phase'],
				}
			
			}
		
		}
		
		if dev_config['dev_mode'] == True:
			
			## Add usage information for request to dev response
			meta_obj['request'] = {
			
				'cpu_usage': quota.get_request_cpu_usage(),
				'cpu_api': quota.get_request_api_cpu_usage()
			
			}
			
			## Add dev config to dev response
			meta_obj['platform']['dev'] = {
			
				'debug':dev_config['debug'],
				'dev_mode':dev_config['dev_mode']
			
			}
				
		return meta_obj
		

	def fail(self, operation, reason):
		
		## Create the beginnings of the response object
		response_object = {
			'operation':operation,
			'result':'failure',
			'response': {'failure_reason':reason},
			'meta': self._build_meta_obj()
		}
			
		## Generate JSON response, set appropriate headers
		self.response.write(json.dumps(response_object))
		self.response.headers['Content-Type'] = 'text/json'

	
	def render(self, operation, **kwargs):
		
		## Create the beginnings of the response object
		response_object = {
			'operation':operation,
			'result':'success',
			'response': {},
			'meta': self._build_meta_obj()
		}
					
		if isinstance(kwargs, dict) and len(kwargs) > 0:
			for key, value in kwargs.items():
				self.response_params[key] = value
					
		## Generate Response dict
		response_object['response'] = self.response_params
		
		## Return generated JSON string
		self.response.write(json.dumps(response_object))
		self.response.headers['Content-Type'] = 'text/json'