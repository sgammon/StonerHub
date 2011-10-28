from google.appengine.ext import db

from project.models import SPIModel

from project.models import UserAuditMixin
from project.models import CreatedModifiedMixin


class Bug(SPIModel, UserAuditMixin, CreatedModifiedMixin):

	title = db.StringProperty()
	description = db.TextProperty()
	
	
class PipelineResult(SPIModel, CreatedModifiedMixin):

	pipeline = db.StringProperty()
	path = db.StringProperty()
	success = db.BooleanProperty()