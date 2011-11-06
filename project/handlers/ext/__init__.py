import webapp2
from apptools.api.assets import AssetsMixin


class OutputPackage(AssetsMixin):
	
	''' Dependency package that groups together assets. '''
	
	request = None
	
	def __init__(self, request=None):
		self.request = request
	
	def get_sections(self):
		return self._get_section('north'), self._get_section('south')
	
	def _get_section(self, section):
		elements = []
		if section == 'north':
			data = self.north()
		elif section == 'south':
			data = self.south()
		
		for typesection in data:
			if typesection[0] == 'style':
				wrapper = lambda x: '<link rel="stylesheet" href="%s">' % str(x)
			elif typesection[0] == 'script':
				wrapper = lambda x: '<script type="text/javascript" src="%s"></script>' % str(x)				
			elif typesection[0] == 'raw':
				wrapper = lambda x: x
			
			for element in typesection[1:]:
				elements.append(wrapper(element))
		
		return elements
	
	def north(self):
		
		''' Get assets that should go into __north.html. '''
		
		return []
		
	def south(self):
		
		''' Get assets that should go into __south.html. '''
		
		return []