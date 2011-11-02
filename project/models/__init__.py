# -*- coding: utf-8 -*-
## Project Models Init

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import Model
from apptools.model import Expando
from apptools.model import NDBModel
from apptools.model import NDBExpando
from apptools.model import Polymodel

import ndb as nndb
from ndb import model as nmodel
from google.appengine.ext import db as ldb

from project.mixins import UserAuditMixin
from project.mixins import CreatedModifiedMixin

from project.mixins import FormGeneratorMixin
from project.mixins import GridGeneratorMixin


class BlobInfo(Expando):
	
	''' Shortcut class to give us the ability to manually pull BlobInfo entities. '''
	
	@classmethod
	def kind(cls):
		return '__BlobInfo__'
		
		
class SPIModel(Model, FormGeneratorMixin, GridGeneratorMixin):
	
	''' Mid-level ancestor class for SPI models. '''
	
	@classmethod
	def _getModelPath(cls, seperator=None):
		
		path = [i for i in str(cls.__module__+'.'+cls.__name__).split('.')]
		
		if seperator is not None:
			return seperator.join(path)
			
		return path
		
	@classmethod
	def _getClassPath(cls, seperator=None):
		
		if hasattr(cls, '__class_hierarchy__'):
			path = [s_cls.__name__ for s_cls in cls.__class_hierarchy__]
			
			if seperator is not None:
				return seperator.join(path)
			return path
		else:
			return []
			
		@classmethod
		def getProto(cls):
			
			properties = []
			for prop, impl_class in cls.properties().items():
				if hasattr(impl_class, 'verbose_name') and impl_class.verbose_name != None:
					label = impl_class.verbose_name
				else:
					label = prop
				properties.append({'label': label, 'name': prop, 'class': str(impl_class.__class__.__name__)})
			return {'kind': cls.kind(), 'properties': properties}
			
			
class SPIExpandoModel(Expando):
	
	def _getModelPath(self, seperator=None):
		path = [i for i in str(self.__module__+'.'+self.__class__.__name__).split('.')]
		if seperator is not None:
			return seperator.join(path)
		return path
		
	def getProto(self):
		properties = []
		for prop in self.properties()+self.dynamic_properties():
			properties.append({'name': prop, 'class': str(properties[prop].__class__.__name__)})
		return {'kind': self.kind(), 'properties': properties}
		

class SPIPolyModel(Polymodel, SPIModel):
	pass