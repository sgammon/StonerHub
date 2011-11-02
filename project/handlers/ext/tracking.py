import config
from project.handlers.ext import OutputPackage


class GoogleAnalytics(OutputPackage):
	
	@classmethod
	def north(cls):
		
		gv_tracking = config.config.get('wirestone.spi.tracking')['google_analytics_account']
		
		html = ('''
<script type="text/javascript">
var _gaq = _gaq || [];_gaq.push(['_setAccount', '%s']);_gaq.push(['_trackPageview']);
(function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);})();
</script>
		''' % str(gv_tracking))
		
		return [html]