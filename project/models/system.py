from google.appengine.ext import db
from project.models import SPIExpandoModel


class _SystemProperty_(SPIExpandoModel):
	
	#key_name = unique properties
	name = db.StringProperty()