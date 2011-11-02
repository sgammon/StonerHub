import logging
import datetime
import simplejson as json

from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.blobstore import BlobKey
from google.appengine.ext.blobstore import BlobInfo

from project.handlers.ajax import SPIAjaxHandler
from project.models.content_item import ContentItem


class ContentItemList(SPIAjaxHandler):
	
	''' Return a list of content items. '''
	
	@classmethod
	def _get_model_json(cls, record):
		
		model_object = {

				'kind':record.kind(),
				'key':str(record.key()),
				'parent':str(record.parent()),
				'properties':{}

		}
		
		props = record.properties()
		for prop, field in props.items():
			val = getattr(record, prop)
			if isinstance(val, datetime.datetime):
				model_object['properties'][prop] = getattr(record, prop).isoformat()
			elif isinstance(val, db.Model):
				model_object['properties'][prop] = str(getattr(record, prop).key())
			elif isinstance(val, db.Key):
				model_object['properties'][prop] = str(getattr(record, prop))
			elif isinstance(val, blobstore.BlobInfo):
				prop_list_value.append(str(val.key()))				

			elif isinstance(val, list):
				prop_list_value = []
				if len(val) > 0:
					for subval in val:
						if isinstance(subval, datetime.datetime):
 							prop_list_value.append(subval.isoformat())
						elif isinstance(subval, db.Model):
							prop_list_value.append(str(subval.key()))
						elif isinstance(subval, db.Key):
							prop_list_value.append(str(subval))
						elif isinstance(subval, blobstore.BlobInfo):
							prop_list_value.append(str(subval.key()))
						else:
							prop_list_value.append(subval)
							
				model_object['properties'][prop] = prop_list_value
				
			else:
				model_object['properties'][prop] = getattr(record, prop)		
				
		return model_object
				
	
	def get(self):
		
		## Pull URL Parameters
		limit = self.request.get('limit', 25)
		offset = self.request.get('offset', 0)
		filters = self.request.get('filters', False)
		
		## Convert to a query
		c = ContentItem.all()
		
		## Apply filters
		if filters:
			filters = json.loads(filters)
			for item in filters:
				c.filter(item.property+' '+item.operator, item.value)
			
		## Fetch records
		records = c.fetch(limit, offset)
		
		## Set up meta object in response
		self.response_params['meta'] = {
		
			'count':len(records),
			'limit':limit,
			'offset':offset,
			'proto':[{i:k.__class__.__name__} for i, k in ContentItem.properties().items()]
		
		}
		
		## Add records to response
		self.response_params['records'] = []
		if len(records) > 0:
			for record in records:
				self.response_params['records'].append(self._get_model_json(record))
			
		## Render JSON Response
		self.render('list_content_items')
		
		
	def post(self):
		return self.get()