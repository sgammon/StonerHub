from project.handlers.ext import OutputPackage


class Fancybox(OutputPackage):
	
	def north(self):
		return [('style', self.get_style_asset('fancybox'))]
		
	def south(self):
		return [('script', self.get_script_asset('fancybox', 'jquery-plugins'))]