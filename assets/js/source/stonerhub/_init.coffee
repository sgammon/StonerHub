
class StonerHub
	
	constructor: (@config)  ->
		
		@datatables = new DatatablesController(@)
		@liveservices = new LiveServicesController(@)
		@newsfeed = new NewsFeedController(@)
		@social = new SocialController(@)
		@upload = new UploadController(@)
		
		return @


window.stonerhub = new StonerHub()
if $?
	$.extend(stonerhub: window.stonerhub)