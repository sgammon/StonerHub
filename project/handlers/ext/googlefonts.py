import config
from project.handlers.ext import OutputPackage


class GoogleFonts(OutputPackage):
	
	@classmethod
	def north(cls):
		
		gv_tracking = config.config.get('wirestone.spi.tracking')['google_analytics_account']
		
		html = ["<link href='http://fonts.googleapis.com/css?family=Cabin:regular,500,600,bold' rel='stylesheet' type='text/css'>"]
		html.append("<link href='/assets/style/static/spi/font-0.1.css' rel='stylesheet' type='text/css'>")
		
		return html