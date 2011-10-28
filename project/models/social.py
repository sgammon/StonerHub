import os
import logging
from google.appengine.ext import db

from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import UserAuditMixin
from project.models import CreatedModifiedMixin

from project.models.security import User

from project.models.content import QueuedBlob
from project.models.content_item import ContentItem

from project.pipelines.util import EmailMessage
from project.pipelines.util import XMPPMessage


#################### ==== SOCIAL ACCOUNTS (FOR Users) ==== ####################
class SocialAccount(SPIPolyModel, UserAuditMixin, CreatedModifiedMixin):
	
	''' An external social media account held by a user. '''
	
	user = db.ReferenceProperty(User, collection_name='social_accounts')
	enabled = db.BooleanProperty(default=False)
	publish_rights = db.BooleanProperty(default=False)
	
	
class TwitterAccount(SocialAccount):
	
	''' A twitter account. '''
	
	pass
	
	
class FacebookAccount(SocialAccount):
	
	''' A facebook account. '''
	
	pass
	
	
class FriendFeedAccount(SocialAccount):
	
	''' A FriendFeed account. '''
	
	pass


#################### ==== SOCIAL ACTIONS (FOR ContentItems) ==== ####################
class SocialAction(SPIPolyModel, CreatedModifiedMixin):
	
	''' A social action on a content item. '''
	
	## Parent = content item
	user = db.ReferenceProperty(User, collection_name='social_actions')
	content_item = db.ReferenceProperty(ContentItem, collection_name='social_actions')
	

class Comment(SocialAction):

	''' A comment on a content item. '''

	text = db.TextProperty()
	
	
class Share(SocialAction):

	''' A comment on a content item. '''

	target_user = db.ReferenceProperty(User, collection_name='social_shares')
	
	
class InternalShare(Share):
	
	''' An action sharing an item with one or many users internal to the UCR system. '''
	
	sys_users = db.ListProperty(db.Key)
	
	
class ExternalShare(Share):
	
	''' An action sharing an item with one or many external recipients (not stored in the UCR system). '''
	
	pass
	
	
class EmailShare(ExternalShare):
	
	''' An action sharing an item with external recipients via email. '''
	
	recipients = db.StringListProperty()
	
	
class SocialShare(ExternalShare):
	
	''' An action sharing an item with an external social media connection. '''
	
	targets = db.ListProperty(db.Key)
	messages = db.ListProperty(db.Key)
	

class Rating(SocialAction):
	
	''' A rating for a content item. '''
	
	rating = db.RatingProperty()


class Like(SocialAction):
	
	''' A 'like' of a content item. '''
	pass


class Views(SocialAction):
	
	''' Count of document views for a period of time. '''
	views = db.IntegerProperty()


class CompiledSocialActions(SPIModel):
	
	''' Caches a compiled list of likes, comments, ratings, and views. '''
	
	## parent = item permissions are compiled for
	## keyname = 'compiled_social_actions'
	
	likes = db.ListProperty(db.Key, indexed=False)
	like_count = db.IntegerProperty(indexed=True)
	like_users = db.ListProperty(db.Key, indexed=False)
	
	comments = db.ListProperty(basestring, indexed=False)
	comment_count = db.IntegerProperty(indexed=True)	
	comment_users = db.ListProperty(db.Key, indexed=False)
	
	views = db.IntegerProperty(indexed=False)
	rating = db.RatingProperty(indexed=True)
	
	
class SocialNotification(SPIPolyModel, CreatedModifiedMixin):

	user = db.ReferenceProperty(User, collection_name='notifications')
	action = db.ReferenceProperty(SocialAction, collection_name='notifications')
	is_read = db.BooleanProperty(default=False)
	
	
class StopNotifications(SPIPolyModel, CreatedModifiedMixin):
	
	user = db.ReferenceProperty(User, collection_name='stop_notifications')
	content_item = db.ReferenceProperty(ContentItem, collection_name='stop_notifications')
	
	
class CINotification(SocialNotification):
	
	relation = db.StringProperty(choices=['creator','editor','sibling'])
	content_item = db.ReferenceProperty(ContentItem, collection_name='notifications')
	
	def generateEmailTo(self):
		
		if self.user.email is None:
			email = self.user.username+'@wirestone.com'
		else:
			if isinstance(self.user.email, list):
				email = self.user.email[0] ## Prep for multiple email address support...
			else:
				email = self.user.email
			
		return self.user.firstname+' '+self.user.lastname+' <'+email+'>'
		
	def generateConfig(self, c_type, **kwargs):
		if c_type.lower() == 'email':
			text, html = self.generateEmailBody(**kwargs)
			cfg = {'to':self.generateEmailTo(), 'subject':self.generateEmailSubject(**kwargs), 'body':text, 'html': html}
			pipeline = EmailMessage
			
		elif c_type.lower() == 'xmpp':
			cfg = {'jid':self.user.jabber, 'message':self.generateXMPPMessage(**kwargs)}
			pipeline = XMPPMessage
			
		if len(kwargs) > 0:
			for key, value in kwargs.items():
				cfg[key] = value
				
		return (pipeline, cfg)


class QueueNotification(SocialNotification):
	
	queued_blob = db.ReferenceProperty(QueuedBlob, collection_name='notifications')


