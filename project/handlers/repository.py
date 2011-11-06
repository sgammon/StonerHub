import config
import logging

from wtforms import fields

from project.handlers import WebHandler

from project.models.search import Tag

from google.appengine.ext import db

from project.models.content import Repository
from project.models.content import ContentItemType
from project.models.content import ContentItemFormat
from project.models.content import ContentItemCategory

from project.models.content_item import ContentItem


class List(WebHandler):

	''' Output a list of repositories that are hosted on the system. '''

	def get(self):
		
		cfg = config.config.get('wirestone.spi.datamodel.repository')
		r = Repository.all().fetch(cfg['max_repositories'])
		if len(r) > 0:
			repositories = r
		else:
			repositories = False
		
		self.render('repository/list.html', repositories=repositories)


class Create(WebHandler):
    
	''' Create a repository. '''

	def get(self):
		
		f = self.get_model_form(Repository, action=self.url_for('repository-create'), method='post', exclude=['permissions_descriptor'], request=self.request)
		self.render('repository/create.html', create_repo_form=f)
       	
	def post(self):

		f = self.get_model_form(Repository, action=self.url_for('repository-create'), method='post', exclude=['permissions_descriptor'], request=self.request)
		
		if f.validate():
			r = Repository(key_name=f.name.data.lower().replace('&','and').replace(' ','-'))
			f.populate_obj(r)
			r.put()
			return self.redirect_to('repository-list')
		else:
			self.render('repository/create.html', create_repo_form=f)
        

class View(WebHandler):
    
	''' View details about a repository (access stats, permissions, content summary, etc). '''

	def get(self, repo):
		
		repository = Repository.get_by_key_name(repo)
		ci_count = ContentItem.all().ancestor(repository).count()
		category_count = ContentItemCategory.all().ancestor(repository).count()
		
		self.render('repository/view.html', repository=repository, ci_count=ci_count, category_count=category_count)
        
        
class Edit(WebHandler):
	
	''' Edit a repository object. '''
    
	def get(self, repo):
		
		r = Repository.get_by_key_name(repo)
		f = self.get_model_form(Repository, action=self.url_for('repository-edit', repo=r.key().name()), method='post', request=self.request, obj=r)
			
		self.render('repository/edit.html', edit_repo_form=f, repository=r)
        
	def post(self, repo):

		r = Repository.get_by_key_name(repo)
		f = self.get_model_form(Repository, action=self.url_for('repository-edit', repo=r.key().name()), method='post', request=self.request, obj=r)
		
		if f.validate():
			f.populate_obj(r)
			r.put()
			self.redirect(self.url_for('repository-list'))
		else:
			self.render('repository/edit.html', create_repo_form=f, repository=r)
        
        
class Permissions(WebHandler):
	
	''' Edit permissions for a repository object. '''
    
	def get(self, repo):
		self.response('<b>Edit Repo Perms</b>')
        
	def post(self, repo):
		pass
        

class Delete(WebHandler):
	
	''' Delete a repository object. '''
    
	def get(self, repo):
		self.response.write('<b>Delete Repo</b>')
        
	def post(self, repo):
		pass
		
        
class Tags(WebHandler):
	
	''' View tags in a repository. '''
    
	def get(self, repo):
		self.response.write('<b>View Tags in Repo</b>')


class CreateCategory(WebHandler):
	
	''' Create a category in a repository. '''
	
	def makeForm(self, r, formdata=None, obj=None):
		f = self.get_model_form(ContentItemCategory, exclude=[], request=self.request)		
		categories = ContentItemCategory.all().ancestor(r)
		categories = categories.fetch(categories.count())

		f.parent_category = fields.SelectField(choices=[('__NULL__', '----No Parent Category----')]+[(str(category.key()), category.name) for category in categories])
		f = f(formdata, obj)
		
		f.set_action(self.url_for('repository-category-create', repo=r.key().name()))
		f.set_method('post')		
		
		return f


	def get(self, repo):
		
		r = Repository.get_by_key_name(repo)
		f = self.makeForm(r)
		m = self.request.get('message', False)
		
		self.render('repository/create-category.html', form=f, repository=r, message=m)


	def post(self, repo):
		
		r = Repository.get_by_key_name(repo)
		f = self.makeForm(r, self.request)

		obj = ContentItemCategory(r, key_name=f.name.data.lower().replace(' ', '-'))
		
		if f.validate():
			if f.parent_category.data is not None and f.parent_category.data != '__NULL__':
				parent_category = db.Key(f.parent_category.data)
				obj.parent_category = parent_category

			obj.name = f.name.data
			obj.description = f.description.data

			obj.put()
			
			return self.redirect_to('repository-category-create', repo=repo, message='Successfully created the category "'+f.name.data+'".')
		else:
			self.render('repository/create-category.html', form=f, repository=r, message='Woops! Try again.')


