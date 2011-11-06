import config
from project.handlers.ext import OutputPackage


class jQuery(OutputPackage):
	
	def north(self):
		return [('script', self.get_script_asset('core', 'jquery')), ('style', self.get_style_asset('smoothness', 'jquery-ui'))]
		
	def south(self):
		return [('script', self.get_script_asset('ui', 'jquery'))]