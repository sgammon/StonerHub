from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.db import polymodel

from project.models import SPIModel
from project.models import UserAuditMixin
from project.models import CreatedModifiedMixin
from project.models.assets import ImageAsset
from project.models.security import User as WirestoneUser
from project.models.security import PermissionsDescriptor

from wtforms import widgets


class QueuedBlob(SPIModel, CreatedModifiedMixin):
	
	blob = blobstore.BlobReferenceProperty()
	filename = db.StringProperty()
	title = db.StringProperty()
	description = db.TextProperty()
	author = db.ReferenceProperty(WirestoneUser, collection_name='queued_blobs')	


class Repository(SPIModel, CreatedModifiedMixin, UserAuditMixin):

	''' Namespaces content data to a certain repository. '''
	
	#_form_fields = ['name', 'description', 'permissions_mode', ('permissions_descriptor', 'permissions.Descriptor', {'form':{'label':'Permissions'}})]

	_form_config = {
						'fields':
						[
							'name',
							'description',
							#('permissions_mode', {'widget':widgets.ListWidget(prefix_label=False),
							#					'option_widget':widgets.RadioInput()}),
							#('permissions_descriptor', 'permissions.Descriptor', {'label': 'Permissions', 'default':None})
						]
						
					}

	## key_name = repository shorttext
	name = db.StringProperty()
	description = db.TextProperty()
	
	## Security Params
	permissions_mode = db.StringProperty(choices=['Open','Group','Role','ACL','Closed'])
	permissions_descriptor = db.ReferenceProperty(PermissionsDescriptor, collection_name='repository')

	
class ContentItemType(SPIModel):

	''' Example: 'File' or 'Request for Proposal' '''
	## key_name = type name, lowercase
	
	_grid_config = {'columns':[('Name', 'name')]}

	name = db.StringProperty(verbose_name='Name')
	model_impl_class = db.StringProperty(default='project.models.content_item.ContentItem',verbose_name='Implementation Class')
	

class ContentItemFormat(SPIModel):

	''' Example: 'Microsoft Word' or 'pdf'. '''
	
	_form_fields = ['name', 'icon', 'mime_type', 'guessable']

	## key_name = file extension
	name = db.StringProperty()
	icon = db.StringProperty()
	type = db.ReferenceProperty(ContentItemType, collection_name='formats', default=None)
	valid_extensions = db.StringListProperty()
	
	## Format Details
	mime_type = db.StringListProperty()
	guessable = db.BooleanProperty(default=False)
	
	
class ContentItemCategory(SPIModel):
	
	''' Example: 'Report' or 'Word of Mouth Marketing' '''
	## key_name = name, lowered
	
	_form_config = {
						'fields':
						[
							'name',
							'description',
						]
						
					}


	name = db.StringProperty()
	description = db.TextProperty()
	parent_category = db.SelfReferenceProperty(collection_name='child_categories')