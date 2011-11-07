from webapp2 import uri_for as url_for

from project.services import remote
from project.services import RemoteService
from project.messages import upload as messages

from project.models.ticket import UploadSessionTicket


class UploadService(RemoteService):
	
	@remote.method(messages.UploadURLRequest, messages.UploadURLResponse)
	def generate_upload_url(self, request):
		
		response = messages.UploadURLResponse()
		
		if request.new_session == True or request.upload_session != None:
			if request.new_session == True:
				response.session_key = str(UploadSessionTicket(blob_count=int(request.upload_count) or 1, progress='upload', status='processing').put())
			else:
				response.session_key = request.upload_session
			
			response.upload_url = self.api.blobstore.create_upload_url(url_for('ajax-upload-success-with-session', sessionkey=response.session_key))
			
		else:
			response.upload_url = self.api.blobstore.create_upload_url(url_for('ajax-upload-success'))
		
		return response