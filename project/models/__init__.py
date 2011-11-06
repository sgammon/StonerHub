# -*- coding: utf-8 -*-
## Project Models Init

import os
import sys
import logging

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import BaseModel
from apptools.model import BaseExpando
from apptools.model import NDBModel
from apptools.model import NDBExpando

###### ====== Polymorphic Datamodel Tools ====== ######
from apptools.model.polypro import _class_map
from apptools.model.polypro import _LOG_IMPORTS
from apptools.model.polypro import _PATH_SEPERATOR, _KEY_NAME_SEPERATOR
from apptools.model.polypro import _ClassKeyProperty, _ModelPathProperty
from apptools.model.polypro import _CLASS_KEY_PROPERTY, _PATH_KEY_PROPERTY

import ndb as nndb
from ndb import model as nmodel
from google.appengine.ext import db as ldb

from project.mixins import UserAuditMixin
from project.mixins import CreatedModifiedMixin

from project.mixins import FormGeneratorMixin
from project.mixins import GridGeneratorMixin


class BlobInfo(BaseExpando):
	
	''' Shortcut class to give us the ability to manually pull BlobInfo entities. '''
	
	@classmethod
	def kind(cls):
		return '__BlobInfo__'
		
		
class BaseSPIModel(object):
	
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
				
		
class SPIModel(BaseModel, BaseSPIModel, FormGeneratorMixin, GridGeneratorMixin):
	
	''' Mid-level ancestor class for SPI models. '''
			
			
class SPIExpandoModel(BaseExpando):
	
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


class PolymorphicModel(ldb.PropertiedClass):

	''' Populates properties like __root_class__ and __class_hierarchy__ and enforces logic about direct instantiation. '''

	def __init__(cls, name, bases, dct):

		if name == 'SPIPolyModel':
			super(PolymorphicModel, cls).__init__(name, bases, dct, map_kind=False)
			return

		elif SPIPolyModel in bases:
			if getattr(cls, '__class_hierarchy__', None):
				raise ldb.ConfigurationError(('%s cannot derive from SPIPolyModel as '
				'__class_hierarchy__ is already defined.') % cls.__name__)
			cls.__class_hierarchy__ = [cls]
			cls.__root_class__ = cls
			super(PolymorphicModel, cls).__init__(name, bases, dct)

		else:
			super(PolymorphicModel, cls).__init__(name, bases, dct, map_kind=False)

			cls.__class_hierarchy__ = [c for c in reversed(cls.mro())
				if issubclass(c, SPIPolyModel) and c != SPIPolyModel]

			if cls.__class_hierarchy__[0] != cls.__root_class__:
				raise ldb.ConfigurationError(
					'%s cannot be derived from both root classes %s and %s' %
					(cls.__name__,
					cls.__class_hierarchy__[0].__name__,
					cls.__root_class__.__name__))

		_class_map[cls.class_key()] = cls


