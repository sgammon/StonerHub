import json
import logging
import mimetypes

from project.handlers import WebHandler
from wtforms import fields

from project.core.forms import get_model_form
from project.core.forms.tagging import TagListField
from project.core.forms.tagging import CategoriyListField

from project.models.assets import StoredAsset

from project.models.content import QueuedBlob
from project.models.content import Repository
from project.models.content import ContentItemType
from project.models.content import ContentItemFormat
from project.models.content import ContentItemCategory

from project.models.ticket import UploadSessionTicket

from project.models.search import Tag
from project.models.search import UserTag

from project.models.content_item import ContentItem
from project.models.content_item import getContentItemCategoryOptions

from project.models.social import Like as SocialLike
from project.models.social import Comment as SocialComment


class Main(WebHandler):
	
	''' Shows a summary of content in the system. '''
	
	def get(self):
		self.response('<b>Global Content</b>')
		

class Create(WebHandler):
	
	''' Universal page to upload/create content items. '''
	
	def get(self, progress=0, repo=None, sessionkey=None, blobkey=None, action=None, **kwargs):
		
		
		if 'inject' in self.request.args:
			queued_blobs = self.request.get('queued')
			blobkeys = []
			
			queued_blobs = QueuedBlob.get([self.api.db.Key(item) for item in queued_blobs])
			
			for queued in queued_blobs:
				if queued is not None:
					blobkeys.append(queued.blob.key())
					
			upload_session = UploadSessionTicket(blob_count=len(blobkeys), progress='upload', status='processing', queued=[str(item) for item in blobkeys])
			sessionkey = str(upload_session.put())
			blobkey = str(blobkeys[0])
			progress = 2
			injectedTitle = queued_blobs[0].title
			injectedDescription = queued_blobs[0].description
		else:
			injectedTitle = None
			injectedDescription = None
			
		
		## Set default template stuff
		total_upload_count = 1
		current_upload_index = 1
		
		template_params = {'categories_list': False}
		
		if blobkey is not None:
			blob_info_obj = self.api.blobstore.BlobInfo.get(blobkey)
		else:
			blob_info_obj = False
		
		## Generate success URL and post action URL
		action_url_params = {'progress':progress}
		
		if repo is not None:
			repository = Repository.get_by_key_name(repo)
			if sessionkey is not None:
				endpoint = 'content-item-create-step-blobkey-with-session'
				action_url_params['sessionkey'] = sessionkey
			else:
				endpoint = 'content-item-create-step'
			action_url_params['repo'] = repo
		else:
			repository = False
			if sessionkey is not None:
				endpoint = 'content-create-step-blobkey-with-session'
				action_url_params['sessionkey'] = sessionkey
			else:
				endpoint = 'content-create-step'
		
		if blobkey is not None:
			action_url_params['blobkey'] = blobkey
		
		if progress == 0:
			action_url_params['progress'] = 1
			self.redirect_to(endpoint, **action_url_params)
		
		## Generate action URL
		action_url = self.url_for(endpoint, **action_url_params)
					
		## Form defaults to False
		f = False

		## First step: file upload and name, type, category, description, file, format
		if progress == 2:
			
			## If we're cancelling an upload
			if action == 'cancel':
				## Guess content type
				b = self.api.blobstore.BlobInfo.get(self.api.blobstore.BlobKey(blobkey))
				upload_session = UploadSessionTicket.get(self.api.db.Key(sessionkey))
				upload_session.queued.remove(str(b.key()))
				
				### @TODO: Switch to Media API for queued & transactional deletion of blob data
				b.delete()
				
				if len(upload_session.queued) == 0:
					upload_session.queued = upload_session.finished[:]
					upload_session.finished = []
					upload_session.progress = 'tagging'
					action_url_params['progress'] = '3'
				else:
					action_url_params['progress'] = '2'

				if len(upload_session.queued) == 0:
					self.redirect_to('content-create')
				else:
					blob_obj = upload_session.queued[0]
					action_url_params['blobkey'] = blob_obj
					upload_session.put()
				
					self.redirect_to(endpoint, **action_url_params)
					
			else:
				## Generate info form
				if blobkey is not None:

					## Generate form class for contentitem details (title, description, etc)
					AddContentStep2Form = get_model_form(ContentItem)

					## Account for injected title/description
					if injectedTitle is not None:
						AddContentStep2Form.title = fields.TextField(default=injectedTitle)
						AddContentStep2Form.description = fields.TextField(default=injectedDescription)
					
					## Set choices for categories <!--- UNCOMMENT FOR AUTOCOMPLETE MODE
					#AddContentStep2Form.category = fields.TextField()
					AddContentStep2Form.category = fields.SelectField(choices=[('__NULL__', '--- Select a Category ---')])
					categories_list = getContentItemCategoryOptions()
					template_params['categories_list'] = SPIJSONAdapter().encode(categories_list)

					## Replace 'repository' parameter if we have a defined repo...
					if repo is not None:
						if hasattr(AddContentStep2Form, 'repository'):
							delattr(AddContentStep2Form, 'repository')
						AddContentStep2Form.repository = fields.HiddenField(str(repository.key()))
					
					## Guess content type
					b = self.api.blobstore.BlobInfo.get(self.api.blobstore.BlobKey(blobkey))
					content_type, encoding = mimetypes.guess_type(b.filename)
					if content_type is None:
						## Attempt to resolve by file extension mapping
						file_parts = str(b.filename).split('.')
						format = ContentItemFormat.all().filter('valid_extensions =', file_parts[-1]).get()
					else:
						format = ContentItemFormat.get_by_key_name(content_type)
					
					AddContentStep2Form.mime = fields.HiddenField(default=content_type)
				
					if format is not None:
						AddContentStep2Form.format = fields.HiddenField(default=str(format.key()))
						AddContentStep2Form.type = fields.HiddenField(default=str(format.type.key()))
					else:
						content_type = 'application/octet-stream'					

					upload_session = UploadSessionTicket.get(self.api.db.Key(sessionkey))
					total_upload_count = upload_session.blob_count
					current_upload_index = len(upload_session.finished)+1
					
					## Add hidden fields for current blob key, remaining blob keys, and action
					AddContentStep2Form.action = fields.HiddenField(default='content_item_create')
					AddContentStep2Form.data = fields.HiddenField(default=blobkey)
					AddContentStep2Form.endpoint = fields.HiddenField(default=endpoint)
					AddContentStep2Form.upload_session_key = fields.HiddenField(default=str(sessionkey))
				
					## Change the submit button label
					if hasattr(AddContentStep2Form, 'submit'):
						delattr(AddContentStep2Form, 'submit')
						f.submit = fields.SubmitField(default='Next Step >')			
				
					## Instantiate created form
					f = AddContentStep2Form(self.request)
				
					## Set action and method
					f.set_action(action_url)
					f.set_method('post')
				
					template_params['mime'] = content_type
					template_params['cancel_link'] = self.url_for('content-create-step-blobkey-with-session-with-action', action='cancel', **action_url_params)
			
		## Second step: tags, keywords
		elif progress == 3:
		
			if blobkey == 'success':
				progress = 'success'
				
				upload_session = UploadSessionTicket.get(self.api.db.Key(sessionkey))
				new_content_items  = self.api.db.get(upload_session.queued)
				
				template_params['new_content_items'] = new_content_items
				
				
			else:
				
				upload_session = UploadSessionTicket.get(self.api.db.Key(sessionkey))
				blob_info_obj = ContentItem.get(blobkey).asset.blobstore_data
				
				total_upload_count = upload_session.blob_count
				current_upload_index = len(upload_session.finished)+1			
				f = ContentItemTagsForm
				f.data = fields.HiddenField(default=blobkey)
				f.content_item = fields.HiddenField(default=blobkey)
				f.upload_session_key = fields.HiddenField(default=sessionkey)
				f = f(self.request)

				## Set action and method
				f.set_action(action_url)
				f.set_method('post')
			
		## Calculate template parameters
		template_params['total_upload_count'] = total_upload_count
		template_params['current_upload_index'] = current_upload_index
		template_params['progress'] = str(progress)
		template_params['form'] = f
		template_params['next_action_url'] = action_url
		template_params['repo'] = repository
		template_params['blob'] = blobkey
		template_params['blob_obj'] = blob_info_obj
		
		## Finish and render...
		self.render('content_item/create.html', dependencies=['Plupload','MarkItUp','autocomplete'], **template_params)
			
	
	def post(self, progress=None, sessionkey=None, repo=None, blobkey=None):

		## Build next action URL
		action_url_params = {}
		if repo is not None:
			repository = Repository.get_by_key_name(repo)
			if sessionkey is not None:
				endpoint = 'content-item-create-step-blobkey-with-session'
				action_url_params['sessionkey'] = sessionkey
			else:
				endpoint = 'content-item-create-step-blobkey'
			action_url_params['repo'] = repo
		else:
			repository = False
			if sessionkey is not None:
				endpoint = 'content-create-step-blobkey-with-session'
				action_url_params['sessionkey'] = sessionkey
			else:
				endpoint = 'content-create-step-blobkey'
		
		
		## Required param...
		if progress is not None:
			
			## Pass off to Step 2 because we're submitting a completed uploader form...
			if progress == 1:
				
				## Extract encoded blob objects
				upload_session = self.request.form.get('upload_session_key', False)

				## Get upload session
				upload_session = UploadSessionTicket.get(self.api.db.Key(upload_session))
				upload_session.progress = 'meta'
				upload_session.put()
				
				first_blob = upload_session.queued[0]
				
				action_url_params['blobkey'] = str(first_blob)
				action_url_params['progress'] = '2'
				action_url_params['sessionkey'] = str(upload_session.key())
				
				if repo is not None:
					endpoint = 'content-item-create-step-blobkey-with-session'
				else:
					endpoint = 'content-create-step-blobkey-with-session'
				
				self.redirect_to(endpoint, **action_url_params)

			## Process submitted content item form
			elif progress == 2:


				AddContentStep2Form = get_model_form(ContentItem)
				AddContentStep2Form.category = fields.SelectField(choices=getContentItemCategoryOptions())
				AddContentStep2Form.action = fields.HiddenField(default='content_item_create')
				AddContentStep2Form.data = fields.HiddenField(default=blobkey)
				AddContentStep2Form.endpoint = fields.HiddenField(default=endpoint)
				AddContentStep2Form.upload_session_key = fields.HiddenField(default=str(sessionkey))
				
				form = AddContentStep2Form(self.request)
				
				## Get content item type
				c_type = ContentItemType.get(self.api.db.Key(form.type.data))
				
				## Create a new content item, with repository as parent
				if repo is not None:
					repository = Repository.get_by_key_name(repo)
				else:
					repository = Repository.get(form.repository.data)
					
				c = ContentItem(repository)
				
				## Set CI params, save
				c.title = form.title.data
				c.type = c_type
				c.format = ContentItemFormat.get(self.api.db.Key(form.format.data))
				c.description = form.description.data
				c.repository = repository
				try:
					c.category = ContentItemCategory.get(self.api.db.Key(form.category.data))
				except:
					c.category = None
				ci_key = c.put()
				
				#c.permissions_mode = form.permissions_mode.data ## NOT YET SUPPORTED
				#c.permissions_descriptor = form
				
				## Provision asset
				c.asset = StoredAsset.provisionBlobstoreAsset(form.data.data, parent=c)

				c.put()
			
				## Grab the upload session, remove new blob from the queue, and add it to finished
				upload_session = UploadSessionTicket.get(self.api.db.Key(sessionkey))
				try:
					upload_session.queued.remove(str(blobkey))
					upload_session.finished.append(str(ci_key))
				except ValueError:
					## CI is already saved...
					pass

			
				## Grab the next blob for step 2 or send to step 3
				if len(upload_session.queued) == 0:
					upload_session.queued = upload_session.finished[:]
					upload_session.finished = []
					upload_session.progress = 'tagging'
					action_url_params['progress'] = '3'
				else:
					action_url_params['progress'] = '2'

				blob_obj = upload_session.queued[0]
				action_url_params['blobkey'] = blob_obj
				upload_session.put()
				
				self.redirect_to(endpoint, **action_url_params)
				
			## Process submitted tagz
			elif progress == 3:
				
				ContentItemTagsForm.action = fields.HiddenField(default='content_item_tag')
				ContentItemTagsForm.data = fields.HiddenField(default=blobkey)
				ContentItemTagsForm.endpoint = fields.HiddenField(default=endpoint)
				ContentItemTagsForm.upload_session_key = fields.HiddenField(default=str(sessionkey))
			
				form = ContentItemTagsForm(self.request)
			
				content_item = ContentItem.get(self.api.db.Key(form.data.data))
				upload_session = UploadSessionTicket.get(self.api.db.Key(form.upload_session_key.data))
			
				content_item.tags = form.tags.data
				content_item.put()
				
				## Remove from queue and add to finished
				upload_session.queued.remove(str(content_item.key()))
				upload_session.finished.append(str(content_item.key()))
				
				## Grab the next blob for step 2 or send to step 3
				if len(upload_session.queued) == 0:
					upload_session.queued = upload_session.finished[:]
					upload_session.queued.reverse()
					upload_session.finished = []
					upload_session.status = 'queued'
					action_url_params['blobkey'] = 'success'
					
					## Queue for indexing
					for item in upload_session.queued:
						OrganicIndexer(key=item).start()
					
				else:
					action_url_params['blobkey'] = upload_session.queued[0]

				action_url_params['sessionkey'] = sessionkey
				action_url_params['progress'] = '3'
								
				upload_session.put()
			
				self.api.memcache.flush_all()
				self.redirect_to(endpoint, **action_url_params)
			
			
		## Fail if no 'progress' param
		else:
			self.response.write('<b>Must provide required parameter: "progress".')
			
		
