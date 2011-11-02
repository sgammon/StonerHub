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
		
		
class UploadCallback(SPIAjaxHandler, BlobstoreUploadMixin):
	
	''' Callback URL used by the blobstore on upload success. Renders a JSON response describing the newly created blob. '''
	
	def get(self, sessionkey=None, blobkey=None):

		if blobkey is not None:
			blob_obj = BlobInfo.get(BlobKey(blobkey))

			## Generate blob object
			blob_obj_response = {
				'key':str(blob_obj.key()),
				'content_type':blob_obj.content_type,
				'creation':str(blob_obj.creation),
				'filename':blob_obj.filename,
				'size': blob_obj.size
			}
		
			## Render JSON Response
			return self.render('upload_callback', blob=blob_obj_response)
			
		else:
			return self.fail('upload_callback', 'BlobKey must be provided with a GET request to this endpoint.')
	

	def post(self, sessionkey=None, blobkey=None):
		
		## Pull 'file' variable with uploaded files
		upload_files = self.get_uploads('file')
		blob_info = upload_files[0]
				
		if sessionkey is not None and sessionkey != 'False' and sessionkey is not False:
			## Decode session key
			upload_session = db.get(db.Key(sessionkey))
			upload_session.queued.append(str(blob_info.key()))
			upload_session_key = upload_session.put()
		
			## Create redirect response object with blobkey and session key
			response = self.redirect_to('ajax-upload-success-passthrough-with-session', sessionkey=str(upload_session_key), blobkey=str(blob_info.key()))
		
		else:
			
			## Create redirect response object with blobkey (no session)
			response = self.redirect_to('ajax-upload-success-passthrough', blobkey=str(blob_info.key()))

		## Clear request body
		response.data = ''
		
		return response