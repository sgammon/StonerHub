{% macro render_page_object(services, config, util, userapi=none) %}

$(document).ready(function (){

	{% for service, action, cfg, opts in services %}
		$.apptools.api.rpc.factory('{{ service }}', '{{ action }}', [{% for method in cfg.methods %}'{{ method }}',{% endfor %}], {% autoescape false %}{{ util.converters.json.dumps(opts) }}{% endautoescape %});
	{% endfor %}

	$.apptools.events.triggerEvent('API_READY');

	{% if userapi != none %}
		// Initliaze user object
		$.apptools.user.setUserInfo({

			{% if userapi.current_user() != none %}
				current_user: "{{ userapi.current_user() }}",
				is_user_admin: {{ util.converters.json.dumps(userapi.is_current_user_admin()) }},
			{% else %}
				current_user: null,
				is_user_admin: false,
			{% endif %}
			login_url: "{{ userapi.create_login_url('/') }}",
			logout_url: "{{ userapi.create_logout_url('/') }}"

		});
	{% endif %}
	// Initialize Sys Object
	_PLATFORM_VERSION = "{{ sys.version }}";

	{% if sys.debug %}
		$.apptools.dev.setDebug({logging: true, eventlog: true, verbose: true});
	{% endif %}	
	
});
{% endmacro %}