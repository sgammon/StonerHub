import os
import string
import random
import datetime

from webapp2 import Router
url_for = Router.build

from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.ext.db import polymodel

from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import SPIExpandoModel
from project.models import CreatedModifiedMixin

from project.models.org import OfficeLocation
from project.models.ticket import UserTicket
from project.core.data.properties.security import UserReferenceProperty

SALT_CHARS = string.ascii_letters + string.digits


def generateSessionID(length=25):
	return ''.join(random.choice(SALT_CHARS) for i in xrange(length))


class User(SPIModel, CreatedModifiedMixin):
	
	''' Model for a Wirestone user. '''
		
	#### ==== Naming & Contact Properties
	firstname = db.StringProperty()
	lastname = db.StringProperty()
	username = db.StringProperty()
	password = db.StringProperty()
	email = db.StringProperty(default=None)
	jabber = db.IMProperty()
	phone = db.PhoneNumberProperty(default=None)
	title = db.StringProperty()
	avatar_url = db.StringProperty(default=None)
	office = db.ReferenceProperty(OfficeLocation, collection_name='users')
	
	#### ==== Session Properties
	session_id = db.StringProperty(default=None)
		
	#### ==== Basic Application Permissions
	# Admin Status
	perm_sys_admin = db.BooleanProperty(default=False)
	perm_dev_admin = db.BooleanProperty(default=False)
	
	# Repo Permission Flags
	perm_repo_create = db.BooleanProperty(default=None)
	perm_repo_edit = db.BooleanProperty(default=None)
	perm_repo_delete = db.BooleanProperty(default=None)
	
	# Content Item Permission Flags
	perm_content_item_create = db.BooleanProperty(default=None)
	perm_content_item_edit = db.BooleanProperty(default=None)
	perm_content_item_delete = db.BooleanProperty(default=None)
	
	# Tag Permissions
	perm_tag_create = db.BooleanProperty(default=None)
	
	def profilePicHref(self,append=''):
		if self.avatar_url is not None:
			return self.avatar_url+append
		return url_for('media-serve-profile-pic', username=self.key().name(), format='jpeg')+append
		
	def is_current_user_admin(self):
		return self.perm_sys_admin
		
	def nickname(self):
		return self.key().name()
		
		
class AuthSession(UserTicket):
	
	username = db.StringProperty()
	ip_addr = db.StringProperty()
	auth_phase = db.IntegerProperty(choices=[0, 1, 2])
	user = db.ReferenceProperty(User, collection_name='auth_tickets', default=None)	
	
	@classmethod
	def provisionTicket(cls, phase_override=1):
		session_id = generateSessionID()
		return cls(key_name=session_id, auth_phase=phase_override, status='pending', ip_addr=os.environ['REMOTE_ADDR']).put()

	@classmethod
	def get_from_cache(cls, key):
		if isinstance(key, db.Key):
			key = key.name()
		key = 'auth_session::'+str(key)
		return memcache.get(key)
		
	@classmethod
	def evict_from_cache_by_key(cls, key):
		if isinstance(key, db.Key):
			key = key.name()
		key = 'AuthSession-'+str(key)
		return memcache.delete('SPISecurity//'+key)
		
	def add_to_cache(self):		
		key = 'AuthSession-'+str(self.key().name())
		return memcache.set('SPISecurity//'+key, self, time=3600)

	def evict_from_cache(self):
		key = 'AuthSession-'+str(self.key().name())
		return memcache.delete(key)
		
		
class AccountClaim(UserTicket):
	
	''' Describes a ticket to create an in-house authentication account. '''
	
	used = db.BooleanProperty(default=False)
	used_at = db.DateTimeProperty(auto_now=True)
	visited = db.BooleanProperty(default=False)
	allocated_at = db.DateTimeProperty(auto_now_add=True)
	allocated_by = UserReferenceProperty(auto_current_user_add=True)
	username = db.StringProperty()

	
class SecurityRole(SPIModel):
	
	''' Model for a user role, like 'Admin' or 'Content Manager'. '''

	# Basic Details
	name = db.StringProperty()
	description = db.TextProperty()
		
	
class SecurityGroup(SPIModel):
	
	''' Group for a user, like 'Developers'. '''
	
	name = db.StringProperty()
	description = db.TextProperty()
	users = db.ListProperty(db.Key)


class PermissionsDescriptor(SPIPolyModel, CreatedModifiedMixin):
	
	''' Abstract ancestor model for a permissions descriptor. '''
	
	## parent = item permissions are for
	allow = db.BooleanProperty(default=True)
	
	
class RolePerms(PermissionsDescriptor):
	
	''' Maps permissions to a set of roles. '''
	value = db.ListProperty(db.Key)


class GroupPerms(PermissionsDescriptor):
	
	''' Maps permissions to a set of groups. '''
	value = db.ListProperty(db.Key)
	
	
class ACLPerms(PermissionsDescriptor):
	
	''' Maps permissions to a set of users. '''
	value = db.ListProperty(db.Key)
	
	
class CompiledPermissions(SPIModel):
	
	''' Caches a compiled list of entities able to access a content item or repository. '''
	
	## parent = item permissions are compiled for
	## keyname = 'compiled_permissions'
	
	allowed_keys = db.ListProperty(db.Key)
	disallowed_keys = db.ListProperty(db.Key)