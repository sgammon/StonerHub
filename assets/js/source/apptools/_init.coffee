
class AppTools
	
	constructor: (@config)  ->
		
		## Dev Tools
		@dev = new CoreDevAPI(@)
		
		## Agent API
		@agent = new CoreAgentAPI(@)
		@agent.discover()
		
		## Events API
		@events = new CoreEventsAPI(@)
		
		## Users API
		@user = new CoreUserAPI(@)
		
		## RPC API
		@api = new CoreRPCAPI(@)
		
		## Live API
		@push = new CorePushAPI(@)
		
		return @


window.apptools = new AppTools()
if $?
	$.extend(apptools: window.apptools)