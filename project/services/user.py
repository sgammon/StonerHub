from project.services import remote
from project.services import messages
from project.services import RemoteService

from project.messages import user as messages


class UserService(RemoteService):
	
	@remote.method(messages.StatsRequest, messages.StatsResponse)
	def stats(self, request):
		pass
		
	@remote.method(messages.ProfilePicRequest, messages.ProfilePicResponse)
	def profile_pic(self, request):
		pass
		
	@remote.method(messages.ActionsRequest, messages.ActionsResponse)
	def actions(self, request):
		pass
		
	@remote.method(messages.NotificationsRequest, messages.NotificationsResponse)
	def notifications(self, request):
		pass
		
	@remote.method(messages.EditProfileRequest, messages.EditProfileResponse)
	def edit_profile(self, request):
		pass
		
	@remote.method(messages.StarredItemsRequest, messages.StarredItemsResponse)
	def starred_items(self, request):
		pass