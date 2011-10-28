import config
import datetime

from webapp2 import cached_property

from google.appengine.ext import db
from google.appengine.ext import blobstore

from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import UserAuditMixin
from project.models import CreatedModifiedMixin


def getExpirationDateTime(lifetime_opt=False):

	ticketConfig = config.config.get('wirestone.spi.datamodel.ticket')
	if lifetime_opt is not False:
		if isinstance(lifetime_opt, (datetime.datetime, datetime.timedelta)):

			if isinstance(lifetime_opt, datetime.timedelta):
				result = datetime.datetime.now()+lifetime_opt

			elif isinstance(lifetime_opt, datetime.datetime):
				result = lifetime_opt
	else:
		result = datetime.datetime.now()+ticketConfig['default_lifetime']
		
	return result
	

class Ticket(SPIPolyModel):

	status = db.StringProperty(choices=['failure','completed','queued','processing','active','inactive','expired','pending','building'])
	expires = db.DateTimeProperty(default=getExpirationDateTime())
	
	def setLifetime(self, lifetime_opt=False):
		self.expires = getExpirationDateTime(lifetime_opt)
	
	@cached_property
	def ticketConfig(self):
		return config.config.get('wirestone.spi.datamodel.ticket')
	
	
class SystemTicket(Ticket):
	pass
	
	
class UserTicket(Ticket, UserAuditMixin):
	pass
	
	
class UploadSessionTicket(UserTicket):
	
	progress = db.StringProperty(choices=['upload','meta','tagging'])
	
	blob_count = db.IntegerProperty(default=0)
	queued = db.StringListProperty(indexed=False, default=None)	
	finished = db.StringListProperty(indexed=False, default=None)
	
	
class UserRegistrationTicket(UserTicket):
	
	user = db.UserProperty()
	progress = db.StringProperty(choices=['info','avatar'])
	continue_url = db.StringProperty(default='/')