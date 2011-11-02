from google.appengine.ext import db
from google.appengine.api.labs import taskqueue

from project.models import SPIModel
from project.models import SPIPolyModel
from project.models import SPIExpandoModel

from project.models.ticket import SystemTicket


class Worker(SPIModel):
	
	''' Describes a queue/cron/queue+cron worker, with accompanying controller. '''

	## Key Name = name.lower().replace(' ', '-')
	
	name = db.StringProperty()
	description = db.TextProperty()
	queue_name = db.StringProperty()
	controller_endpoint = db.StringProperty()
	enabled = db.BooleanProperty(default=False)	
	
	
class WorkerTaskType(SPIPolyModel):
	
	''' Describes a type of task a worker can do. '''

	## Parent = Worker
	## Key Name = name.lower().replace(' ', '-')
	
	name = db.StringProperty()
	description = db.TextProperty()
	endpoint = db.StringProperty()
	endpoint_args = db.StringListProperty(indexed=False)
	enabled = db.BooleanProperty(default=False)	
	worker = db.ReferenceProperty(Worker, collection_name='task_types')	

	task_args = db.StringListProperty()
	
	
class EntityTaskType(WorkerTaskType):
	pass
	
	
class PerPropertyTaskType(WorkerTaskType):
	pass
	
	
class SpecialPropertyTaskType(WorkerTaskType):
	property_name = db.StringProperty()
	

class WorkerJobType(SPIModel):
	
	''' Describes a set of TaskTypes for a particular type of job. '''
	
	## Parent = Worker
	## Key Name = short name
	
	name = db.StringProperty()
	description = db.TextProperty()
	task_length = db.IntegerProperty()
	task_types = db.ListProperty(db.Key)
	
	
class WorkerJob(SystemTicket):
	
	''' Describes a single job that is assigned to a worker and processed until completion or fatal error. '''

	## Parent = Worker
	
	job_start = db.DateTimeProperty(default=None)
	job_finish = db.DateTimeProperty(default=None)	
	worker = db.ReferenceProperty(Worker, collection_name='jobs')
	job_type = db.ReferenceProperty(WorkerJobType, collection_name='jobs')
	
	queued_tasks = db.ListProperty(db.Key)
	queued_count = db.IntegerProperty(default=0)
	
	completed_tasks = db.ListProperty(db.Key)
	completed_count = db.IntegerProperty(default=0)
	
	
class EntityBasedWorkerJob(WorkerJob):
	
	''' Sub-class of a WorkerJob that has an entity attached to it for whatever job is taking place. '''
	
	subject_entity = db.StringProperty()
	model_impl_class = db.StringProperty()
	
	
class WorkerTask(SPIExpandoModel):
	
	''' Describes a task in a WorkerJob that will be inserted into a task queue and processed. '''
	
	## Parent = WorkerJob
	## ID = Used as sequential ordering of job tasks
	
	## Task Properties
	task_url = db.StringProperty()
	task_job = db.ReferenceProperty(WorkerJob, collection_name='tasks')
	task_type = db.ReferenceProperty(WorkerTaskType, collection_name='tasks')
	task_status = db.StringProperty(choices=['queued','complete','error','skipped'])
	subject_entity = db.StringProperty(default=None)
	
	## Audit Properties
	task_start = db.DateTimeProperty(default=None)
	task_finish = db.DateTimeProperty(default=None)
	
	def getTaskqueueTask(self, entity=None):
		if entity is not None:
			return taskqueue.Task(url=self.task_url, headers={'X-SPI-JobKey':str(self.task_job.key()), 'X-SPI-JobType':str(self.task_type.key()), 'X-SPI-Model-Path':entity._getModelPath('.')}, params={'SPI-Task-Key':str(self.key()), 'SPI-Subject-Entity':str(self.subject_entity)})
		else:
			return taskqueue.Task(url=self.task_url, name=self.subject_entity, headers={'X-SPI-JobKey':str(self.task_job.key()), 'X-SPI-JobType':str(self.task_type.key()), 'X-SPI-Model-Path':None}, params={'SPI-Task-Key':str(self.key()), 'SPI-Subject-Entity':str(self.subject_entity)})
			
			
class WorkerPipeline(SPIExpandoModel):
	
	''' Describes a task in a WorkerJob that will be queued and processed as a pipeline. '''
	
	## Task Properties
	pass