import inspect
import logging
from google.appengine.ext import db

from project.models.assets import AssetType
from project.models.system import _SystemProperty_

from project.models.content import Repository
from project.models.content import ContentItemType
from project.models.content import ContentItemFormat
from project.models.content import ContentItemCategory

from project.models.worker import Worker
from project.models.worker import WorkerJobType
from project.models.worker import WorkerTaskType

from project.models.worker import EntityTaskType
from project.models.worker import PerPropertyTaskType
from project.models.worker import SpecialPropertyTaskType

from project.models.worker.indexer import IndexerJob

from project.models.security import SecurityRole
from project.models.security import SecurityGroup
from project.models.security import User as WirestoneUser


def makeProperty(prototype, name, p_type):

	from project.models.proto import Property
	
	#PropImplClass = type(str(p_type.__class__.__name__.split('.')[-1]), (Property,), {})
	#return PropImplClass(prototype, key_name=name, name=name, type=str(p_type.__class__.__name__.split('.')[-1]))
	return Property(prototype, key_name=name, name=name, type=str(p_type.__class__.__name__.split('.')[-1]))


def add_prototypes():
	
	from project.models import _proto_
	from project.models import SPIModel
	from project.models import SPIPolyModel

	from project.models.proto import Property
	from project.models.proto import Prototype
	
	models = []
	properties = []
	
	logging.info('Making prototypes for _proto_ list: '+str(_proto_))
	m = __import__('project.models', globals(), locals(), _proto_)
	
	for proto_module in _proto_:
		submodule = getattr(m, proto_module)
		for artifact in dir(submodule):
			
			if artifact == 'SPIModel' or artifact == 'SPIPolyModel':
				continue
			else:
			
				logging.info('---Found artifact "'+str(artifact)+'"...')
				obj = getattr(submodule, artifact)
				if inspect.isclass(obj):
					logging.info('------Artifact is a CLASS.')
					if issubclass(obj, SPIModel):
						logging.info('------Requirements met. Creating Prototype.')
						if issubclass(obj, SPIPolyModel):
							proto = Prototype(key_name=obj.class_name(), kind_name=obj.kind(), description=str(obj.__doc__).rstrip().lstrip(), path=obj._getModelPath(), classpath=obj._getClassPath(), property_names=obj.properties().keys(), property_types=[str(pt.__class__.__name__) for pt in obj.properties().values()])
							models.append(proto)
						else:
							proto = Prototype(key_name=obj.kind(), kind_name=obj.kind(), description=str(obj.__doc__).rstrip().lstrip(), path=obj._getModelPath(), classpath=obj._getClassPath(), property_names=obj.properties().keys(), property_types=[str(pt.__class__.__name__) for pt in obj.properties().values()])
							models.append(proto)
						
						for prop_name, prop_class in obj.properties().items():
							if prop_name not in ['_class', '_path', '_class_', '_path_']:
								properties.append(makeProperty(proto, prop_name, prop_class))
						
	return db.put(models+properties)


def add_default_asset_types():
	
	assets = []
	
	assets.append(AssetType(key_name='image', name='Image'))
	assets.append(AssetType(key_name='style', name='Stylesheet'))
	assets.append(AssetType(key_name='script', name='Script'))
	
	return db.put(assets)
	
	
def add_default_content_types():
	
	types = []
	
	f = ContentItemType(key_name='file', name='File').put()
	types.append(ContentItemType(f,key_name='drawing', name='Drawing'))
	types.append(ContentItemType(f,key_name='document', name='Document'))
	types.append(ContentItemType(f,key_name='spreadsheet', name='Spreadsheet'))	
	types.append(ContentItemType(f,key_name='presentation', name='Presentation'))	
	types.append(ContentItemType(f,key_name='image', name='Image'))
	types.append(ContentItemType(f,key_name='audio', name='Audio'))
	types.append(ContentItemType(f,key_name='video', name='Video'))
	types.append(ContentItemType(f,key_name='archive', name='Archive'))
	
	return db.put(types)
	
	
