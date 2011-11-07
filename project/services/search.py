from project.services import remote
from project.services import messages
from project.services import RemoteService

from project.messages import search as messages


class SearchService(RemoteService):
	
	@remote.method(messages.QuicksearchRequest, messages.QuicksearchResponse)
	def quicksearch(self, request):
		pass
		
	@remote.method(messages.FullsearchRequest, messages.FullsearchResponse)
	def fullsearch(self, request):
		pass
		
	@remote.method(messages.AutocompleteRequest, messages.AutocompleteResponse)
	def autocomplete(self, request):
		pass