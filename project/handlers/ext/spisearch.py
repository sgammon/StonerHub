from project.handlers.ext import OutputPackage


class Search(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/spi/search-0.2.css' />"]
		
		return html