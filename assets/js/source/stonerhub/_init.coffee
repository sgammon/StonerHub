
class StonerHub
	
	constructor: (@config)  ->
		
		@datatables = new DatagridController(@)
		@liveservices = new LiveServicesController(@)
		@newsfeed = new NewsfeedController(@)
		@social = new SocialController(@)
		@upload = new UploadController(@)
		
		@models =

			ContentItem:
				objects: {}
				register: (key, object) ->
					@objects[key] = object
					
				get: (key) ->
					return @objects[key]
		
		return @


window.stonerhub = new StonerHub()
if $?
	$.extend(stonerhub: window.stonerhub)