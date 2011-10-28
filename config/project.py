# -*- coding: utf-8 -*-
""" 

	######################################## AppTools Project configuration. ########################################

"""
import os
import datetime
config = {}


## App settings
config['apptools.project'] = {

	'name': 'AppTools',

	'version': {
		'major': 4,
		'minor': 0,
		'micro': 0,
		'build': 20111028,
		'release': 'BETA'
	}

}

## Development/debug settings
config['apptools.project.dev'] = {

}

## Output layer settings
config['apptools.project.output'] = { 

	# Output Configuration

	'minify': False, ## whether to minify page output or not
	'optimize': True, ## whether to use the async script loader or not
	'standalone': False, ## whether to render only the current template, or the whole context (ignores "extends")

	'appcache': { ## HTML5 appcaching
		'enable': False, ## whether to enable
		'manifest': 'scaffolding-v1.appcache' ## manifest to link to
	},

	'assets':{
		'minified': False, ## whether to switch to minified assets or not
		'serving_mode': 'local', ## 'local' or 'cdn' (CDN prefixes all assets with an absolute URL)
		'cdn_prefix': [] ## CDN prefix/prefixes - a string is used globally, a list of hostnames is selected from randomly for each asset
	}

}

## Caching
config['apptools.project.cache'] = {

	# Caching Configuration

	'key_seperator': '::',
	'prefix': 'dev',
	'prefix_mode': 'explicit',
	'prefix_namespace': False,
	'namespace_seperator': '::',
	
	'adapters': {

		# Instance Memory
		'fastcache': {

			'default_ttl': 600
	
		},
		
		# Memcache API
		'memcache': {

			'default_ttl': 10800
		
		}, 
		
		# Backend Instance Memory
		'backend': {

			'default_ttl': 10800

		},
		
		# Datastore Caching
		'datastore': {

			'default_ttl': 86400
		
		}
			
	}

}

config['apptools.project.output.template_loader'] = {

	# Template Loader Config

	'force': True, ## Force enable template loader even on Dev server
	'debug': False,  ## Enable dev logging
	'use_memory_cache': False, ## Use handler in-memory cache for template source
	'use_memcache': False, ## Use Memcache API for template source

}

# Pipelines Configuration
config['apptools.project.pipelines'] = {

    'debug': False, # Enable basic serverlogs
	'logging': {
	
		'enable': False, # Enable the pipeline logging subsystem
		'mode': 'serverlogs', # 'serverlogs', 'xmpp' or 'channel'
		'channel': '', # Default channel to send to (admin channels are their email addresses, this can be overridden on a per-pipeline basis in the dev console)
		'jid': '', # Default XMPP JID to send to (this can be overridden on a per-pipeline basis in the dev console)
	
	}

}

# Env Configuration
config['wirestone.spi.env'] = {

	'platform': {
	
		'dev': True if os.environ['SERVER_SOFTWARE'].startswith('Dev') else False
	
	}

}

# Internal System Configuration
config['wirestone.spi.system'] = {

	# Profiling
	'enable_profiler': False,

	# Hooks
	'enable_hooks': False,
	'enable_hook_logging': False,
	'hooks': [
		## Name/Path/Enable
		('debug', 'wirestone.spi.core.hooks.debug.DebugLoggerPatches', False),
		('caching', 'wirestone.spi.core.hooks.caching.CachingShim', False)
	
	]

}

# Dev Configuration
config['wirestone.spi.dev'] = {

    'debug': True,  ## General debug features like Werkzeug and killswitch for param dumps
	'dev_mode': True, ## Appends version to title, enables values below
    'debug_markup': False, ## Enable output of HTML comments for easy debugging    
    'force_append_dev_footer': False,  ## Force appending a tiny dev footer with request and env stuff
    'request_logging': False,  ## Whether to enable general logging in request handlers

}

# Debug Configuration
config['wirestone.spi.debug'] = {

	'datastore':{
		'runtime_stats':False,
		'runtime_logging':False
	},
	'memcache':{
		'runtime_logging':False
	},
	'channel':{
		'runtime_logging':False
	}

}

# Data/Modeling Configuration
config['wirestone.spi.data'] = {

	'repo_by_reference': True, ## Sets a content item's repo by reference
	'repo_by_parent': False, ## Sets a content item's repo by parent-child
	'repo_by_namespace': False ## Sets a content item's repo by namespace

}

# API Configuration
config['wirestone.spi.api'] = {

	'debug': False, ## Turns on debug logging for the API dispatcher and API requests
	'use_backend': False,
	'backend_name': 'api',
	
	'webcache': {
		'enable': False,
		'use_backend': False,
		'backend_name': 'webcache'
	}

}

# Data API Configuration
config['wirestone.spi.api.data'] = {

	'query_caching':{
		'enable':True,
		'log_cache_rpcs':False,
		'ttl':500
	},

}

# Pipelines Configuration
config['wirestone.spi.pipelines'] = {

    'debug': False

}

