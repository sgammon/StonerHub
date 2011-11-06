from project.handlers.ext import OutputPackage


class DataGrid(OutputPackage):
	
	def north(self):
		return [('style', self.get_style_asset('grid-ci', 'datagrid'),
						  self.get_style_asset('grid-jqui', 'datagrid'))]
		
	def south(self):
		return [('script', self.get_script_asset('datatables', 'jquery-plugins'))]