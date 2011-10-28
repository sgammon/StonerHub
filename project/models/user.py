from google.appengine.ext import db
from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import CreatedModifiedMixin

from project.models.security import User as WirestoneUser


class UserPrefGroup(SPIPolyModel):
	
	name = db.StringProperty()
	user = db.ReferenceProperty(WirestoneUser, collection_name='settings')
	
	
class NotificationPrefs(UserPrefGroup):
	
	notify_comment = db.BooleanProperty(default=True)
	notify_comment_method = db.StringProperty(choices=['email','xmpp'])
	
	notify_like = db.BooleanProperty(default=True)
	notify_like_method = db.StringProperty(choices=['email','xmpp'])
	
	notify_sibling = db.BooleanProperty(default=True)
	notify_sibling_method = db.StringProperty(choices=['email','xmpp'])
	
	
class SocialNetworkAccount(SPIModel, CreatedModifiedMixin):
	
	ext_id = db.StringProperty()
	profile = db.StringProperty()
	user = db.ReferenceProperty(WirestoneUser, collection_name='social_accounts')
	network = db.StringProperty(choices=['facebook', 'twitter', 'google+', 'linkedin', 'flickr', 'reddit', 'vimeo', 'youtube', 'delicious', 'digg', 'dopplr', 'blog', 'tumblr'])