class Categories(WebHandler):
	
	''' View categories in a repository. '''
	
	def get(self, repo):

		r = Repository.get_by_key_name(repo)
		
		c = ContentItemCategory.all().ancestor(r).order('name')
		categories = {}
		category_records = c.fetch(c.count())
		
		for category in category_records:
			count = ContentItem.all().filter('category =', category.key()).count()
			categories[category.name] = {'category': category, 'count':count, 'filter_path':'category/'+category.key().name()}
		
		self.render('repository/categories.html', categories=categories, repository=r)
		

class Content(WebHandler):
	
	''' List content in a repository. '''
	
	def get(self, repo):
		
		grid = ContentItem.generateGrid()

		r = Repository.get_by_key_name(repo)

		grid.set_endpoint('api-call', module='data', service='ContentItem')
		grid.set_method('byRepository', repository=str(r.key()))
		
		self.render('repository/content.html', grid=grid, repository=r)
	

class RecentContent(WebHandler):
	
	''' List content in a repository, ordered by modifiedAt (descending). '''
	
	def get(self, repo):
		
		grid = ContentItem.generateGrid()
		r = Repository.get_by_key_name(repo)
		
		grid.set_endpoint('api-call', module='data', service='ContentItem')
		
		filterset = [
		
			('repository','=',r.key().name())
		
		]
		
		orderings = [
			('modifiedAt','dsc')
		]
		
		grid.set_method('query', filters=filterset, orderings=orderings)
		
		self.render('repository/recent-content.html', grid=grid, repository=r)
		
		
class PopularContent(WebHandler):
	
	''' List content in a repository, ordered by popularity. '''
	
	def get(self, repo):
		
		grid = ContentItem.generateGrid()
		r = Repository.get_by_key_name(repo)
		
		grid.set_endpoint('api-call', module='data', service='ContentItem')
		grid.set_method('popularContent', repository=str(r.key()))
		
		self.render('repository/recent-content.html', grid=grid, repository=r)
		
		
class FilteredContent(WebHandler):
	
	''' List content in a repository that matches a list of filters of arbitrary length. '''
	
	def get(self, repo, filters):
		
		## Generate filters from URL
		filters = filters.split('/')
		segments = {}
		for i in xrange(0, len(filters)):
			if i in segments:
				continue
			else:
				try:
					segments[i] = (filters[i], '=', filters[i+1])
					segments[i+1] = None
				except:
					continue
					
		## Start building template params
		result_params = {}
		
		## Convert URL filters into segments
		filter_segments = filter(None,segments.values())
		
		## Resolve repository
		r = Repository.get_by_key_name(repo)
		result_params['repository'] = r		
		
		## Generate grid header & caption
		grid_header = r.name ## defaults
		grid_subline = 'Repository' ## defaults
		grid_caption = 'Showing all content from the '+r.name+' repository.'
		
		logging.info('filter_segments: '+str(filter_segments))
		
		if len(filter_segments) == 1:
			f_name, f_operator, f_value = filter_segments[0]
			if f_name == 'category':
				context = ContentItemCategory.get_by_key_name(f_value, parent=r)
				grid_header = context.name
				grid_subline = context.parent().name
				grid_caption = 'Showing content from the '+r.name+' repository in the category "'+context.name+'".'
			elif f_name == 'tag':
				context = Tag.get_by_key_name(f_value)
				grid_header = context.value
				grid_subline = r.name
				grid_caption = 'Showing content from the '+r.name+' repository tagged with "'+context.value+'".'
				
		result_params['grid_header'] = grid_header
		result_params['grid_subline'] = grid_subline
		result_params['grid_caption'] = grid_caption
		
		## Generate RPC results grid
		filter_segments.insert(0, ('repository', '=', repo))
		grid = ContentItem.generateGrid()		
		grid.set_endpoint('api-call', module='data', service='ContentItem')
		grid.set_method('query', filters=filter_segments)
		result_params['grid'] = grid		

		self.render('repository/content.html', **result_params)