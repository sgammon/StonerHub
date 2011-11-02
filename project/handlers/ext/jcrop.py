from project.handlers.ext import OutputPackage


class JCrop(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/jcrop/jquery.Jcrop-0.1.css' />"]
		html.append("<script type='text/javascript' src='/assets/js/static/jcrop/jquery.Jcrop.min.js'></script>")
		
		return html