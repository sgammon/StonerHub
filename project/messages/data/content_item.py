from protorpc import messages

from project.messages.data import ModelKey
from project.messages.data import QueryMeta
from project.messages.data import DatagridMeta
from project.messages.data import ResultSetMeta

	
class Repository(messages.Message):

	key = messages.MessageField(ModelKey, 1)
	name = messages.StringField(2)
	description = messages.StringField(3)


class ContentItemType(messages.Message):

	key = messages.MessageField(ModelKey, 1)
	name = messages.StringField(2)


class ContentItemFormat(messages.Message):

	key = messages.MessageField(ModelKey, 1)
	name = messages.StringField(2)
	icon = messages.StringField(3)
	
	
class ContentItemCategory(messages.Message):

	key = messages.MessageField(ModelKey, 1)
	name = messages.StringField(2)
	description = messages.StringField(3)
	parent_category = messages.StringField(4)
	
	
class ContentItemTag(messages.Message):
	
	key = messages.MessageField(ModelKey, 1)
	value = messages.StringField(2)


class AssetType(messages.Message):
	
	key = messages.MessageField(ModelKey, 1)
	name = messages.StringField(2)
	mimetypes = messages.StringField(3)
	expiration = messages.StringField(4)
	parent_type = messages.StringField(5)


class StoredAsset(messages.Message):
	
	key = messages.MessageField(ModelKey, 1)
	name = messages.StringField(2)
	filename = messages.StringField(3)
	size = messages.IntegerField(4)
	mime_type = messages.StringField(5)
	href = messages.StringField(6)
	asset_type = messages.MessageField(AssetType, 7)
	version = messages.IntegerField(8)


class ContentItemResponse(messages.Message):

	key = messages.MessageField(ModelKey, 1)
	repository = messages.MessageField(Repository, 2)
	category = messages.MessageField(ContentItemCategory, 3)
	title = messages.StringField(3)
	description = messages.StringField(4)
	status = messages.StringField(5)
	type = messages.MessageField(ContentItemType, 6)
	format = messages.MessageField(ContentItemFormat, 7)
	tags = messages.MessageField(ContentItemTag, 8, repeated=True)
	category = messages.MessageField(ContentItemCategory, 9)
	like_count = messages.IntegerField(10)
	comment_count = messages.IntegerField(11)
	view_count = messages.IntegerField(12)


class ContentItemListResponse(messages.Message):

	resultset = messages.MessageField(ResultSetMeta, 1)
	timestamp = messages.StringField(2)
	content_items = messages.MessageField(ContentItemResponse, 3, repeated=True)
	datagrid = messages.MessageField(DatagridMeta, 4)


class ContentItemQuerySort(messages.Message):
	pass


class ContentItemQueryFilter(messages.Message):
	pass
	
	
class ContentItemQueryRequest(messages.Message):
	pass
	
	
class ContentItemsByFragmentRequest(messages.Message):

	user = messages.StringField(1)
	type = messages.StringField(2)
	format = messages.StringField(3)
	category = messages.StringField(4)
	repository = messages.StringField(5)
	options = messages.MessageField(QueryMeta, 6)
	

class ContentItemsListRequest(messages.Message):
	
	options = messages.MessageField(QueryMeta, 1)	