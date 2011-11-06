from project.handlers.ext import OutputPackage


class GoogleFonts(OutputPackage):
	
	def north(self):
		return [('raw', "<link href='http://fonts.googleapis.com/css?family=Cabin:regular,500,600,bold' rel='stylesheet' type='text/css'>")]