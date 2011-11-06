from project.handlers.ext import OutputPackage


class AutoComplete(OutputPackage):
	
	def north(self):
		return [('style', self.get_style_asset('main', 'facelist'))]
		
	def south(self):
		return [('script', self.get_script_asset('autocomplete', 'jquery-interaction'), self.get_script_asset('facelist', 'jquery-plugins'))]
		
	