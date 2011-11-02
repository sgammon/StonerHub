from webapp2 import Router
url_for = Router.build

from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.db import polymodel

from project.models import SPIModel
from project.models import SPIPolyModel

from project.mixins import UserAuditMixin
from project.mixins import CreatedModifiedMixin

from project.models.security import User as WirestoneUser


class AssetType(SPIModel):
	
	''' A type of asset to be stored in the dynamic asset system. '''

	## key_name = name
	name = db.StringProperty()
	mimetypes = db.StringListProperty(default=[])
	expiration = db.StringProperty()
	parent_type = db.SelfReferenceProperty(collection_name='children')


class StoredAsset(SPIModel, CreatedModifiedMixin, UserAuditMixin):
	
	''' An asset to be served/stored dynamically. Not content - these are images/scripts/styles that are used in site structure. '''

	## key_name = shortname
	name = db.StringProperty()
	filename = db.StringProperty()
	size = db.IntegerProperty()
	mime_type = db.StringProperty(default='application/octet-stream')
	asset_type = db.ReferenceProperty(AssetType, collection_name='assets')
	version = db.IntegerProperty(default=1)
	
	# Storage properties
	storage_mode = db.StringProperty(choices=['blobstore', 'datastore'])
	datastore_data = db.BlobProperty()
	blobstore_data = blobstore.BlobReferenceProperty()
	
	# Methods to access assets
	def getServingURL(self):
		try:
			if self.storage_mode == 'blobstore':
				return url_for('media-serve-blob-filename', blobkey=self.blobstore_data.key(), filename=self.blobstore_data.filename)
			else:
				return url_for('media-serve-blob', blobkey=str(self.key()), filename=self.name)
		except db.Error:
			return False
			
	def deleteData(self):
		if self.storage_mode == 'datastore':
			return True
		elif self.storage_mode == 'blobstore':
			self.blobstore_data.delete()
			return True
			
	def getAsset(self):
		if self.storage_mode == 'datastore':
			return {'key': self.key(), 'filename': self.filename, 'size':None, 'mime': self.mime_type, 'version': version, 'mode': self.storage_mode}
		elif self.storage_mode == 'blobstore':
			return {'key': self.blobstore_data.key(), 'filename': self.blobstore_data.filename, 'size': self.blobstore_data.size, 'mime': self.mime_type, 'version': self.version, 'mode': self.storage_mode}
		else:
			return None
	
	def getDownloadURL(self):
		try:
			if self.storage_mode == 'blobstore':
				return url_for('media-download-blob-filename', blobkey=self.blobstore_data.key(), filename=self.blobstore_data.filename)
			else:
				return url_for('media-download-blob-filename', blobkey=str(self.key()), filename=self.name)
		except db.Error:
			return False
			
	@classmethod
	def provisionAsset(cls, storage_mode, data=None, version=1, parent=None, key_name=None, **kwargs):
		asset = cls(parent, key_name=key_name, version=version, **kwargs)
		if storage_mode == 'blobstore':
			asset.storage_mode = 'blobstore'
			asset.blobstore_data = data
		elif storage_mode == 'datastore':
			asset.storage_mode = 'datastore'
			asset.datastore_data = data
		return asset.put()
		
	@classmethod
	
	def provisionBlobstoreAsset(cls, data=None, version=1, parent=None, key_name=None, **kwargs):
		return cls.provisionAsset('blobstore', data, version, parent, key_name, **kwargs)
	
	@classmethod
	def provisionDatastoreAsset(cls, data=None, version=1, parent=None, key_name=None, **kwargs):
		return cls.provisionAsset('datastore', data, version, parent, key_name, **kwargs)
	
	
class ImageAsset(StoredAsset):
	
	''' A dynamically stored image. '''

	width = db.IntegerProperty()
	height = db.IntegerProperty()
	fast_serving_url = db.StringProperty(default=None)
	enable_fast_serving = db.BooleanProperty(default=False)

	# Methods to access assets
	def getServingURL(self):
		if self.enable_fast_serving:
			return self.fast_serving_url
		else:
			return super(ImageAsset, self).getServingURL()
			
	# Methods for high performance images API
	def isFastServingCompatible(self):
		if self.storage_mode == 'blobstore':
			return True
		return False
		
	def isFastServingEnabled(self):
		return self.enable_fast_serving
		
	def fastServingURL(self):
		return self.fast_serving_url
	
	def constructFastServingURL(self):
		self.fast_serving_url = images.get_serving_url(str(self.blobstore_data.key()))
		self.enable_fast_serving = True
		return True
	
	
class ProfilePic(ImageAsset):
	
	''' A user's profile picture. '''
	
	user = db.ReferenceProperty(WirestoneUser, collection_name='profile_pictures')
	
	
class StyleAsset(StoredAsset):
	
	''' A dynamically stored stylesheet. '''
	
	media = db.StringProperty(choices=['screen','tty','tv','projection','handheld','print','all'])
	
	
class ScriptAsset(StoredAsset):
	
	''' A dynamically stored script. '''
	
	pass