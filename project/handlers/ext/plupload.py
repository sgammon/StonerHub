from project.handlers.ext import OutputPackage


class Plupload(OutputPackage):
	
	def north(self):		
		return [('style', self.get_style_asset('jqui-widget', 'plupload'))]
		
	def south(self):
		return [('script', self.get_script_asset('core', 'plupload'),
						   self.get_script_asset('jqui_widget', 'plupload'),
						   self.get_script_asset('runtime.html4', 'plupload'),
						   self.get_script_asset('runtime.gears', 'plupload'),
						   self.get_script_asset('runtime.flash', 'plupload'),
						   self.get_script_asset('runtime.html5', 'plupload'),
						   self.get_script_asset('runtime.silverlight', 'plupload'))]
		