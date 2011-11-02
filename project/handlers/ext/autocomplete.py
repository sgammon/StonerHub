from project.handlers.ext import OutputPackage


class AutoComplete(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' type='text/css' href='/assets/style/static/autocomplete/facelist-0.3.css' />"]
		html.append("<script type='text/javascript' src='/assets/js/static/autocomplete/jquery.autocomplete.js'></script>")
		html.append("<script type='text/javascript' src='/assets/js/static/autocomplete/jquery.facelist.js'></script>")		
		return html