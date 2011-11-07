import config
import hashlib
import logging

from protorpc import remote

import webapp2

from project.services import RemoteService
from project.messages import data as messages

_query_cache = {}

ReservedParamNames = ['query']
QueryParamNames = [('iDisplayStart', int, 'offset'), ('iDisplayLength', int, 'limit'), ('iColumns', int, 'properties'),
					('offset', int, 'offset'), ('limit', int, 'limit'), ('keys_only', bool, 'keys_only')]


class DataService(RemoteService):
	
	model = None
	query = None
	query_params = {'offset':0, 'limit':25}
	request_params = {}
	request = None
	result = {}
	response = {}
	datagrid_params = {}
	
	def __init__(self):
		self.request = webapp2.get_request()
		
	@webapp2.cached_property
	def config(self):
		return config.config.get('wirestone.spi.api.data')
	
	def keyToMessage(self, key):
		if key.parent() is not None:
			parent = str(key.parent())
		else:
			parent = None
		return messages.ModelKey(value=str(key), kind=key.kind(), name=key.name(), id=key.id(), parent=parent)
	
	@classmethod
	def _flattenQuery(cls, query, limit, offset):
		query_obj = {}
		
		## Kind, Keys Only & Namespace
		query_obj['kind'] = query._model_class.kind()
		query_obj['keys_only'] = query._keys_only
		query_obj['namespace'] = query._namespace

		## Ancestor, Filters & Orders
		query_obj['orderings'] = query._Query__orderings
		query_obj['filters'] = query._Query__query_sets
		query_obj['ancestor'] = str(query._Query__ancestor)		

		## Fetch Params (added later)
		query_obj['limit'] = limit
		query_obj['offset'] = offset
		query_obj['cursor'] = str(query._cursor)
		query_obj['end_cursor'] = str(query._end_cursor)

		## Make Query ID
		query_id = cls._makeQueryID(query_obj)
		return query_id, query_obj
		
	@classmethod
	def _makeQueryID(cls, query):
		hash_ = hashlib.md5()
		hash_.update(str(query))
		return hash_.hexdigest()
	
	def buildDataAPIResponse(self):
		return self.result

	def buildDataTableResponse(self):
		if self.model is not None:
			grid = self.model.generateGrid()
			
			columns = grid.getColumnsForRPC()
			columnproto = grid.getColumnsForProto()
			modelproto = self.model.getProto()
			
			model_properties = []
			for m_property in modelproto['properties']:
				model_properties.append(messages.ModelProperty(name=m_property['name'], type=m_property['class'], label=m_property['label']))
			
			mproto = messages.ModelProto(kind=self.model.kind(), properties=model_properties)
			return messages.DatagridMeta(model_schema=mproto, columns=columnproto, rpc_fields=columns)
		
	def runQuery(self, query, limit=25, page=1, offset=None):

		if offset is None:
			offset = limit * (page-1)
		
		query_id, query_obj = self._flattenQuery(query, limit, offset)
		
		if self.config['query_caching']['enable'] == True:
			m = self.api.memcache.get('SPIDataAPI//QueryResult-'+query_id)
			if self.config['query_caching']['log_cache_rpcs'] == True: logging.info('--DataAPI Cacher: Checking for cached results at key "SPIDataAPI//QueryResult-'+str(query_id)+'".')
		else:
			m = None
		if m is None:
			result_obj = {}
			result_obj['count'] = query.count()
			if limit is False:
				result_obj['data'] = query.fetch(result_obj['count'], offset)
			else:
				result_obj['data'] = query.fetch(limit, offset) 
			result_obj['cursor'] = query.cursor()
			result_obj['length'] = len(result_obj['data'])
				
			query_obj['cursor'] = result_obj['cursor']
			query_obj['result'] = {'data':result_obj['data'], 'length': result_obj['length'], 'count':result_obj['count']}
				
			## Set hints for cache management
			if self.config['query_caching']['enable'] == True:
				cache_blocks = {}
				if isinstance(result_obj['data'], dict):
					result_data = result_obj['data'].values()
				elif isinstance(result_obj['data'], list):
					result_data = result_obj['data']
				for result_item in result_data:
					if not isinstance(result_item, (self.api.db.Key, self.api.db.db.Model)):
						continue
					if isinstance(result_item, self.api.db.Model):
						result_item = result_item.key()
					block = self.api.memcache.get('SPIDataAPI//CacheHint-'+str(result_item))
					if block is not None:
						block['QueryResults'].append('QueryResult-'+query_id)
					else:
						block = {'QueryResults':['QueryResult-'+query_id]}
					cache_blocks[str(result_item)] = block
				if len(cache_blocks) > 0:
					self.api.memcache.set_multi(cache_blocks, time=self.config['query_caching']['ttl'], key_prefix='SPIDataAPI//CacheHint-')
	
				self.api.memcache.set('SPIDataAPI//QueryResult-'+query_id, query_obj, time=self.config['query_caching']['ttl'])
				if self.config['query_caching']['log_cache_rpcs'] == True: logging.info('--DataAPI Cacher: Placing query cache results: "SPIDataAPI//QueryResult-'+str(query_id)+'": '+str(query_obj))
			return (result_obj['count'], result_obj['length'], result_obj['data'], result_obj['cursor'], self.buildDataTableResponse())
		else:
			if self.config['query_caching']['log_cache_rpcs'] == True: logging.info('--DataAPI Cacher: Found object. Returning.')
			return (m['result']['count'], m['result']['length'], m['result']['data'], m['cursor'], self.buildDataTableResponse())
		
	
