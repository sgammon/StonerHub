import logging
import mimetypes

from google.appengine.runtime import apiproxy_errors

from google.appengine.api import datastore
from google.appengine.api import datastore_types

from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.blobstore import BlobKey
from google.appengine.ext.blobstore import BlobInfo

from project.models.ticket import UploadSessionTicket

from project.handlers.ajax import SPIAjaxHandler


class GenerateUploadURL(SPIAjaxHandler):
	
	''' Generate a blobstore upload URL and return as JSON response... used with Plupload. '''
	
	def get(self):
		
		try:
		
			## Pull URL Parameters
			new_session = self.request.get('createNewUploadSession', False)
			upload_count = self.request.get('uploadCount', False)
			upload_session = self.request.get('uploadSession', False)
		
			if new_session == 'true' or 'upload_session' != False:
			
				if new_session == 'true':
					self.response_params['upload_session_key'] = str(UploadSessionTicket(blob_count=int(upload_count) or 1, progress='upload', status='processing').put())
				
				else:
					self.response_params['upload_session_key'] = upload_session

				## Generate URL with AJAX success callback as success URL, include session key
				self.response_params['upload_url'] = blobstore.create_upload_url(self.url_for('ajax-upload-success-with-session', sessionkey=self.response_params['upload_session_key']))
			
			else:
			
				## Generate URL with AJAX success callback as success URL
				self.response_params['upload_url'] = blobstore.create_upload_url(self.url_for('ajax-upload-success'))
		
		## Catch 'billing must be enabled' error.
		except apiproxy_errors.FeatureNotEnabledError, e:
			logging.error('Attempt to create Blobstore upload URL resulted in a FeatureNotEnabledError. Check that billing is enabled in the AppEngine administration console.')
			return self.fail('generate_ajax_upload_url', 'Blobstore storage not enabled.')
			
		except Exception, e:
			logging.error('Exception encountered while retrieving a blobstore upload URL.')
			return self.fail('generate_ajax_upload_url', 'Unknown exception encountered.')
		
			
		## Render JSON Response
		return self.render('generate_ajax_upload_url')
		
		
