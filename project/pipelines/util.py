from google.appengine.ext import db

from google.appengine.api import mail
from google.appengine.api import xmpp
from google.appengine.api import channel

from project.pipelines import SPIPipeline


class EmailMessage(SPIPipeline):
	
	def run(self, **kwargs):

		messageArgs = {}
		messageFields = ['sender', 'to', 'cc', 'bcc', 'reply_to', 'subject', 'body', 'html', 'attachments']
		for key, value in kwargs.items():
			if key in messageFields:
				messageArgs[key] = value

		m = mail.EmailMessage(**messageArgs)
		return m.send()
		
		
class XMPPMessage(SPIPipeline):
	
	def run(self, jid, message, **kwargs):
		pass
		
		
class ChannelMessage(SPIPipeline):
	
	def run(self, channel_id, message, **kwargs):
		return channel.send_message(channel_id, message)