# -*- coding: utf-8 -*-
import sys
import logging
import bootstrap

bootstrap.AppBootstrapper.prepareImports()

import config

try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		try:
			from django.utils import simplejson as json
		except ImportError:
			logging.critical('No compatible JSON adapter found.')

## Pipeline library
import pipeline
from pipeline import common

from google.appengine.ext import db
from google.appengine.api import xmpp
from google.appengine.api import channel
from google.appengine.api import memcache
from google.appengine.api import taskqueue


#### ==== Pipeline Support Framework ==== ####
class SPIPipelineLogger(object):

	enable = False
	dispatch_args = {}
	pipeline_obj = None

	def __init__(self, pipeline, **kwargs):
		self.pipeline_obj = pipeline
		self.dispatch_args = kwargs

	def debug(self, message):
		self._dispatch(self.pipeline_obj, 'debug', message, **self.dispatch_args)

	def info(self, message):
		self._dispatch(self.pipeline_obj, 'info', message, **self.dispatch_args)

	def warning(self, message):
		self._dispatch(self.pipeline_obj, 'warning', message, **self.dispatch_args)

	def error(self, message):
		self._dispatch(self.pipeline_obj, 'error', message, **self.dispatch_args)

	def exception(self, exception):
		self._dispatch(self.pipeline_obj, 'exception', str(exception), **self.dispatch_args)

	def critical(self, message):
		self._dispatch(self.pipline_obj, 'critical', str(message), **self.dispatch_args)

	def _dispatch(self, *args, **kwargs):
		if self.enable:
			self.dispatch(*args, **kwargs)
		else:
			pass

	def dispatch(self, *args, **kwargs):
		raise NotImplementedError('SPIPipelineLogger cannot be used directly to dispatch log messages.')



#### XMPP Logger
class SPIXMPPLogger(SPIPipelineLogger):


	def dispatch(self, pipeline, severity, message, jid=None):
		try:
			xmpp.send_message(jid, json.dumps({'_pc_message_type':'log_message', 'severity': severity, 'message': message}))
		except:
			pass
		

#### Channel Logger
class SPIChannelLogger(SPIPipelineLogger):

	def dispatch(self, pipeline, severity, message, channel_id=None):
		try:
			channel.send_message(channel_id, json.dumps({'_pc_message_type':'log_message','severity':severity, 'message':message}))
		except:
			pass


#### Serverlogs Logger
class SPIStandardLogger(SPIPipelineLogger):

	def debug(self, message): logging.info(message)
	def info(self, message): logging.info(message)
	def warning(self, message): logging.warning(message)
	def error(self, message): logging.error(message)
	def critical(self, message): logging.critical(message)


#### No Logging
class SPIDummyLogger(SPIPipelineLogger):

	def dispatch(self, *args, **kwargs):
		return None


#### Cache Adapter
class SPIPipelineCacheAdapter(object):

	@classmethod
	def set(cls, key, value, time=3600):
		memcache.set(key, value, time)

	@classmethod
	def get(cls, key):
		return memcache.get(key)
		

class SPIPipeline(pipeline.Pipeline):

		db = db
		_opts = {}
		memcache = memcache
		pipeline = pipeline
		taskqueue = taskqueue
		logger = None
		common = common
		cache = SPIPipelineCacheAdapter

		def __init__(self, *args, **kwargs):

			## Add Pipeline Config
			self.pipeline_config = config.config.get('wirestone.spi.pipelines')

			## Process pipeline options
			if '_opts' in kwargs:
				self._opts = kwargs['_opts']
				if 'logging' in kwargs['_opts']:

					if 'enable' in kwargs['_opts']['logging']:

						if kwargs['_opts']['logging']['enable'] == True:
							if 'mode' in kwargs['_opts']['logging']:

								if kwargs['_opts']['logging']['mode'] == 'xmpp':
									if 'jid' in kwargs['_opts']['logging']:
										self.logger = SPIXMPPLogger(self, jid=kwargs['_opts']['logging']['jid'])

								elif kwargs['_opts']['logging']['mode'] == 'channel':
									if 'channel' in kwargs['_opts']['logging']:
										self.logger = SPIChannelLogger(self, channel_id=kwargs['_opts']['logging']['channel'])

								elif kwargs['_opts']['logging']['mode'] == 'serverlogs':
									self.logger = SPIStandardLogger(self)

						else:
							self.logger = SPIDummyLogger(self)

			## If debugger is still none, it defaults to the dummy or standard if we're in debug mode...
			if self.logger == None:
				if self.pipeline_config['debug'] == True:
					self.logger = SPIStandardLogger(self)
				else:
					self.logger = SPIDummyLogger(self)

			## Pass it up the line...
			super(SPIPipeline, self).__init__(*args, **kwargs)

		@property
		def log(self):
			return self.logger

		@classmethod
		def _coerceToKey(cls, fragment):
			if isinstance(fragment, basestring):
				return db.Key(fragment)
			elif isinstance(fragment, db.Model):
				return model.key()
			elif isinstance(fragment, db.Key):
				return fragment


class TestKeyPipeline(SPIPipeline):

	def run(self):
		return db.Key.from_path('Test', 'test')