from google.appengine.ext import db

from project.models import SPIModel
from project.models import SPIPolyModel


class OfficeLocation(SPIModel):
	
	address = db.PostalAddressProperty()
	phone = db.PhoneNumberProperty()