def add_default_content_formats():
	
	formats = []
	
	f = ContentItemType.get_by_key_name('file')
	
	## Drawing Formats
	drawing_type = ContentItemType.get_by_key_name('drawing', parent=f)
	formats.append(ContentItemFormat(key_name='application/postscript', name='PS', icon='drawing.png', mime_type=['application/postscript'], valid_extensions=['ai', 'eps', 'ps']))
	formats.append(ContentItemFormat(key_name='application/dxf', name='DXF', icon='drawing.png', mime_type=['application/dxf', 'image/dxf'], valid_extensions=['dxf']))
	formats.append(ContentItemFormat(key_name='font/ttf', name='TTF', icon='font.ttf', mime_type=['font/ttf'], valid_extensions=['ttf']))
	
	## Document Formats
	doc_type = ContentItemType.get_by_key_name('document', parent=f)
	formats.append(ContentItemFormat(key_name='text/plain',name='TXT', type=doc_type, icon='txt.png', mime_type=['text/plain'], valid_extensions=['txt', 'text']))
	formats.append(ContentItemFormat(key_name='application/msword',name='MSWORD', type=doc_type, icon='doc.png', mime_type=['application/msword'], valid_extensions=['doc', 'docx']))
	formats.append(ContentItemFormat(key_name='application/pdf',name='PDF', type=doc_type, icon='pdf.png', mime_type=['application/pdf'], valid_extensions=['pdf']))
	formats.append(ContentItemFormat(key_name='application/x-iwork-pages-sffpages',name='PAGES', type=doc_type, icon='doc.png', mime_type=['application/x-iwork-pages-sffpages'], valid_extensions=['pages']))
	

	## Spreadsheet Formats
	spreadsheet_type = ContentItemType.get_by_key_name('spreadsheet', parent=f)
	formats.append(ContentItemFormat(key_name='application/vnd.ms-excel', name='XLS', type=spreadsheet_type, icon='page_white_excel.png', mime_type=['application/vnd.ms-excel'], valid_extensions=['xls']))
	formats.append(ContentItemFormat(key_name='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', name='XLSX', type=spreadsheet_type, icon='page_white_excel.png', mime_type=['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'], valid_extensions=['xlsx']))

	## Presentation Formats
	pres_type = ContentItemType.get_by_key_name('presentation', parent=f)
	formats.append(ContentItemFormat(key_name='application/vnd.ms-powerpoint',name='Microsoft PowerPoint', type=pres_type, icon='page_white_powerpoint.png', mime_type=['application/vnd.ms-powerpoint'], valid_extensions=['ppt']))
	formats.append(ContentItemFormat(key_name='application/vnd.openxmlformats-officedocument.presentationml.presentation',name='PPT', type=pres_type, icon='page_white_powerpoint.png', mime_type=['application/vnd.ms-powerpoint'], valid_extensions=['pptx']))	
	
	## Image Formats
	img_type = ContentItemType.get_by_key_name('image', parent=f)
	formats.append(ContentItemFormat(key_name='image/gif',name='GIF', type=img_type, icon='gif.png', mime_type=['image/gif'], valid_extensions=['gif']))
	formats.append(ContentItemFormat(key_name='image/png',name='PNG', type=img_type, icon='png.png', mime_type=['image/png'], valid_extensions=['png']))
	formats.append(ContentItemFormat(key_name='image/jpeg',name='JPEG', type=img_type, icon='jpg.png', mime_type=['image/jpeg'], valid_extensions=['jpg', 'jpeg']))	
	formats.append(ContentItemFormat(key_name='image/svg+xml',name='SVG', type=img_type, icon='svg.png', mime_type=['image/svg+xml'], valid_extensions=['svg']))
	
	## Video Formats
	vid_type = ContentItemType.get_by_key_name('video', parent=f)
	formats.append(ContentItemFormat(key_name='video/mpg',name='MPG', type=vid_type, icon='mpg.png', mime_type=['video/mpg'], valid_extensions=['mpg','mpeg']))
	formats.append(ContentItemFormat(key_name='video/x-ms-wmv',name='WMV', type=vid_type, icon='wmv.png', mime_type=['video/x-ms-wmv'], valid_extensions=['wmv']))
	formats.append(ContentItemFormat(key_name='video/x-msvideo',name='AVI', type=vid_type, icon='avi.png', mime_type=['video/x-msvideo'], valid_extensions=['avi']))
	formats.append(ContentItemFormat(key_name='video/quicktime',name='MOV', type=vid_type, icon='mov.png', mime_type=['video/quicktime', 'video/x-quicktime', 'image/mov']))

	## Archive
	archive_type = ContentItemType.get_by_key_name('archive', parent=f)
	formats.append(ContentItemFormat(key_name='application/zip',name='ZIP', type=archive_type, icon='zip.png', mime_type=['application/zip'], valid_extensions=['zip']))
	
	return db.put(formats)
	
	
