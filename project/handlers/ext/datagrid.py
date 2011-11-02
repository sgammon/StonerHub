from project.handlers.ext import OutputPackage


class DataGrid(OutputPackage):
	
	@classmethod
	def north(cls):
		html = []
		html.append("<link rel='stylesheet' href='/assets/style/static/datagrid/grid-ci-1.0.css' type='text/css' media='screen' />")
		html.append("<link rel='stylesheet' href='/assets/style/static/datagrid/grid-table-jui-1.0.css' type='text/css' media='screen' />")		
		
		return html
		
	@classmethod
	def south(cls):
		html = ["<script type='text/javascript' src='/assets/js/static/datagrid/jquery.dataTables.min.js'></script>"]
		html.append("<script type='text/javascript' src='/assets/js/static/datagrid/util.datagrid.0.2.js'></script>")
		return html