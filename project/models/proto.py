from google.appengine.ext import db

from project.models import SPIModel
from project.models import SPIPolyModel


class Prototype(SPIModel):

	kind_name = db.StringProperty()
	description = db.TextProperty()

	path = db.StringListProperty()
	classpath = db.StringListProperty()
	
	property_names = db.StringListProperty()
	property_types = db.StringListProperty()
	
	
class Property(SPIPolyModel):
	
	name = db.StringProperty()
	type = db.StringProperty()