def add_default_repositories():
	
	repositories = []
	
	repositories.append(Repository(key_name='strategic-insights', name='Strategy & Planning', description='Base repository.'))
	repositories.append(Repository(key_name='system', name='Wirestone UCR', description='Repository for design and test documents for this system.'))
	repositories.append(Repository(key_name='marketing', name='Marketing', description='Base repository.'))
	repositories.append(Repository(key_name='creative', name='Creative', description='Repository for graphic/media assets and other resources for the Creative department.'))
	
	return db.put(repositories)
	
	
def add_default_content_categories():
	
	categories = []
	
	spi = Repository.get_by_key_name('strategic-insights')
	marketing = Repository.get_by_key_name('marketing')
	creative = Repository.get_by_key_name('creative')
	system = Repository.get_by_key_name('system')
	
	# SPI Categories
	categories.append(ContentItemCategory(spi,key_name='3d-television', name='3D Television'))
	categories.append(ContentItemCategory(spi,key_name='ad-networks-ad-servers-ad-exchanges', name='Ad Networks, Ad Servers, & Ad Exchanges'))
	categories.append(ContentItemCategory(spi,key_name='advanced-analytics', name='Advanced Analytics'))
	categories.append(ContentItemCategory(spi,key_name='advertising', name='Advertising'))
	categories.append(ContentItemCategory(spi,key_name='advertising-agencies', name='Advertising Agencies'))
	categories.append(ContentItemCategory(spi,key_name='advertising-technologies', name='Advertising Technologies'))
	categories.append(ContentItemCategory(spi,key_name='application-development', name='Application Development'))
	categories.append(ContentItemCategory(spi,key_name='authentication-authorization-audit', name='Authentication, Authorization, & Audit'))
	categories.append(ContentItemCategory(spi,key_name='behavioral-targeting', name='Behavioral Targeting'))
	categories.append(ContentItemCategory(spi,key_name='blogging-and-blogs', name='Blogging and Blogs'))
	categories.append(ContentItemCategory(spi,key_name='brand-management', name='Brand Management'))
	categories.append(ContentItemCategory(spi,key_name='business-intelligence', name='Business Intelligence'))
	categories.append(ContentItemCategory(spi,key_name='cloud-computing', name='Cloud Computing'))
	categories.append(ContentItemCategory(spi,key_name='community-management', name='Community Management'))
	categories.append(ContentItemCategory(spi,key_name='consumer-behaviors', name='Consumer Behaviors'))
	categories.append(ContentItemCategory(spi,key_name='consumer-experiences', name='Consumer Experiences'))
	categories.append(ContentItemCategory(spi,key_name='content-management-systems', name='Content Management Systems'))
	categories.append(ContentItemCategory(spi,key_name='customer-relationship-management', name='CRM - Customer Relationship Management'))
	categories.append(ContentItemCategory(spi,key_name='crowdsourcing', name='Crowdsourcing'))
	categories.append(ContentItemCategory(spi,key_name='broadcast-television-advertising', name='Broadcast Television/Advertising'))
	categories.append(ContentItemCategory(spi,key_name='data-integration', name='Data Integration'))
	categories.append(ContentItemCategory(spi,key_name='data-mining', name='Data Mining'))
	categories.append(ContentItemCategory(spi,key_name='data-visualization', name='Data Visualization'))
	categories.append(ContentItemCategory(spi,key_name='database-marketing', name='Database Marketing'))
	categories.append(ContentItemCategory(spi,key_name='demand-lead-generation-marketing', name='Demand / Lead Generation Marketing'))
	categories.append(ContentItemCategory(spi,key_name='ecommerce-trends', name='Ecommerce trends'))
	categories.append(ContentItemCategory(spi,key_name='email-marketing', name='Email Marketing'))
	categories.append(ContentItemCategory(spi,key_name='experiential-marketing', name='Experiential Marketing'))
	categories.append(ContentItemCategory(spi,key_name='go-to-market-strategies', name='Go-To-Market Strategies'))
	categories.append(ContentItemCategory(spi,key_name='immersive-experiences', name='Immersive Experiences'))
	categories.append(ContentItemCategory(spi,key_name='industry-trends', name='Industry Trends'))
	categories.append(ContentItemCategory(spi,key_name='information-architecture', name='Information Architecture'))
	categories.append(ContentItemCategory(spi,key_name='interactive-marketing', name='Interactive Marketing'))
	categories.append(ContentItemCategory(spi,key_name='interactive-television', name='Interactive Television'))
	categories.append(ContentItemCategory(spi,key_name='location-based-marketing', name='Location Based Marketing'))
	categories.append(ContentItemCategory(spi,key_name='location-based-services', name='Location Based Services'))
	categories.append(ContentItemCategory(spi,key_name='market-analysis-research', name='Market Analysis & Research'))
	categories.append(ContentItemCategory(spi,key_name='marketing-measurement', name='Marketing Measurement Methods & Techniques'))
	categories.append(ContentItemCategory(spi,key_name='merchandizing', name='Merchandizing'))
	categories.append(ContentItemCategory(spi,key_name='mobile-advertising', name='Mobile Advertising'))
	categories.append(ContentItemCategory(spi,key_name='mobile-applications', name='Mobile Applications'))
	categories.append(ContentItemCategory(spi,key_name='mobile-commerce', name='Mobile Commerce'))
	categories.append(ContentItemCategory(spi,key_name='mobile-marketing', name='Mobile Marketing'))
	categories.append(ContentItemCategory(spi,key_name='mobile-web', name='Mobile Web'))
	categories.append(ContentItemCategory(spi,key_name='online-advertising', name='Online Advertising'))
	categories.append(ContentItemCategory(spi,key_name='operating-systems-software', name='Operating Systems & Software'))
	categories.append(ContentItemCategory(spi,key_name='personalization', name='Personalization'))
	categories.append(ContentItemCategory(spi,key_name='porsonas-persona-development', name='Personas & Persona Development'))
	categories.append(ContentItemCategory(spi,key_name='public-relations', name='Public Relations'))
	categories.append(ContentItemCategory(spi,key_name='retail-experiences-offline', name='Retail Experiences: Offline'))
	categories.append(ContentItemCategory(spi,key_name='retail-marketing-offline', name='Retail Marketing: Offline'))
	categories.append(ContentItemCategory(spi,key_name='rss-feeds', name='RSS Feeds'))
	categories.append(ContentItemCategory(spi,key_name='search-marketing-ppx', name='Search Engine Marketing - PPC'))
	categories.append(ContentItemCategory(spi,key_name='search-marketing-seo', name='Search Engine Marketing - SEO'))
	categories.append(ContentItemCategory(spi,key_name='search-seo', name='Search Engine Optimization'))
	categories.append(ContentItemCategory(spi,key_name='social-brand-management', name='Social Brand Reputation Management'))
	categories.append(ContentItemCategory(spi,key_name='social-channel-integration', name='Social Channel Integration'))
	categories.append(ContentItemCategory(spi,key_name='social-commerce', name='Social Commerce'))
	categories.append(ContentItemCategory(spi,key_name='social-gaming', name='Social Gaming'))
	categories.append(ContentItemCategory(spi,key_name='social-media-marketing', name='Social Media & Marketing'))
	categories.append(ContentItemCategory(spi,key_name='social-networking', name='Social Networking'))
	categories.append(ContentItemCategory(spi,key_name='strategic-insight-development', name='Strategic Insight Development'))
	categories.append(ContentItemCategory(spi,key_name='surveys', name='Surveys'))
	categories.append(ContentItemCategory(spi,key_name='tech', name='Tech'))
	categories.append(ContentItemCategory(spi,key_name='television-advertising', name='Television & Advertising'))
	categories.append(ContentItemCategory(spi,key_name='testing-and-targeting', name='Testing & Targeting'))
	categories.append(ContentItemCategory(spi,key_name='usability-and-ux', name='Usability & UX'))
	categories.append(ContentItemCategory(spi,key_name='user-experience-design', name='User Experience Design'))
	categories.append(ContentItemCategory(spi,key_name='user-interaction-design', name='User Interaction Design'))
	categories.append(ContentItemCategory(spi,key_name='web-site-analytics', name='Web Site Analytics'))
	categories.append(ContentItemCategory(spi,key_name='word-of-mouth-marketing', name='Word of Mouth Marketing'))
	
	# Marketing Categories
	categories.append(ContentItemCategory(marketing,key_name='rfp-responses', name='RFP Responses'))
	categories.append(ContentItemCategory(marketing,key_name='rfi-responses', name='RFI Responses'))
	categories.append(ContentItemCategory(marketing,key_name='capabilities', name='Meet Wirestone (Capabilities)'))
	categories.append(ContentItemCategory(marketing,key_name='proposals', name='Proposals'))
	categories.append(ContentItemCategory(marketing,key_name='sow', name='SOWs'))
	categories.append(ContentItemCategory(marketing,key_name='solution-briefs', name='Solution Briefs'))
	categories.append(ContentItemCategory(marketing,key_name='templates', name='Templates'))	
	
	# Creative Categories
	categories.append(ContentItemCategory(creative,key_name='graphics', name='Graphics'))
	categories.append(ContentItemCategory(creative,key_name='photography', name='Still Photography'))
	categories.append(ContentItemCategory(creative,key_name='video', name='Video'))
	categories.append(ContentItemCategory(creative,key_name='animation', name='Animation'))
	
	# System Categories
	categories.append(ContentItemCategory(system, key_name='test', name='Test Content'))
	categories.append(ContentItemCategory(system, key_name='documentation', name='Documentation'))

	
	return db.put(categories)
					
					
