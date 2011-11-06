from project.handlers.ext import OutputPackage


class JCrop(OutputPackage):
	
	def north(self):
		return [('style', self.get_style_asset('jcrop'))]
		
	def south(self):
		return [('script', self.get_script_asset('jcrop', 'jquery-plugins'))]