from google.appengine.api import channel
from project.handlers.ext import OutputPackage


class Main(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/spi/main-0.3.css' />"] ## <--- V1 Design
		#html = ["<link rel='stylesheet' media='screen' href='/assets/style/spi/v2/wirestone.css"] ## <--- V2 Design
		#html.append("<script src='/assets/js/spi/v2/wirestone.jquery.js")
		return html
		
		
class Forms(OutputPackage):

	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/spi/forms-0.2.css' />"]
		return html

	@classmethod
	def south(cls):
		return []
		
		
class Social(OutputPackage):

	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/spi/social-0.3.css' />"]
		#html = []
		return html
		
	@classmethod
	def south(cls):
		#return []
		return ["<script src='/assets/js/static/spi/social-0.2.js'></script>"]
		
		
class Newsfeed(OutputPackage):
	
	@classmethod
	def north(cls):
		html = ["<link rel='stylesheet' media='screen' href='/assets/style/static/spi/newsfeed-0.1.css' />"]
		return html
		
	@classmethod
	def south(cls):
		html = ["<script src='/assets/js/static/spi/newsfeed-0.1.js'></script>"]
		return html