def add_dev_users():

	users = []
	users.append(_SystemProperty_(key_name='root_admins', name='root_admins', value=['sam.gammon','neil.michel','scott.doniger','mike.higgins']))
	return db.put(users)
	
	
def add_default_security_roles():

	roles = []
	
	roles.append(SecurityRole(key_name='sysadmin',name='System Administrator',description='Highest-level system administrator.'))
	roles.append(SecurityRole(key_name='developer',name='System Developer',description='Gives a user development console priviliges.'))
	roles.append(SecurityRole(key_name='content_admin',name='Content Administrator',description='Administrator of content - all priviliges related to content data Create/Update/Read/Delete.'))
	roles.append(SecurityRole(key_name='content_moderator',name='Content Moderator',description='Moderator of content - delete, edit, etc priviliges for content items.'))	
	
	return db.put(roles)
	
	
def add_default_security_groups():
	pass
	
		
def add_default_office_locations():
	
	from project.models.org import OfficeLocation
	
	locations = []
	locations.append(OfficeLocation(key_name='[wire] stone Sacramento', address='920 20th St., Sacramento, CA 95811'))
	locations.append(OfficeLocation(key_name='[wire] stone Boise', address='913 W. River Street, Suite 200, Boise, ID 83702', phone='(208) 343-2868'))
	locations.append(OfficeLocation(key_name='[wire] stone Chicago', address='225 W. Illinois, Suite 400, Chicago, IL 60654', phone='(312) 222-0733'))
	locations.append(OfficeLocation(key_name='[wire] stone Fort Collins', address='1235 River Side Avenue, Fort Colins, CO 80525', phone='(970) 493-3181'))
	locations.append(OfficeLocation(key_name='[wire] stone San Diego', address='312 S Cedros Avenue, Suite 340, Solana Beach, CA 92075-1971', phone='(858) 509-1125'))
	locations.append(OfficeLocation(key_name='[wire] stone Seattle', address='8809 148th Ave. NE, Redmond, WA 98052', phone='(208) 761-0986'))
	
	return db.put(locations)
		

## Map all function to an array to easily iterate through...
all_functions = [add_default_asset_types, add_default_content_types, add_default_content_formats, add_default_repositories, add_default_content_categories, add_dev_users, add_default_security_roles, add_default_security_groups, add_default_office_locations] # add_prototypes,