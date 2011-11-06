from google.appengine.ext import db
from project.core.data.properties import KeyProperty


class UserReferenceProperty(KeyProperty):
	
	_auto_current_user = False
	_auto_current_user_add = False
	
	def __init__(self, auto_current_user=False, auto_current_user_add=False, **kwargs):
		
		if auto_current_user is not False:
			self._auto_current_user = True
		elif auto_current_user_add is not False:
			self._auto_current_user_add = True
			
		super(UserReferenceProperty, self).__init__(**kwargs)

	def default_value(self):
		from project.core import security
		
		## Since this is only executed on 'default' (when the property is left empty), we add the user if either flag is true...
		if self._auto_current_user or self._auto_current_user_add:
			if security.get_current_user() is not None:
				return security.get_current_user().key()
		return None
		
	def validate(self, value):
		from project.core import security

		if self._auto_current_user:
			if security.get_current_user() is not None:
				return security.get_current_user().key()
		return value