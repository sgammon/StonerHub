from project.handlers.ext import OutputPackage


class MarkItUp(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<script type='text/javascript' src='/assets/ext/static/markitup/jquery.markitup.js'></script>"]
		html.append("<script type='text/javascript' src='/assets/ext/static/markitup/sets/markdown/set.js'></script>")
		html.append("<link rel='stylesheet' type='text/css' href='/assets/ext/static/markitup/skins/markitup/style.css' />")
		html.append("<link rel='stylesheet' type='text/css' href='/assets/ext/static/markitup/sets/markdown/style.css' />")
		
		return html