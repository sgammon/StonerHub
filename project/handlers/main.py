import string
import logging
from project.handlers import WebHandler

from project.models.search import Tag
from project.models.content import Repository
from project.models.content_item import ContentItem


class Landing(WebHandler):
	
	''' Main site landing! :) '''
	
	def get(self):

		## Since this is the root handler, serve the Yadis OpenID descriptor if something is looking for it
		if str(self.request.headers.get('http-accept')).find('application/xrds+xml') != -1:
			logging.info('Remote host '+str(self.request.remote_addr)+' requested Yadis/XRDS OpenID descriptor. Serving.')
			self.render('util/openid-discovery.xml', server_name=self.request.host)
		
		grid = ContentItem.generateGrid()

		grid.set_service('ContentItem')
		grid.set_method('list')
		
		context = {'grid': grid}
		
		self.render('main/landing.html', dependencies=['Plupload'], **context)
		

class Newsfeed(WebHandler):
	
	''' User's main newsfeed page. '''
	
	def get(self):
		
		context = {}
		
		## Display page with AJAX call for newsfeed pull
		self.render('main/newsfeed.html', dependencies=['SPINewsfeed'], **context)
		

class Offline(WebHandler):
	
	''' Page that is displayed when the user is offline. This is automatically consumed via the appcache manifest. '''
	
	def get(self):
		self.render('main/offline.html')

		
class ShortURL(WebHandler):
	
	''' Handles shortURLs to keys in the application. '''
	
	def get(self):
		
		key_types = {
			
			'r': ('repository-view', Repository),
			'c': ('content-item-view', ContentItem),
			't': ('tag-view', Tag)
			
		}
		
		for key, value in key_types.items():
			endpoint, kind = value
			if key in self.request:
				obj = kind.get(self.request.get(key))
				if obj is not None:
					if key == 'r':
						self.redirect(self.url_for(endpoint, repo=str(obj.key())))
					elif key == 'c':
						self.redirect(self.url_for(endpoint, repo=str(obj.repository.key()), key=str(obj.key())))
					elif key == 't':
						self.redirect(self.url_for(enpodint, tag=str(obj.key().name())))
						
		self.redirect(self.url_for('landing'))