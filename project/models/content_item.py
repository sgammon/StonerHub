import logging

from webapp2 import cached_property

from google.appengine.ext import db
from google.appengine.ext import search
from google.appengine.api import memcache
from google.appengine.ext import blobstore

from wtforms import widgets

from project.core import security as WirestoneSecurity

from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import SPIExpandoModel
from project.models import UserAuditMixin
from project.models import CreatedModifiedMixin
from project.models.assets import StoredAsset
from project.models.content import Repository
from project.models.content import ContentItemType
from project.models.content import ContentItemFormat
from project.models.content import ContentItemCategory

from project.mixins import FormGeneratorMixin
from project.mixins import GridGeneratorMixin

from project.models.security import User as WirestoneUser
from project.models.security import PermissionsDescriptor


def getContentItemCategoryOptions(limit=80):
	
	''' Retrieves a list of category options for a form dropdown box, with proper indentation. '''

	m = memcache.get('SPIRuntime//ContentItemCategories')
	if m is None:
		q = ContentItemCategory.all()
		categories = q.fetch(q.count())
		categories_list = {}
		for category in categories:
			repository = category.parent_key()
			if str(repository) not in categories_list:
				categories_list[str(repository)] = []
			categories_list[str(repository)].append({'name':str(category.key()), 'value':category.name})
		if len(categories_list) > 0:
			memcache.set('SPIRuntime//ContentItemCategories', categories_list)
		return categories_list
	else: return m
	

class ContentItem(SPIPolyModel, CreatedModifiedMixin, UserAuditMixin):

	''' An actual content item. '''
	
	_index_config = {
						'properties':['title','description'],
					}
	
	_form_config = {
						'fields':
						[
							'title',
							'description',

							('type',{'select_instruction_text':'Select a Type',
									 'label_attr':'name'}),

							('format',{'select_instruction_text':'Select a Format',
									   'label_attr':'name'}),

							('category',{'select_instruction_text':'Select a Category'}),
										
							('repository', {'select_instruction_text': 'Select a Repository',
											'label_attr':'name'}),

							#('permissions_mode',{'default': 'Open',
							#					 'widget':widgets.ListWidget(prefix_label=False),
							#					 'option_widget':widgets.RadioInput()}),
							#('permissions_descriptor', 'permissions.Descriptor')
						]
						
					}
					
	_grid_config = {
						'grid':{'aoColumns':'ciColumns'},
						'columns':[('Title','title'),('Type','type'),('Repository','repository'),('Description','description'),('Tags','tags'),('Category','category')],
						'script_snippet':'ci_default.js'
					}
	
	## Item Details
	title = db.StringProperty(verbose_name='Title') #indexed
	description = db.TextProperty() # indexed
	
	## Item Status
	status = db.StringProperty(choices=['queued','processing','serving'], default='queued')

	## Data Properties ('data' property added in child classes)
	type = db.ReferenceProperty(ContentItemType, collection_name='content_items')
	asset = db.ReferenceProperty(StoredAsset, default=None)
	assets = db.ListProperty(db.Key) ## holds past versions, only if there are past versions
	format = db.ReferenceProperty(ContentItemFormat, collection_name='content_items')
	category = db.ReferenceProperty(ContentItemCategory, collection_name='content_items')
	repository = db.ReferenceProperty(Repository, collection_name='content_items')		  

	## Cached Lists
	tags = db.ListProperty(db.Key, indexed=True)
	social_likes = db.StringListProperty(indexed=False)
	social_like_users = db.StringListProperty(indexed=False)
	social_comments = db.StringListProperty(indexed=False)	

	## Permission Settings
	permissions_mode = db.StringProperty(choices=['Open','Group','Role','ACL','Closed'])
	permissions_descriptor = db.ReferenceProperty(PermissionsDescriptor, collection_name='content_item')
	
	## Social
	like_count = db.IntegerProperty(default=0)
	rating_count = db.IntegerProperty(default=0)
	average_rating = db.RatingProperty(default=None)
	comment_count = db.IntegerProperty(default=0)
	view_count = db.IntegerProperty(default=0)	
	
	## Maintenance
	do_healthcheck = db.BooleanProperty(default=True)
	last_healthcheck = db.DateTimeProperty(default=None)
		
	def currentUserLike(self):
		u = WirestoneSecurity.get_current_user()
		if u == None:
			return u
		else:
			if str(db.Key.from_path('User', u.nickname())) in self.social_like_users:
				return True
			else:
				return False
				
	def getAsset(self):
		return self.asset.getAsset()
		
	def deleteAsset(self):
		self.asset.deleteData()
		self.asset.delete()