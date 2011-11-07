# -*- coding: utf-8 -*-
"""

	###################################### Asset configuration. ######################################


"""
config = {}


# Installed Assets
config['apptools.project.assets'] = {

	'debug': False, ## Output log messages about what's going on.
	'verbose': False, ## Raise debug-level messages to 'info'.

	# JavaScript Libraries & Includes
	'js': {


		### Core Dependencies ###
		('core', 'core'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'dependencies.bundle.min.js'
			},
			
			'assets': {
				'backbone': {'min': True, 'version': '0.5.2'}, # Backbone.JS - site MVC core
				'amplify': {'min': True, 'version': '1.0.0'}, # AmplifyJS - for request, local storage + pubsub management
				'modernizr': {'min': True, 'version': '2.0'}, # Modernizr - browser polyfill + compatibility testing
				'lawnchair': {'min': True, 'version': '0.6.3'}, # Lawnchair: Client-side persistent storage
				'underscore': {'min': True, 'version': '1.2.1'}, # Underscore: JavaScript's utility belt
			}
		
		},
		
		### AppTools Platform Scripts ###
		('apptools', 'apptools'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'core.bundle.min.js'
			},

			'assets': {
				'base': {'min': True, 'version': 0.1}, # apptools base, rpc, events, dev, etc (accessible at window.apptools)
			}
	
		},
		
		### StonerHub Project Scripts ###
		('stonerhub', 'stonerhub'): {
		
			'config': {
				'version_mode': 'getvar',
				'bundle': 'stonerhub.bundle.min.js',
				'min': True
			},
			
			'assets': {
				'main': {'name': 'app', 'version': '0.1'}, # all of stonerhub's js, written in coffeescript :)
			}
		
		},
		
		### Browser feature Polyfills ###
		('polyfills', 'core/polyfills'): { 

			'config': {
				'version_mode': 'getvar',
				'bundle': 'polyfills.bundle.min.js'
			},
			
			'assets': {
				'json2': {'min': True}, # Adds JSON support to old IE and others that don't natively support it
				'history': {'min': True} # Adds support for history management to old browsers
			}

		},
		
		### jQuery Core ###
		('jquery', 'jquery'): { 
		
			'config': {
				'version_mode': 'getvar',				
				'bundle': 'jquery.bundle.min.js'
			},
			
			'assets': {
				'core': {'name': 'jquery', 'min': True, 'version': '1.7'}, # jQuery Core
				'ui': {'name': 'jquery.ui', 'min': True, 'version': '1.8.9'} # jQuery UI
			}
			
		},
		
		### jQuery Plugins ###
		('jquery-plugins', 'jquery/plugins'): {
		
			'config': {
				'version_mode': 'getvar',
				'bundle': 'jquery.ui.bundle.min.js',
				'min': True
			},
			
			'assets': {
				'jcrop': {'name': 'jquery.jcrop', 'version': '0.9.8'}, # jCrop - plugin for cropping images inline
				'tipsy': {'name': 'jquery.tipsy', 'version': '1.0.0a'}, # Tipsy - facebook-like tooltips
				'facelist': {'name': 'jquery.facelist', 'version': '2.0'}, # Facelist - facebook-like autocomplete
				'fancybox': {'name': 'jquery.fancybox', 'version': '1.3.4'}, # Fancybox - pretty lightbox dialogs
				'jeditable': {'name': 'jquery.jeditable', 'version': '1.0'}, # jEditable - in-place form editing
				'datatables': {'name': 'jquery.datatables', 'version': '1.8.2'} # DataTables - plugin for rendering interactive grids
			}
		
		},
		
		### jQuery Interaction ###
		('jquery-interaction', 'jquery/interaction'): {
		
			'config': {
				'version_mode': 'getvar',
				'bundle': 'jquery.interaction.bundle.min.js',
				'min': True,
				'version': '1.0'
			},
			
			'assets': {
				'autocomplete': {'name': 'jquery.autocomplete', 'min': True, 'version': '1.0'}, # Form Autocomplete
				'cookie': {'name': 'jquery.cookie', 'min': True, 'version': '1.0'}, # JS Cookie access
				'easing': {'name': 'jquery.easing', 'min': True, 'version': '1.0'}, # JS Easing animations
				'highlight': {'name': 'jquery.highlight', 'min': True, 'version': '1.0'}, # Highlight things on the page
				'localscroll': {'name': 'jquery.localscroll', 'min': True, 'version': '1.0'}, # LocalScroll, for scrollers
				'scrollto': {'name': 'jquery.scrollto', 'min': True, 'version': '1.0'}, # ScrollTo - for scrolling to a specific element
				'serialscroll': {'name': 'jquery.serialscroll', 'min': True, 'version': '1.0'}, # SerialScroll - for scrollers
				'mousewheel': {'name': 'jquery.mousewheel', 'min': True, 'version': '1.0'} # jQuery mousewheel ops
			}
		
		},
		
		### Plupload - HTML5 uploader library ###
		('plupload', 'plugins/plupload'): {
		
			'config': {
				'version_mode': 'getvar',
				'bundle': 'plupload.bundle.js',
				'min': True,
				'version': '1.5.1.1'
			},
			
			'assets': {
				# Core Packages
				'core': {'name': 'plupload'}, # core only
				'full': {'name': 'plupload.full'}, # full package
				
				# Runtimes
				'runtime.flash': {'name': 'runtime.flash'}, # flash runtime
				'runtime.gears': {'name': 'runtime.gears'}, # gears runtime
				'runtime.html4': {'name': 'runtime.html4'}, # html4 runtime
				'runtime.html5': {'name': 'runtime.html5'}, # html5 runtime
				'runtime.silverlight': {'name': 'runtime.silverlight'}, # silverlight runtime
				'runtime.browserplus': {'name': 'runtime.browserplus'}, # browserplus runtime
				
				# Uploader Widgets
				'jq_widget': {'name': 'queuewidget.jquery'}, # regular jq widget
				'jqui_widget': {'name': 'queuewidget.jqui'} # jquery-ui widget
			}
		
		},
		
		'belated_png': {'path': 'util/dd_belatedpng.js'} # Belated PNG fix
	
	},


	# Cascading Style Sheets
	'style': {
		
		# Compiled (SASS) FCM Stylesheets
		('compiled', 'compiled'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
		
			'assets': {
				'main': {'version': 0.1}, # reset, main, layout, forms
				'ie': {'version': 0.1}, # fixes for internet explorer (grrr...)
				'print': {'version': 0.1}, # proper format for printing
				'mobile': {'version': 0.1} # proper format for mobile
			}
		
		},
		
		# Content-section specific stylesheets
		('stonerhub', 'compiled/stonerhub'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'main': {'name': 'app', 'version': '1.0'}, # main stonerhub styles (combines main, search, security, social, fonts + forms, newsfeed)
				'security': {'name': 'security', 'version': '1.0'} # security styles (/login, /logout, etc)
			}
		
		},
		
		# Plugins
		('facelist', 'plugins/facelist'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'main': {'name': 'facelist', 'version': '1.0'}, # main facelist styles
				'ie': {'name': 'facelist.ie', 'version': '1.0'}, # ie facelist styles
			}
		
		},
		
		('datagrid', 'plugins/datagrid'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'grid': {'name': 'grid-table', 'version': '1.0'}, # main facelist styles
				'grid-ci': {'name': 'grid-ci', 'version': '1.0'}, # content item grid styles
				'grid-jqui': {'name': 'grid-table-jqui', 'version': '1.0'}, # jquery ui grid styles
			}
		
		},
		
		'fancybox': {'path': 'plugins/fancybox/fancybox.css'},
		'jcrop': {'path': 'plugins/jcrop/jquery.jcrop.css'},
		'tipsy': {'path': 'plugins/tipsy/tipsy.css'},
		
		('jquery-ui', 'themes'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'smoothness': {'name': 'smoothness', 'version': '1.0'} # modified smoothness theme
			}
		
		},
		
		('plupload', 'plugins/plupload'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'queue-widget': {'name': 'queue-widget', 'version': '1.0'}, # queue widget css
				'jqui-widget': {'name': 'queue-ui-widget', 'version': '1.0'} # jqui queue widget css
			}
		
		}
			
	},

	
	# Other Assets
	'ext': {
		
		('plupload', 'plupload'): {
		
			'config': {
				'min': False,
				'version_mode': 'getvar'
			},
			
			'assets': {
			
				'flash': {'name': 'plupload.flash', 'extension': 'swf'},
				'silverlight': {'name': 'plupload.silverlight', 'extension': 'xap'}
			
			}
		
		}
		
	 },
	
}