class All(WebHandler):
	
	''' Shows all content from all repositories. '''
	
	def get(self):
		
		grid = ContentItem.generateGrid()

		grid.set_endpoint('api-call', module='data', service='ContentItem')
		grid.set_method('list')
		
		context = {'grid': grid}
		
		self.render('content_item/all.html', dependencies=[], **context)
		
		
class Recent(WebHandler):
	
	''' Recent content handler '''
	
	def get(self):

		grid = ContentItem.generateGrid()

		grid.set_endpoint('api-call', module='data', service='ContentItem')
		grid.set_method('recentlyCreated')
		
		context = {'grid': grid}
		
		self.render('content_item/recent.html', dependencies=[], **context)
	
		
class ByUser(WebHandler):
	
	''' View content by a user. '''
	
	def get(self, userid=None):
		self.response('<b>View content by user</b>')
		
		
class ByCurrentUser(WebHandler):
	
	''' View content created by the currently logged in user. '''

	def get(self):
		
		grid = ContentItem.generateGrid()

		grid.set_endpoint('api-call', module='data', service='ContentItem')
		grid.set_method('byUser', user=str(get_current_user().key()))
		
		context = {'grid': grid}
		
		self.render('content_item/mine.html', dependencies=[], **context)
				

class View(WebHandler):
	
	''' View a content item. '''
    
	def get(self, repo, key):
		
		## Resolve Repository
		try:
			r = self.api.db.get(self.api.db.Key(repo))
		except:
			r = Repository.get_by_key_name(repo)
		
		## Resolve CI
		try:
			c = self.api.db.get(self.api.db.Key(key))
		except:
			return self.abort(404)
				
		## Get tags...
		to_fetch = []
		cached_tags = self.api.memcache.get_multi([str(k.name()) for k in c.tags], 'SPIRuntime//Tag-')
		for tag in c.tags:
			if tag not in cached_tags:
				to_fetch.append(tag)
		tags = cached_tags.values()+self.api.db.get(to_fetch)
		
		## Get comments...
		comments = self.api.memcache.get('CIComments-'+str(c.key()))
		if comments is None:
			comments = SocialComment.all().ancestor(c).order('createdAt').fetch(50)
			self.api.memcache.set('SPIRuntime//CIComments-'+str(c.key()), comments)
		
		self.render('content_item/view.html', dependencies=['fancybox'], repo=r, content_item=c, comments=comments, tags=tags, hits=current_hitcount)

        
