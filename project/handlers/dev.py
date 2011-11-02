from project.handlers import WebHandler

import os
import logging

from project.core import security

from project.forms.dev import FileBugForm

from project.dev.default_data import all_functions

from project.models.dev import Bug
from project.models.content_item import ContentItem


class SPIDevHandler(WebHandler):
	pass
	


class Index(SPIDevHandler):

	""" Dev index page with links to other dev pages and basic statistics. """

	def get(self):
		
		u = security.get_current_user()
		if u is not None and u.perm_dev_admin == True:
			return self.render('dev/index.html')
		else:
			self.abort(403)
			
			
class Environment(SPIDevHandler):
	
	''' Dev page for dumping environment variables. '''
	
	def get(self):
		namespace = self.api.multitenancy.get_namespace()
		return self.render('dev/environ.html', state=os.environ, namespace=namespace)


class Cache(SPIDevHandler):
	
	''' Dev page for accessing cache settings. '''
	
	def get(self):
		
		if self.request.get('flush', False) == 'success':
			flush_success = True
		else:
			flush_success = False
		
		return self.render('dev/memcache.html', stats=self.api.memcache.get_stats(), flush=flush_success)
		
	def post(self):

		if self.request.form.get('action', False) == 'flush_all':
			u = security.get_current_user()
			if u.perm_dev_admin == True:
				self.api.memcache.flush_all()
		return self.redirect(self.url_for('dev-cache', flush='success'))
		
		
class Security(SPIDevHandler):

	''' Dev page for checking current security status. '''

	def get(self):
		
		return self.render('dev/security.html', user=security.get_current_user())

	def post(self):
		pass	
		
		
class ManageAccountClaims(SPIDevHandler):

	''' Page for creating/deleting/checking the status of account claim tickets. '''

	def get(self, key=None, action=None):

		from wirestone.spi.models.security import AccountClaim

		success = self.request.get('success', False)

		if key is not None:
			c = AccountClaim.get(self.api.db.Key(key))

			if action is not None:

				if action == 'delete':
					return self.render('dev/security/claim-delete.html', claim=c)
					
		else:
			
			if action == 'provision':
				return self.render('dev/security/claim-create.html')
			else:			
				claims = AccountClaim.all().order('used').order('-used_at').fetch(50)
				return self.render('dev/security/claim-list.html', claims=claims, success=success)
		

	def post(self, key=None, action=None):
		
		from wirestone.spi.models.security import AccountClaim		
		
		action_f = self.request.form.get('action')
		if action == 'delete':
			if action_f == 'delete_confirmed':
				k = self.api.db.Key(key)
				self.api.db.delete(k)
				return self.redirect_to('dev-security-claims', success='true')
				
		elif action == 'provision':
			
			usr = self.request.form.get('username')
			a = AccountClaim(key_name=usr, username=usr).put()
			logging.info('Provisioned AccountClaim ticket at key '+str(a)+'.')
			return self.redirect_to('dev-security-claims', success='true')
			
		elif action == 'invite':
			
			usr = self.request.form.get('username')
			
			mail = {
				'sender': 's@providenceclarity.com',
				'to': usr+'@wire-stone.com',
				'body': 'Sam you are cool',
				'subject': 'cool'
			} 


			t = self.api.taskqueue.Task(params=mail, url='/_workers/mail/outbound')

			q = self.api.taskqueue.Queue(name='mail')
			q.add(t)

		
class Shell(SPIDevHandler):

	''' Dev page for checking current security status. '''

	def get(self):

		return self.response('<b>Dev Security</b>')

	def post(self):
		pass		
		
		
class DefaultData(SPIDevHandler):
	
	''' Dev page for adding a bunch of default data. '''

	def get(self):
		
		return self.render('dev/default_data.html', functions=[str(func.__name__) for func in all_functions], success=False)


	def post(self):
	
		logging.info('Dev: Creating default data.')
	
		results = []
		status = []
	
		logging.info('Beginning data creation routine...')
		for item in all_functions:

			logging.debug('--- Running insert function "'+str(item.__name__)+".")
			result = item()
			if result is not None:
				logging.debug('------ Result is not None. No errors encountered.')
				if isinstance(result[0], self.api.db.Model):
					logging.debug('------ Created '+str(len(result))+' keys of kind '+str(result[0].kind())+'.')
				else:
					logging.debug('------ Created '+str(len(result))+' keys.')
				logging.debug('------ Appending results. New results length: '+str(len(results))+'.')
				results = results+result
				status.append((str(item.__name__), len(result)))
			else:
				status.append((str(item.__name__), 0))
		
		
		logging.info('Default data operation completed successfully.')
			
		return self.render('dev/default_data.html', functions=[str(func.__name__) for func in all_functions], success=True, exec_results=status)
		
		
class FileBug(SPIDevHandler):
	
	def get(self):
		f = FileBugForm(self.request)
		f.set_method('post')
		f.set_action(self.url_for('file-bug'))
		
		if self.request.get('fileSuccess', False) != False:
			success = True
		else:
			success = False
		
		return self.render('dev/file_bug.html', form=f, success=success)
		
	def post(self):
		f = FileBugForm(self.request)
		
		b = Bug(title=f.title.data, description=f.description.data)
		b_key = b.put()
		
		try:
			self.api.mail.send_mail(sender="Providence/Clarity Notifier <s@providenceclarity.com>",
						  to=["Sam Gammon <samuel.gammon+bugreports@gmail.com>", "Neil Michel <neil.michel@wire-stone.com>"],
						  subject='"'+f.title.data+'" - SPI Universal Content Repository - Bug Report',
						  body="----- BUG REPORT ENCLOSED -----\n\n"+f.description.data+"\n\n----- BUG REPORT END -----\n\n"+'User: '+str(b.createdBy.name())+"\n"+'Bug Key: '+str(b_key))
		except Exception, e:
			logging.error('Encountered exception sending bug report: '+str(e))
		
		return self.redirect_to('file-bug', fileSuccess='true')
		
		
class IndexerRoot(SPIDevHandler):
	
	def get(self):
		return self.render('dev/indexer.html')
		

class IndexerMakeTask(SPIDevHandler):
	
	def get(self):
		return self.render('dev/indexer/queue_task.html', result=False)
		
	def post(self):

		if self.request.form.get('action', False) != False:
			if self.request.form.get('action').lower() == 'enqueuetask':
				
				c = ContentItem.get(self.api.db.Key(self.request.form.get('subject_key')))
				
				if self.request.form.get('dry_run', False) == False:
					worker, task = c.generateIndexJobTask()
					enqueued_task = None

				else:
					worker, task, enqueued_task = c.enqueueIndexJob()
				

				return self.render('dev/indexer/queue_task.html', result=True, ci=c, w=worker, t=task, e=enqueued_task, k=self.request.form.get('subject_key'))