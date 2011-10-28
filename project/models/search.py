import config
import hashlib

from google.appengine.ext import db
from google.appengine.api import memcache

from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import UserAuditMixin
from project.models import CreatedModifiedMixin
from project.models.content_item import ContentItem


class Tag(SPIPolyModel, CreatedModifiedMixin):
	
	''' Ancestor model for a tag in the system. '''
	
	## Keyname = value of tag
	value = db.StringProperty()


class CalaisTag(Tag):
	
	''' A tag provided by OpenCalais. (shhh... coming soon) '''

	calais_id = db.StringProperty()
	
	
class UserTag(Tag, UserAuditMixin):
	
	''' A tag created by a user. '''
	pass


class StringSet(SPIPolyModel, CreatedModifiedMixin):
	
	''' Ancestor model for a set of strings linked to a content item. '''
	
	value = db.StringListProperty()
	content_item = db.ReferenceProperty(ContentItem, collection_name='string_sets')


class SubstringSet(StringSet):
	
	''' A set of substrings to match a content item with autocomplete. '''

	## Keyname = key of content item
	## Parent = content item
	pass
	
	
class KeywordSet(StringSet):
	
	''' A set of keywords (for indexing) linked to a content item. '''
	
	## Keyname = key of content item
	## Parent = content item
	pass
		
	
class TagSet(StringSet):
	
	''' A set of tags linked to a content item. '''
	
	## Keyname = key of content item
	## Parent = content item
	pass
	

class UserSearch(SPIPolyModel, CreatedModifiedMixin):

	search_terms = db.StringProperty()
	tag_filters = db.StringListProperty()
	repository_filter = db.StringProperty()
	category_filter = db.StringProperty()
	user = db.ReferenceProperty(collection_name='searches')


class SavedSearch(UserSearch):
	pass


class SearchHistory(UserSearch):
	pass
	
	
class ResultSet(SPIModel, CreatedModifiedMixin):
	
	ttl = config.config.get('wirestone.spi.search')['caching']['result_set_ttl']
	
	query = db.StringProperty()
	result = db.ListProperty(db.Key)
	
	@classmethod
	def _makeQueryID(cls, query):
		hash_ = hashlib.md5()
		hash_.update(query)
		return hash_.hexdigest()
	
	@classmethod
	def store(cls, query, results):
		id = cls._makeQueryID(query)
		obj = cls(key_name=id, query=query, result=results).put()
		memcache.store('SPISearch//ResultSet'+id, obj, time=cls.ttl)
		return obj
	
	@classmethod
	def find(cls, query):
		id = cls._makeQueryID(query)
		m = memcache.get('SPISearch//ResultSet'+id)
		if m is None:
			m = cls.get_by_key_name(id)
			return m
		return m
			
	
class ResultHint(SPIModel):
	pass