class SPIPolyModel(ldb.Model, BaseSPIModel):

	__metaclass__ = PolymorphicModel

	# stores class inheritance/ancestry (list property)
	_class_property = _ClassKeyProperty(name=_CLASS_KEY_PROPERTY)

	# stores python package import path
	_model_path_property = _ModelPathProperty(name=_PATH_KEY_PROPERTY,indexed=False)

	def __new__(cls, *args, **kwds):

	 	''' Prevents direct instantiation of SPIPolyModel. '''

		if cls is SPIPolyModel:
			raise NotImplementedError() # raise NotImplemented
		return super(SPIPolyModel, cls).__new__(cls, *args, **kwds)

	def __init__(self, *args, **kwargs):

		''' Initiates the SPIPolyModel object. '''

		super(SPIPolyModel, self).__init__(*args, **kwargs)

	@classmethod
	def kind(cls):

		''' Always return name of root class. '''

		if cls.__name__ == 'SPIPolyModel': return cls.__name__
		else: return cls.class_key()[0]

	@classmethod
	def class_key(cls):

		''' Returns class path (in tuple form). '''

		if not hasattr(cls, '__class_hierarchy__'):
			raise NotImplementedError('Cannot determine class key without class hierarchy')
		return tuple(cls.class_name() for cls in cls.__class_hierarchy__)

	@classmethod
	def class_name(cls):

		''' Returns the name of the current class. '''

		return cls.__name__

	@classmethod
	def path_key(cls):

		''' Returns the Python import path for the implementation class (in tuple form). '''

		if not hasattr(cls, _PATH_KEY_PROPERTY):
			return tuple(i for i in str(cls.__module__+'.'+cls.__name__).split('.'))
		else:
			path_t = getattr(cls, _PATH_KEY_PROPERTY).split(_PATH_SEPERATOR)
			return tuple('.'.join(path_t).split('.'))

	def path_module(self):

		''' Returns the module part of the Python import path for the implementation class (in tuple form). '''

		if not hasattr(self, _PATH_KEY_PROPERTY):
			return tuple(self.__module__.split('.'))
		else:
			path_t = getattr(self, _PATH_KEY_PROPERTY).split(_PATH_SEPERATOR)
			return tuple(path_t[0].split('.'))

	def path_module_name(self):

		''' Returns the module part of the Python import path for the implementation class (in string form). '''

		if not hasattr(self, _PATH_KEY_PROPERTY):
			return str(self.__module__)
		else:
			path_t = getattr(self, _PATH_KEY_PROPERTY).split(_PATH_SEPERATOR)
			return path_t[0]

	@classmethod
	def path_class(cls):

		''' Returns a Python 'class' object of the implementation class. '''

		if _class_map[cls.class_key()] is not None:
			return _class_map[cls.class_key()]
		else: return cls

	@classmethod
	def from_entity(cls, entity):

		''' Overrides db.Model's from_entity to lazy-load the implementation class if it isn't in _kind_map. '''

		global _class_map

		if(_PATH_KEY_PROPERTY in entity and
		   tuple(entity[_PATH_KEY_PROPERTY]) != cls.path_key()):
			key = entity[_PATH_KEY_PROPERTY].split(':')
			try:
				abspath = os.path.abspath(os.path.dirname(__file__))
				if abspath not in sys.path:
					sys.path.insert(0,abspath)

					tx_path = []
					for index, key_chunk in enumerate(key):
						if key_chunk == 'wirestone':
							tx_path.append('project')
						elif key_chunk == 'spi':
							continue
						else:
							tx_path.append(key_chunk)

					module = __import__(str('.'.join(tx_path[0:-1])), globals(), locals, str(tx_path[-1])) #### FIX THIS
					imported_class = getattr(module, key[-1])
					obj = imported_class()
					_class_map[obj.class_key()] = obj.__class__

					return obj.from_entity(entity)

			except ImportError:
				raise ldb.KindError('Could not import model hierarchy \'%s\'' % str(key))

		if (_CLASS_KEY_PROPERTY in entity and
			tuple(entity[_CLASS_KEY_PROPERTY]) != cls.class_key()):
			key = tuple(entity[_CLASS_KEY_PROPERTY])
			try:
				poly_class = _class_map[key]
			except KeyError:
				raise ldb.KindError('No implementation for class \'%s\'' % (key,))

			return poly_class.from_entity(entity)
		return super(SPIPolyModel, cls).from_entity(entity)

	@classmethod
	def class_key_as_list(cls):

		''' Returns class path (in list form). '''

		if not hasattr(cls, '__class_hierarchy__'):
			raise NotImplementedError('Cannot determine class key without class hierarchy')
		return list(cls.class_name() for cls in cls.__class_hierarchy__)

	@classmethod
	def all(cls, **kwds):

		''' Automatically filter queries by class name. '''

		query = super(SPIPolyModel, cls).all(**kwds)
		if cls != SPIPolyModel:
			query.filter(_CLASS_KEY_PROPERTY + ' =', cls.class_name())
		return query

	@classmethod
	def gql(cls, query_string, *args, **kwds):

		''' Automatically filter GQL queries by class name. '''

		if cls == cls.__root_class__:
			return super(SPIPolyModel, cls).gql(query_string, *args, **kwds)
		else:
			from google.appengine.ext import gql

			query = ldb.GqlQuery('SELECT * FROM %s %s' % (cls.kind(), query_string))

			query_filter = [('nop',[gql.Literal(cls.class_name())])]
			query._proto_query.filters()[(_CLASS_KEY_PROPERTY, '=')] = query_filter
			query.bind(*args, **kwds)
			return query

_proto_ = ['assets','client','content','content_item','search','security','social','system','ticket']