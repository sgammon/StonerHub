import logging

from mapreduce import input_readers
from mapreduce import operation as op

from google.appengine.api import datastore
from project.models.content_item import ContentItem

def fix_content_items(key):
	
	entity = datastore.Get(key)
	
	## Change _path_
	newpath = ['project']
	for item in entity['_path_'].split(':'):
		if item in ['wirestone', 'spi', 'project']:
			continue
		else:
			newpath.append(item)
	
	logging.info('Oldpath: '+str(entity['_path_'])+' to newpath: '+str(newpath))

	entity['_path_'] = ':'.join(newpath)
	
	## Change _class_
	if entity['_class_'][-1] == 'Document' and entity['_class_'][-2] == 'DimensionedContent':
		entity['_class_'] = ['ContentItem', 'File', 'Document']
		logging.info('Overwrote class: '+str(entity['_class_']))
	
	## Remove category
	logging.info('Removing category: '+str(entity['category']))
	entity['category'] = None
	
	newentity = ContentItem.from_entity(entity)
	yield op.db.Put(newentity)