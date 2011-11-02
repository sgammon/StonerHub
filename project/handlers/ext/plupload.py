from project.handlers.ext import OutputPackage


class Plupload(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link href='/assets/style/static/plupload/jquery.ui.plupload.css' rel='stylesheet' type='text/css' />"]
		html.append("<script type='text/javascript' src='/assets/js/static/plupload/gears_init.js'></script>")
		html.append("<script type='text/javascript' src='/assets/js/static/plupload/plupload.min.js'></script>")
		html.append("<script type='text/javascript' src='/assets/js/static/plupload/plupload.html5.min.js'></script>")
		html.append("<script type='text/javascript' src='/assets/js/static/plupload/plupload.browserplus.min.js'></script>")
		html.append("<script type='text/javascript' src='/assets/js/static/plupload/jquery.ui.plupload.min.js'></script>")
		html.append("<script type='text/javascript' src='/assets/js/static/plupload/util.upload.0.1.js'></script>")
		
		return html