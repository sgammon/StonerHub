from google.appengine.api import channel
from project.handlers.ext import OutputPackage


class Main(OutputPackage):
	
	def north(self):
		return [('style', self.get_style_asset('main', 'stonerhub'))]
				
		
class Newsfeed(OutputPackage):
	
	def north(self):
		return [('style', self.get_style_asset('newsfeed', 'stonerhub'))]
		
	def south(self):
		return [('script', self.get_script_asset('newsfeed', 'stonerhub'))]