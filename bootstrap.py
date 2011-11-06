import sys

if 'lib' not in sys.path:
	# Add lib as primary libraries directory, with fallback to lib/dist
	# and optionally to lib/dist.zip, loaded using zipimport.
	sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']
	

class AppBootstrapper(object):

	@classmethod
	def prepareImports(cls):
		if 'lib' not in sys.path or sys.path[0] != 'lib':
			sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']
		return cls