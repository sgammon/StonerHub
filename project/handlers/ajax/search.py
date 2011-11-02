import logging
import datetime
import simplejson as json

from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.blobstore import BlobKey
from google.appengine.ext.blobstore import BlobInfo

from project.handlers.ajax import SPIAjaxHandler
from project.models.content_item import ContentItem


class ContentSearch(SPIAjaxHandler):
	
	''' Search for content and return matching items. '''
	
	def get(self):
		
		self.render('content-search')