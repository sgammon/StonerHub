# -*- coding: utf-8 -*-
import logging
import datetime
from google.appengine.ext import db

from project.services import remote
from project.services import message_types

from project.services.data import DataService
from project.services.data import QueryResponder
from project.services.data import NotFoundError
from project.services.data import NotLoggedInError
from project.services.data import EmptyRequestError
from project.services.data import MalformedRequestError

from project.models.search import *
from project.models.search import Tag
from project.models.content import Repository
from project.models.content import ContentItemType
from project.models.content import ContentItemFormat
from project.models.content import ContentItemCategory
from project.models.content_item import ContentItem
from project.models.security import User

from project.messages.data import content_item as messages


class ContentItemService(DataService):
	
	model = ContentItem
	
	filter_properties = {'repository':Repository, 'type':ContentItemType, 'format':ContentItemFormat, 'category':ContentItemCategory, 'tag':Tag}

	def run_ci_query(self, query, request):
		
		if hasattr(request, 'options'):
			result_struct = self.runQuery(query, request.options.limit, request.options.page, request.options.offset)
		else:
			result_struct = self.runQuery(query, 15, 1, None)
			
		total_count, result_count, resultset, cursor, datatables_meta = result_struct
			
		results = []
		for ci in resultset:
			
			if ci.category is not None:
				ci_category = messages.ContentItemCategory(key=self.keyToMessage(ci.category.key()), name=ci.category.name, description=ci.category.description, parent_category=None)
			else:
				ci_category = None
				
			ci_tags = []
			
			results.append(messages.ContentItemResponse(key=self.keyToMessage(ci.key()),
			 											repository=messages.Repository(key=self.keyToMessage(ci.repository.key()), name=ci.repository.name, description=ci.repository.description),
														category=ci_category,
														type=messages.ContentItemType(key=self.keyToMessage(ci.type.key()), name=ci.type.name),
														format=messages.ContentItemFormat(key=self.keyToMessage(ci.format.key()), name=ci.format.name, icon=ci.format.icon),
														tags=ci_tags,
														title=ci.title,
														description=ci.description,
														status=ci.status,
														like_count=ci.like_count, comment_count=ci.comment_count, view_count=ci.view_count))
														
		return messages.ContentItemListResponse(resultset=messages.ResultSetMeta(
													results_count=query.count(), returned_count=len(results),
													cursor=query.cursor()),
												content_items=results, timestamp=datetime.datetime.now().isoformat(), datagrid=datatables_meta)
		
	
	@remote.method(messages.ContentItemsListRequest, messages.ContentItemListResponse)
	def list(self, request):
		response = self.run_ci_query(ContentItem.all(), request)
		return response
		
	@remote.method(messages.ContentItemsByFragmentRequest, messages.ContentItemListResponse)
	def byRepository(self, request):
		try:
			repo = db.get(db.Key(request.repository))
			assert repo != None
		except (AssertionError, db.Error), e:
			repo = Repository.get_by_key_name(request.repository)
			if repo is None:
				raise NotFoundError

		return self.run_ci_query(ContentItem.all().filter('repository =', repo), request)
	
	@remote.method(messages.ContentItemsByFragmentRequest, messages.ContentItemListResponse)
	def byTag(self, request):
		try:
			t = db.get(db.Key(request.tag))
			assert t != None
		except (AssertionError, db.Error), e:
			t = Tag.get_by_key_name(request.tag)
			if tag is None:
				raise NotFoundError

		return self.run_ci_query(ContentItem.all().filter('tags =', t.key()), request)
	
	@remote.method(messages.ContentItemsByFragmentRequest, messages.ContentItemListResponse)
	def byUser(self, request):
		try:
			u = User.get(db.Key(request.user))
			assert u != None
		except (AssertionError, db.Error), e:
			u = User.get_by_key_name(request.user)
			if u is None:
				raise NotFoundError

		return self.run_ci_query(ContentItem.all().filter('createdBy =', u.key()), request)
	
	@remote.method(messages.ContentItemsByFragmentRequest, messages.ContentItemListResponse)
	def byCategory(self, request):
		try:
			c = ContentItemCategory.get(db.Key(request.category))
			assert c != None
		except (AssertionError, db.Error), e:
			c = ContentItemCategory.get_by_key_name(request.category)
			if c is None:
				raise NotFoundError
			
		return self.run_ci_query(ContentItem.all().filter('category =', c.key()), request)
	
	@remote.method(message_types.VoidMessage, messages.ContentItemListResponse)
	def recentlyCreated(self):
		return self.run_ci_query(ContentItem.all().order('-createdAt'), request)
	
	@remote.method(message_types.VoidMessage, messages.ContentItemListResponse)
	def recentlyModified(self):
		return self.run_ci_query(ContentItem.all().order('-modifiedAt'), request)