from wtforms import fields, validators

from google.appengine.api import memcache

from project.core.forms import SPIForm
from project.models.org import OfficeLocation


def get_office_locations():
	m = memcache.get('SPIRuntime//OfficeLocations')
	if m is None:
		o = OfficeLocation.all(keys_only=True)
		locations = o.fetch(o.count())
		m = [('__NULL__', '-- Office Locations --')]
		for location in locations:
			m.append((str(location), location.name()))
		if len(m) > 4:
			memcache.set('SPIRuntime//OfficeLocations', m)
	return m
	

class RegistrationForm(SPIForm):
	
	firstname = fields.TextField('First Name', [validators.Required('Please enter your first name.')])
	lastname = fields.TextField('Last Name', [validators.Required('Please enter your last name.')])
	title = fields.TextField('Title')
	office = fields.SelectField('Location',choices=get_office_locations())
	
	
class ProfileCreateForm(SPIForm):
	
	phone = fields.TextField('Phone Number', [validators.Required('Please enter a phone number.')])
	email = fields.TextField('Email Address', [validators.Required('Please enter an email address.'), validators.Email('Please enter a valid email address.')])
	
	
class LogonForm(SPIForm):
	
	username = fields.TextField()
	password = fields.PasswordField()
	action = fields.HiddenField(default='spi-logon')
	
	
class TokenClaimForm(SPIForm):

	password_1 = fields.PasswordField(label='Password')
	password_2 = fields.PasswordField(label='Password (Again)')
	action = fields.HiddenField(default='spi-claim-token')