# Auth Configuration
config['wirestone.spi.auth'] = {
	
	'debug': False,
	'ticket_lifetime': datetime.timedelta(hours=6),
	'enable_federated_logon': False
	
}

config['wirestone.spi.auth.openid'] = {

	'endpoint': 'http://webstaging.wirestone.com/AssetsAuth/openid-mvc/Default.aspx',
	'logout_url': 'http://webstaging.wirestone.com/AssetsAuth/openid-mvc/Account/LogOff'

}

# Security Configuration
config['wirestone.spi.security'] = {

	'sysadmins_only': False,  ## Only allow in appengine-defined sysadmins ## DEPREACATED @TODO
    'check_repo_permissions': False  ## Whether to perform checks on use repo access permissions.

}

# Output Configuration
config['wirestone.spi.output'] = {

    'enable_rest_api': False,  ## Whether to enable the REST api for endpoints that lead to models
	'enable_appcache': False, ## Whether or not to enable appcache features
	'appcache_location': '/staging-v1.1.manifest'

}

# jQuery Configuration
config['wirestone.spi.output.jquery'] = {

	'source': 'local', ## 'local' or 'web' (fetches from Google's CDN)
	'mode': 'production', ## 'production' or 'dev' for uncompressed/compressed code

	'ui': {
		'enable': True,
		'source': 'local',
		'mode': 'production',
		'theme': 'smoothness'
	},
	
	'mobile': {
		'enable': True,
		'mode': 'development'
	}

}

# Social Configuration
config['wirestone.spi.social'] = {

	'enable_ajax_logging':False,
	
	## Default notification settings
	'default_notifications': {
	
		## Configuration for Comments
		'Comment': {
			
			## Notify creator of ContentItem
			'creator': {
				'enabled': True,
				'notify':['email', 'web', 'xmpp']
			},
			
			## Notify editor of ContentItem
			'editor': {
				'enabled': True,
				'notify':['email', 'web', 'xmpp']
			},
			
			## Notify sibling commentors
			'sibling': {
				'enabled': True,
				'notify':['email', 'web', 'xmpp']
			}
		
		},
		
		
		## Configuration for Likes
		'Like': {
			
			## Notify creator of ContentItem
			'creator': {
				'enabled': True,
				'notify':['web', 'xmpp']
			},
			
			## Notify editor of ContentItem
			'editor': {
				'enabled': False,
				'notify':['web', 'xmpp']
			},
			
			## Notify sibling origin users
			'sibling': {
				'enabled': False,
				'notify': ['web', 'xmpp']
			}
		
		},
		
		
		## Configuration for Shares
		'Share': {
		
			## Do not notify creator of ContentItem
			'creator': {
				'enabled': False
			},
			
			## Do not notify editor of ContentItem
			'editor': {
				'enabled': False
			},
			
			## Do not notify siblings
			'editor': {
				'enabled': False
			}
		
		}		
	
	}

}

## Notifications
config['wirestone.spi.notifications'] = {

	'types':['email','xmpp'],
	
	'make_channel': False,

	'email':{
		'enabled': True,

		'config':{
			'sender': 'Wirestone <social@wirestone-spi.appspotmail.com>',
		}
	},
	
	'xmpp':{
		'enabled': False,

		'config':{
			'name': 'Wirestone UCR',
		}
	}

}

config['wirestone.spi.output.request_handler'] = {

	'dependencies':
	{
		'packages':{
		
			'main': {'enabled':True,'module': 'wirestone.spi.handlers.ext.main.Main'},
			'forms': {'enabled':True,'module': 'wirestone.spi.handlers.ext.main.Forms'},			
			'social': {'enabled':True,'module': 'wirestone.spi.handlers.ext.main.Social'},
			'spinewsfeed': {'enabled': True, 'module': 'wirestone.spi.handlers.ext.main.Newsfeed'},				
			'jquery':{'enabled':True,'module':'wirestone.spi.handlers.ext.jquery.jQuery'},
			'plupload':{'enabled':True,'module':'wirestone.spi.handlers.ext.plupload.Plupload'},
			'tracking':{'enabled':True,'module':'wirestone.spi.handlers.ext.tracking.GoogleAnalytics'},
			'datagrid':{'enabled':True,'module':'wirestone.spi.handlers.ext.datagrid.DataGrid'},
			'fancybox':{'enabled':True,'module':'wirestone.spi.handlers.ext.fancybox.Fancybox'},
			'spisearch':{'enabled':True,'module':'wirestone.spi.handlers.ext.spisearch.Search'},
			'markitup':{'enabled':True,'module':'wirestone.spi.handlers.ext.markitup.MarkItUp'},
			'fonts':{'enabled':True,'module':'wirestone.spi.handlers.ext.googlefonts.GoogleFonts'},
			'autocomplete':{'enabled':True,'module':'wirestone.spi.handlers.ext.autocomplete.AutoComplete'},
			'jcrop':{'enabled':True,'module':'wirestone.spi.handlers.ext.jcrop.JCrop'},
		
		},
		
		'always_include':['main','fonts','jquery','forms','datagrid','social', 'tracking']
	}

}

