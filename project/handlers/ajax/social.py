import logging
import datetime
import simplejson as json

from google.appengine.ext import db

from project.core import security as WirestoneSecurity

from project.handlers.ajax import SPIAjaxHandler

from project.models.social import Like as SocialLike
from project.models.social import Comment as SocialComment
from project.models.social import SocialNotification as Notification

from project.pipelines.social import DeleteNotifications
from project.pipelines.social import GenerateNotifications


class SocialAction(SPIAjaxHandler):
	
	''' Search for content and return matching items. '''
	
	def get(self, action=None, document=None):
		
		return self.post(action, document)
		
	
	def post(self, action=None, document=None):
		
		## Grab logging config
		app = Tipfy.app
		cfg = app.config.get('wirestone.spi.social')
		do_log = cfg['enable_ajax_logging']
		if do_log: logging.info('Starting AJAX social action request.')
		
		## Grab current user
		u = WirestoneSecurity.get_current_user()
		if do_log: logging.info('Current user: "'+str(u)+'".')
		
		if action is not None:
			
			if do_log: logging.debug('Action parameter is not None.')
			
			if document is not None:
				
				if do_log: logging.debug('Document parameter is not None.')
				
				try:
					
					## Convert to CI key.
					document_obj = db.get(db.Key(document))
					if do_log: logging.debug('Pulled document object: "'+str(document_obj)+'".')
				
					subject_user = u.key()
					if do_log: logging.debug('Generated user key: "'+str(subject_user)+'"')
					
				except:
					logging.error('Errors encountered converting user or document to valid key.')
					logging.debug('Action input: %s' % str(action))
					logging.debug('Document input: %s' % str(document))
					return self.fail('social_action', 'Errors encountered converting user or document to valid key.')
				
				def txn():
				
					op = []
					if do_log: logging.info('Beginning transaction.')
				
					## Create social action object & increment appropriate counter
					if action == 'like':
						
						existing = SocialLike.get_by_key_name(str(subject_user)+'::like', parent=document_obj)
						if existing is not None:
							return False, op, 'User already likes specified document.'
						
						sa_entity_obj = SocialLike(document_obj, key_name=str(subject_user)+'::like', user=subject_user, content_item=document_obj)
						sa_entity = sa_entity_obj.put()
						if do_log: logging.debug('---SocialLike pre-put object "'+str(sa_entity)+'".')

						document_obj.like_count = document_obj.like_count+1
						if do_log: logging.debug('---New CI like count: '+str(document_obj.like_count)+'.')
						document_obj.social_likes.append(str(sa_entity))
						document_obj.social_like_users.append(str(subject_user))
						
						op.append(GenerateNotifications(str(sa_entity)))						
						op_result = {'key':sa_entity, 'datestring': sa_entity_obj.createdAt.strftime('%A, %b %d %I:%M %p')}
						
					elif action == 'comment':
						sa_entity_obj = SocialComment(document_obj, user=subject_user, content_item=document_obj, text=self.request.form.get('body'))
						sa_entity = sa_entity_obj.put()
						if do_log: logging.debug('---SocialComment pre-put object "'+str(sa_entity)+'".')

						document_obj.comment_count = document_obj.comment_count+1
						if do_log: logging.debug('---New CI comment count: '+str(document_obj.comment_count)+'.')						
						document_obj.social_comments.append(str(sa_entity))
						
						op.append(GenerateNotifications(str(sa_entity)))
						op_result = {'key':sa_entity}
						
					elif action == 'unlike':
						q = SocialLike.all().ancestor(document_obj).filter('user =', subject_user).get()
						if do_log: logging.debug('---Pulled like: "'+str(q)+'".')

						if q is not None and q != []:
							document_obj.like_count = document_obj.like_count-1
							if do_log: logging.debug('---List index: '+str(document_obj.social_likes.index(str(q.key())))+'.')
							if do_log: logging.debug('---Username list index: '+str(document_obj.social_like_users.index(str(subject_user)))+'.')
							document_obj.social_likes.remove(str(q.key()))
							document_obj.social_like_users.remove(str(subject_user))
							if do_log: logging.debug('---New CI like count: '+str(document_obj.like_count)+'.')	

							op.append(DeleteNotifications(action=str(q.key())))
							db.delete(q)
							op_result = True
						else:
							op_result = False
							
					elif action == 'uncomment':
						try:
							action_key = self.request.args.get('action_key', default=False)
							if action_key == False:
								return False, op, 'Must specify an action key.'
							else:
								c = db.get(db.Key(action_key))
								if do_log: logging.debug('Action key: '+str(c)+'.')
						except:
							return False, op, 'Could not retrieve specified action key.'
							
						document_obj.social_comments.remove(str(c.key()))
						document_obj.comment_count = document_obj.comment_count-1
						op_result = {'key':str(c.key())}						
						
						## Delete notifications & Comment
						op.append(DeleteNotifications(action=str(c.key())))
						db.delete(c)
							
					else:
						return False, op, 'Must specify valid social action type. Options are "like" or "comment".'
						
					## Flag as dirty for caching + indexing
					document_obj.do_healthcheck = True

					## Always save document object
					document_obj.put()
					

					## Save everything
					if do_log: logging.debug('---Transaction result: '+str(op_result)+'.')
					
					if isinstance(op_result, (basestring, dict, db.Key)) or op_result == True:
						return True, op, op_result
					else:
						return False, op, 'Unidentified datastore error.'
					
				## Run transaction
				success, op, response = db.run_in_transaction(txn)
				if do_log: logging.info('Transaction complete. Success: '+str(success)+'. Response: "'+str(response)+'".')
				
				## Queue notifications
				if success == True and op is not None and len(op) > 0:
					for operation in op:
						operation.start(queue_name='social')
					
				## Respond appropriately
				if success == True:
					if not isinstance(response, dict):
						return self.render('social_action', key=response)
					else:
						return self.render('social_action', **response)
				else:
					return self.fail('social_action', response)
				
			else:
				return self.fail('social_action', 'Must specify document key.')
			
		else:
			return self.fail('social_action', 'Must specify social action type.')
			
			
class SocialNotification(SPIAjaxHandler):

	''' Handles methods related to the Social Notifications framework. '''

	def get(self, key=None, action=None):
		return self.post(key, action)


	def post(self, key=None, action=None):
		pass