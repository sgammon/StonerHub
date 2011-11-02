import config
from project.handlers.ext import OutputPackage


class jQuery(OutputPackage):
	
	@classmethod
	def north(cls):
		
		jq_href = '/assets/js/static/jquery/jquery.full.1.5.js'
		jq_cfg = config.config.get('wirestone.spi.output.jquery')
		if jq_cfg['source'] == 'web':
			if jq_cfg['mode'] == 'development':
				jq_href = 'https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.js'
			elif jq_cfg['mode'] == 'production':
				jq_href = 'https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js'
		elif jq_cfg['source'] == 'local':
			if jq_cfg['mode'] == 'development':
				jq_href = '/assets/js/static/jquery/jquery.full.1.5.js'
			elif jq_cfg['mode'] == 'production':
				jq_href = '/assets/js/static/jquery/jquery.min.1.5.js'
		
		html = ["<script type='text/javascript' src='"+jq_href+"'></script>"]
		html.append("<script type='text/javascript' src='/assets/js/static/jquery/jquery.rpc.2.0.js'></script>")
		
		jqui_href = '/assets/js/jquery/jquery.full.1.5.js'
		if jq_cfg['ui']['enable'] is True:
			
			if jq_cfg['ui']['source'] == 'web':
				if jq_cfg['ui']['mode'] == 'development':
					jqui_href = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.js'
				elif jq_cfg['ui']['mode'] == 'production':
					jqui_href = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js'
			elif jq_cfg['ui']['source'] == 'local':
				if jq_cfg['ui']['mode'] == 'development':
					jqui_href = '/assets/js/static/jquery/ui/jquery-ui-1.8.9.spi.full.js'
				elif jq_cfg['ui']['mode'] == 'production':
					jqui_href = '/assets/js/static/jquery/ui/jquery-ui-1.8.9.spi.min.js'
		
		
			html.append("<script type='text/javascript' src='"+jqui_href+"'></script>")
			html.append("<link rel='stylesheet' media='screen' href='/assets/style/static/themes/"+jq_cfg['ui']['theme']+"/jquery-ui-1.8.9.css' />")
		
		return html
		
		
class jQueryMobile(OutputPackage):

	@classmethod
	def north(cls):

		jq_href = '/assets/js/static/jquery/jquery.min.1.5.js'

		jq_cfg = config.config.get('wirestone.spi.output.jquery')	
		
		if jq_config['mobile']['enable'] == True:

			if jq_config['mobile']['mode'] == 'development':
				html = ["<link rel='stylesheet' href='http://code.jquery.com/mobile/1.0a3/jquery.mobile-1.0a3.min.css' />"]
				html.append("<script src='http://code.jquery.com/mobile/1.0a3/jquery.mobile-1.0a3.min.js'></script>")

			if jq_config['mobile']['mode'] == 'production':
				html = ["<link rel='stylesheet' href='http://code.jquery.com/mobile/1.0a3/jquery.mobile-1.0a3.css' />"]
				html.append("<script src='http://code.jquery.com/mobile/1.0a3/jquery.mobile-1.0a3.js'></script>")
				

		return html