def QueryResponder(func):

	def decorated(self, query={}, *args, **kwargs):

		## Retrieve 'mode' parameter
		mode = self.request.get('mode', False)
		if mode is False:
			self.request.get('mode', False)
			if mode is False:
				if mode in kwargs:
					mode = kwargs['mode']
					
		## Check for query params
		query_params = {}
		if isinstance(query, list):
			for entry in query:
				## @TODO: Add sorting here
				query_params[entry['name']] = entry['value']
			query = query_params
		
		## Get result of function call
		result = func(self, *args, **kwargs)
		
		## If it's a query, fetch results according to params and return
		if isinstance(result, (self.api.db.Query)):
			
			if 'keys_only' in query:
				result.keys_only = True

			if mode == 'datagrid':

				## == Get datagrid params (if they exist)
				self.datagrid_params['iColumns'] = int(query.get('iColumns',0))
				self.datagrid_params['iDisplayLength'] = min(int(query.get('iDisplayLength',10)), 100)
				self.datagrid_params['iDisplayStart'] = int(query.get('iDisplayStart',0))
				self.datagrid_params['iDisplayEnd'] = int(self.datagrid_params['iDisplayStart']+self.datagrid_params['iDisplayLength'])
				
				## == Adapt to DataGrids API
				self.query_params['limit'] = self.datagrid_params.get('iDisplayLength')
				self.query_params['offset'] = self.datagrid_params.get('iDisplayStart')

				## == Run Query
				query_result = self.runQuery(result, limit=self.query_params['limit'], offset=self.query_params['offset'])

				## == Populate Response
				self.result['iTotalRecords'] = query_result['count']
				self.result['data'] = query_result['data']
				self.result['iTotalDisplayRecords'] = len(self.result['data'])
				self.result['cursor'] = query_result['cursor']
			
				## Build response for datagrid if prompted
				return self.buildDataTableResponse()

			## == Run Query
			query_result = self.runQuery(result, limit=query.get('limit'), offset=query.get('offset'))

			self.result['data_count'] = query_result['count']
			self.result['data'] = query_result['data']
			self.result['cursor'] = query_result['cursor']

			return self.buildDataAPIResponse()
			
		else:
			self.result = result

    	return decorated


## Data API Exceptions
class DataAPIException(remote.ApplicationError): pass
class NotFoundError(DataAPIException): pass
class NotLoggedInError(DataAPIException): pass
class MalformedRequestError(DataAPIException): pass
class EmptyRequestError(DataAPIException): pass