class LikeNotification(CINotification):
	
	action_verb = 'liked'

	def generateEmailSubject(self, **kwargs):
		return self.action.user.firstname+' '+self.action.user.lastname+' liked "'+self.action.content_item.title+'"'
		
	def generateEmailBody(self, **kwargs):
		
		link_host = os.environ['HTTP_HOST']
		link = 'http://'+link_host+'/go?c='+str(kwargs['action'].content_item.key())
		
		text_body = ("""
Hey There!

%(likeline)s

To view the content in your browser, head over to:
%(link)s


===================
Note: To reply to this comment by email, hit 'reply' and write your comment in the email body.
Do not modify the subject line or original email.
===================

Sincerely,
--Your friendly neighborhood email robot

(::spi::%(code)s::)
		""" % {'likeline': self.action.user.firstname+' '+self.action.user.lastname+' liked '+self.action.content_item.title+'!', 'link': 'http://'+os.environ['HTTP_HOST']+'/go?c='+link, 'code': str(self.action.key())})

		html_likeline = '<a href="http://'+str(link_host)+'/people/'+self.action.user.username+'">'
		html_likeline += self.action.user.firstname+' '+self.action.user.lastname
		html_likeline += '</a> liked <a href="'+link+'">'
		html_likeline += self.action.content_item.title+'</a>.'

		html_body = ("""
Hey There!<br /><br />

<b>%(likeline)s</b><br /><br />

===================<br />
Note: To reply to this comment by email, hit 'reply' and write your comment in the email body.<br />
Do not modify the subject line or original email.<br />
===================<br /><br />

Sincerely,<br />
--Your friendly neighborhood email robot

(::spi::%(code)s::)
		""" % {'likeline': html_likeline, 'comment_body': self.action, 'core': str(self.action.key())})
		
		return (text_body, html_body)
		
	def generateXMPPMessage(self, **kwargs):
		return self.action.user.firstname+' '+self.action.user.lastname+' liked "'+self.action.content_item.title+'"!'

	def generateChannelMessage(self, **kwargs):
		return SPIJSONAdapter().encode({'type':'LikeNotification', 'text':self.generateEmailSubject(), 'id':str(self.key())})
	
	
class CommentNotification(CINotification):
	
	action_verb = 'commented on'

	def generateEmailSubject(self, **kwargs):
		
		subject = None
		if 'notification' in kwargs:
			relation = kwargs['notification']['relation']
			if relation == 'creator':
				subject = self.action.user.firstname+' '+self.action.user.lastname+' commented on your "'+self.action.content_item.title+'"'
			elif relation == 'sibling':
				subject = self.action.user.firstname+' '+self.action.user.lastname+' also commented on the "'+self.action.content_item.title
				
		if subject is None:
			subject = self.action.user.firstname+' '+self.action.user.lastname+' commented on "'+self.action.content_item.title+'"'
		
		return self.action.user.firstname+' '+self.action.user.lastname+' commented on "'+self.action.content_item.title+'"'
		
		
	def generateEmailBody(self, **kwargs):
		
		current_host = os.environ['SERVER_NAME']+':'+os.environ['SERVER_PORT']
		
		link = 'http://'+current_host+'/go?c='+str(self.action.content_item.key())
		
		text_body = ("""
Hey There!

%(commentline)s:
"%(commentbody)s"

To view the comment in your browser, head over to:
%(link)s


===================
Note: To reply to this comment by email, hit 'reply' and write your comment in the email body.
Do not modify the subject line or original email.
===================

Sincerely,
--Your friendly neighborhood email robot

(::spi::%(code)s::)
		""" % {'commentline': self.action.user.firstname+' '+self.action.user.lastname+' commented on '+self.action.content_item.title,
				'link': 'http://'+current_host+'/go?c='+str(self.action.content_item.key()),
				'commentbody': self.action.text,
				'code': str(self.action.key())
		})
		
		
		html_commentline = '<a href="http://'+current_host+'/people/'+self.action.user.username+'">'
		html_commentline += self.action.user.firstname+' '+self.action.user.lastname
		html_commentline += '</a> commented on <a href="'+link+'">'
		html_commentline += self.action.content_item.title+'</a>.'
		
		html_body = ("""
Hey There!

<b>%(commentline)s:</b>
"%(commentbody)s"


===================
Note: To reply to this comment by email, hit 'reply' and write your comment in the email body.
Do not modify the subject line or original email.
===================

Sincerely,
--Your friendly neighborhood email robot

(::spi::%(code)s::)
		""" % {'commentline': html_commentline, 'commentbody': self.action.text, 'code': str(self.action.key())})
		
		return (text_body, html_body)
		
		
	def generateXMPPMessage(self, **kwargs):
		return self.action.user.firstname+' '+self.action.user.lastname+' commented on "'+self.action.content_item.title+'"'

	def generateChannelMessage(self, **kwargs):
		return SPIJSONAdapter().encode({'type':'CommentNotification', 'text':self.generateEmailSubject(), 'id':str(self.key())})
		
		
class ShareNotification(CINotification):
	
	action_verb = 'shared'

	def generateEmailSubject(self, **kwargs):
		return self.action.user.firstname+' '+self.action.user.lastname+' shared something with you!'

	def generateEmailBody(self, **kwargs):
		body = self.action.user.firstname+' '+self.action.user.lastname+' thinks you should take a look at "'+self.action.content_item.title+'"'
		return body

	def generateXMPPMessage(self, **kwargs):
		return self.action.user.firstname+' '+self.action.user.lastname+' shared "'+self.action.content_item.title+'"'

	def generateChannelMessage(self, **kwargs):
		return SPIJSONAdapter().encode({'type':'ShareNotification', 'text':self.generateEmailSubject()})