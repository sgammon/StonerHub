from protorpc import messages

class ModelKey(messages.Message):
	
	value = messages.StringField(1)
	kind = messages.StringField(2)
	name = messages.StringField(3)
	id = messages.IntegerField(4)
	parent = messages.StringField(5)


class ModelProperty(messages.Message):
	
	name = messages.StringField(1)
	type = messages.StringField(2)
	label = messages.StringField(3)
	
	
class ModelProto(messages.Message):
	
	kind = messages.StringField(1)
	properties  = messages.MessageField(ModelProperty, 2, repeated=True)


class ResultSetMeta(messages.Message):
	
	results_count = messages.IntegerField(1)
	returned_count = messages.IntegerField(2)
	cursor = messages.StringField(3)
	freshness = messages.StringField(4)
	

class QueryMeta(messages.Message):
	
	limit = messages.IntegerField(1, default=15)
	page = messages.IntegerField(2, default=1)
	offset = messages.IntegerField(3, default=0)
		
	
class DatagridMeta(messages.Message):
	
	columns = messages.StringField(1, repeated=True)
	model_schema = messages.MessageField(ModelProto, 2)
	rpc_fields = messages.StringField(3)