class Edit(WebHandler):
	
	''' Edit a content item object. '''
	
	def get(self, repo, key):

		try:
			r = Repository.get_by_key_name(repo)
			c = self.api.db.get(self.api.db.Key(key))
		except:
			self.abort(404)
		
		## Get comments...
		comments = self.api.memcache.get('CIComments-'+str(c.key()))
		if comments is None:
			comments = SocialComment.all().ancestor(c).order('createdAt').fetch(50)
			self.api.memcache.set('SPIRuntime//CIComments-'+str(c.key()), comments)
		

		EditContentItemForm = get_model_form(ContentItem)
		del EditContentItemForm.type
		del EditContentItemForm.format
		del EditContentItemForm.repository
		
		
		categories = getContentItemCategoryOptions()
		
		if str(r.key()) in categories:
			EditContentItemForm.category = CategoryListField(choices=[(k['name'], k['value']) for k in categories[str(r.key())]])
		else:
			del EditContentItemForm.category
		
		EditContentItemForm.tags = TagListField(default=c.tags)
				
		form = EditContentItemForm(self.request, obj=c)
		
		form.set_method('post')
		form.set_action(self.url_for('content-item-edit', repo=repo, key=key))	
		
		self.render('content_item/edit.html', repo=r, content_item=c, comments=comments, form=form)
		
		
	def post(self, repo, key):

		try:
			r = Repository.get_by_key_name(repo)
			c = self.api.db.get(self.api.db.Key(key))
		except:
			self.abort(404)

		EditContentItemForm = get_model_form(ContentItem)
		del EditContentItemForm.type
		del EditContentItemForm.format
		del EditContentItemForm.repository

		EditContentItemForm.tags = TagListField(default=c.tags)
		EditContentItemForm.category = CategoryListField(choices=getContentItemCategoryOptions())		

		form = EditContentItemForm(self.request, obj=c)

		c.title = form.title.data
		c.description = form.description.data
		#c.permissions_mode = form.permissions_mode.data
		c.category = form.category.data
		c.tags = form.tags.data

		ci_key = c.put()

		## Queue for index update
		OrganicIndexer(key=str(ci_key), update=True).start()
		
		self.redirect_to('content-item-view', repo=repo, key=key)
			
		

class Permissions(WebHandler):
	
	''' Edit permissions to access a content item object. '''
	
	def get(self, repo, key):
		self.response('<b>Content Permissions</b>')
		
	def post(self, repo, key):
		pass
		
		
class Delete(WebHandler):
	
	''' Delete a content item object. '''
	
	def get(self, repo, key):
		
		try:
			r = Repository.get_by_key_name(repo)
			c = self.api.db.get(self.api.db.Key(key))
		except:
			return self.abort(404)
		
		self.render('content_item/delete.html', repo=r, content_item=c)
		

	def post(self, repo, key):

		if self.request.form.get('delete_confirm', False) == 'true':

			ci = self.api.db.get(self.api.db.Key(key))

			## @TODO: Use media API for transactional deletion of blobs
			if ci is not None:
				ci.deleteAsset()
				ci.delete()
				
			self.api.memcache.flush_all()
			self.redirect_to('landing')

		else:
			self.redirect_to('content-item-view', repo=repo, key=key)