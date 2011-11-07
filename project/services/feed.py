from project.services import remote
from project.services import messages
from project.services import RemoteService

from project.messages import feed as messages


class FeedService(RemoteService):
	
	@remote.method(messages.FeedRequest, messages.FeedResponse)
	def feed(self, request):
		pass
		
	@remote.method(messages.SubscribeRequest, messages.SubscribeResponse)
	def subscribe(self, request):
		pass
		
	@remote.method(messages.UnsubscribeRequest, messages.UnsubscribeResponse)
	def unsubscribe(self, request):
		pass