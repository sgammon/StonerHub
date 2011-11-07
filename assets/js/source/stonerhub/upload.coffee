

class UploadController extends StonerHubController

	constructor: (stonerhub) ->
		
		@state =
			total_upload_files: 0
		
		@filters = [
			
			## Basic file types
			{title: "Basic Files", extensions: "txt,rtf"},
			{title: "Image Files", extensions: "jpg,jpeg,gif,png,tiff,ico,svg"},

			## Business-related file types
			{title: "Document Files", extensions: "doc,docx,dot,pdf,rtf,txt"},
			{title: "Spreadsheet Files", extensions: "xls,xlsx"},
			{title: "Presentation Files", extensions: "ppt,pptx"},

			## Creative file types
			{title: "Movie Files", extensions: "mpg,mov,avi,wmv"},
			{title: "Drawing Files", extensions: "ai,eps,ps,dxf,ttf,psd"},
			{title: "Sound Files", extensions: "mp3,m4a,wav,flag,ogg"},
			
			## Code file types
			{title: "Web Files", extensions: "html,css,sass,js,coffee,appcache,manifest"},
			{title: "Source Files", extensions: "py,rb,c,cpp,php,java"},

			## Special file types
			{title: "Archive Files", extensions: "zip"},
			
		]
	
		@create_uploader = (@selector, @runtimes, @browse_button, @drag_drop=true, @drop_element=none, @swf='runtime.flash-0.2.swf', @silverlight='runtime.silverlight-0.2.xap') =>
			
			## Convert our asset URLs to be full...
			@swf = '/assets/ext/static/plupload/'+@swf
			@silverlight = '/assets/ext/static/plupload/'+@silverlight
			
			## Create plupload
			create_queue = () =>

				$(@selector).plupload
					runtimes: @runtimes
					browse_button: @browse_button
					preinit: @_bind_uploader_events
					url: '#'
					use_query_string: false
					multipart: true
					drop_element: @drop_element
					flash_swf_url: @swf
					silverlight_xap_url: @silverlight
					dragdrop: @drag_drop
					filters: @filters
			
		@_bind_uploader_events = (uploader) =>
		
			uploader.bind 'UploadFile', @events.upload_file
			uploader.bind 'FileUploaded', @events.file_uploaded
			uploader.bind 'QueueChanged', @events.queue_changed
				
				
		@events =
			
			upload_file: (up, file) =>
				mime_type = @get_mime file.name
				
				if @session_key?
					request = $.apptools.api.upload.generate_upload_url upload_count: up.total.queued, upload_session: @session_key
				else
					request = $.apptools.api.upload.generate_upload_url upload_count: up.total.queued, new_session: true
										
				request.fulfill
				
					success: (response) =>
						up.settings.url = response.upload_url
						up.settings.multipart_params =
							session_key: @session_key						
							blob_content_type: mime_type
					
					failure: (response) =>
						alert 'There was an error generating an upload endpoing. See console.'
						$.apptools.dev.error 'upload', 'Uploader error: ', response
					
				
			file_uploaded: (up, file, raw_api_response) =>
			
				@state.total_upload_files--
				console.log 'FILE UPLOAD RESPONSE', up, file, raw_api_response
			
			queue_changed: (up, files) =>
				
				@state.total_upload_files = up.files.length