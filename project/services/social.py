from project.services import remote
from project.services import messages
from project.services import message_types
from project.services import RemoteService

from project.messages import social as messages


class SocialService(RemoteService):
	
	@remote.method(messages.LikeRequest, message_types.VoidMessage)
	def like(self, request):
		pass
		
	@remote.method(messages.CommentRequest, messages.CommentResponse)
	def comment(self, request):
		pass
		
	@remote.method(messages.ShareRequest, messages.ShareResponse)
	def share(self, request):
		pass
		
	@remote.method(messages.SuggestTagRequest, message_types.VoidMessage)
	def suggest_tag(self, request):
		pass
		
	@remote.method(messages.GetSocialActionsRequest, messages.GetLikesResponse)
	def get_likes(self, request):
		pass
		
	@remote.method(messages.GetSocialActionsRequest, messages.GetLikesResponse)
	def get_comments(self, request):
		pass
		
	@remote.method(messages.StarItemRequest, message_types.VoidMessage)
	def star(self, request):
		pass