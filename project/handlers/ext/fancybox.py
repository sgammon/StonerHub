from project.handlers.ext import OutputPackage


class Fancybox(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/fancybox/jquery.fancybox-1.3.4.css' />"]
		return html
		
	@classmethod
	def south(cls):
		html = ["<script type='text/javascript' src='/assets/js/static/jquery/jquery.fancybox-1.3.4.pack.js'></script>"]
		return html