config['wirestone.spi.output.template_loader'] = {

    'debug': False,  ## Enable dev logging
	'use_memory_cache': False, ## Use handler in-memory cache for template bytecode
	'use_memcache': False, ## Use Memcache API for template bytecode

}

# Template Stuff: Superbar
config['wirestone.spi.output.elements.superbar'] = {

	'navigation': [
	
		{'label': 'Home',
			'endpoint': 'landing',
			'title': 'System home page (all repositories).',
			'subnav':False},
		
		{'label': 'Upload',
			'endpoint': 'content-create',
			'title': 'System home page (all repositories).',
			'subnav':False},
			
		{'label': 'Search',
			'endpoint': 'search-global',
			'title': 'System home page (all repositories).',
			'subnav':False},
			
		{'label': 'Repositories',
			'endpoint': 'repository-list',
			'title': 'System home page (all repositories).',
			'subnav':False}, ## Automagically replaced with a list or repositories for subnav											

		{'label': 'Content',
			'endpoint': 'content-global',
			'title': 'Content summary page (all repositories).',
			'subnav':[
			
				{'label': 'All Repositories',
					'endpoint': 'content-all',
					'title': 'All content (all repositories).'},
					
				{'label': 'Recent Content',
					'endpoint': 'content-recent',
					'title': 'Recent content (all repositories).'},
					
				{'label': 'My Content',
					'endpoint':'content-mine',
					'title': 'Content I\'ve uploaded (all repositories).'}
			
			
			]},

		{'label': 'Tags',
			'endpoint': 'tags-global',
			'title': 'System home page (all repositories).',
			'subnav':[
			
				{'label': 'All Tags',
					'endpoint': 'tags-all',
					'title': 'All tags (all repositories).'},
					
				{'label': 'Popular Tags',
					'endpoint': 'tags-popular',
					'title': 'Popular tags (all repositories).'},
					
				{'label': 'My Tags',
					'endpoint':'tags-mine',
					'title': 'Tags I\'ve used (all repositories).'}
			
			
		]}
	]

}

# Configuration for polymodel
config['wirestone.spi.datamodel.polymodel'] = {

	'class_property_name':'_class_',
	'path_property_name':'_path_'

}

# Configuration for system+user tickets
config['wirestone.spi.datamodel.ticket'] = {

	'default_lifetime': datetime.timedelta(hours=8),
	
}

# Configuration for indexer entities
config['wirestone.spi.datamodel.indexer'] = {

	'mappings':{
		'IndexMapping':{'map_limit':50},
		'CIIndexMapping':{'map_limit':50},
		'SAIndexMapping':{'map_limit':100}
	}
	
}

# Configuration for repository handling
config['wirestone.spi.datamodel.repository'] = {

	'max_repositories':25

}

# Configuration for content item handling
config['wirestone.spi.datamodel.content_item'] = {

	'extensions':
	{
		'_default_': 'file.html',
		'document': 'document.html',
		'presentation': 'presentation.html',		
		'image': 'image.html',
		'video': 'video.html'
	}

}

# Ticket worker
config['wirestone.spi.workers.ticketManager'] = {

	'debug': False

}


# Indexer
config['wirestone.spi.indexer'] = {

	'debug': False,
	'use_backend': False,
	'backend_name': 'indexer'

}

config['wirestone.spi.workers.indexer'] = {
	
	'debug':False,
	'autoqueue':True

}

# Counters
config['wirestone.spi.counters'] = {

	'default_shards': 8

}

# Analytics Tracking
config['wirestone.spi.tracking'] = {

	'enable_analytics': True,
	'google_analytics_account': 'UA-2908422-23'

}

# Search
config['wirestone.spi.search'] = {

	'minimum_term_length': 3,

	'caching': {
		'result_set_ttl': 360 ## datastore-backed search caching time-to-live (default:360)
	},
	
	'results':{
		'show_tags': True
	},
	
	'cut_words': ["'s"],
	
	'stop_words': ['a','able','about','across','after','all','almost','also','am','among',
				   'an','and','any','are','as','at','be','because','been','but','by','can',
				   'cannot','could','dear','did','do','does','either','else','ever','every',
				   'for','from','get','got','had','has','have','he','her','hers','him','his',
				   'how','however','i','if','in','into','is','it','its','just','least','let',
				   'like','likely','may','me','might','most','must','my','neither','no','nor',
				   'not','of','off','often','on','only','or','other','our','own','rather',
				   'said','say','says','she','should','since','so','some','than','that','the',
				   'their','them','then','there','these','they','this','tis','to','too',
				   'twas','us','wants','was','we','were','what','when','where','which',
				   'while','who','whom','why','will','with','would','yet','you','your']

}