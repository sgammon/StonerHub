#!/usr/bin/env python

"""Sample remote_api appengine_config for copying datastore across apps.

For more information, see
http://code.google.com/appengine/docs/adminconsole/

Note that this appengine_config.py file is the same one that you would
use for appstats; if you are bundling this with your existing app you may
wish to copy the version from
google/appengine/ext/appstats/sample_appenigne_config.py instead.
"""

#########################################
# Remote_API Authentication configuration.
#
# See google/appengine/ext/remote_api/handler.py for more information.
# For datastore_admin datastore copy, you should set the source appid
# value.  'HTTP_X_APPENGINE_INBOUND_APPID', ['trusted source appid here']
#
remoteapi_CUSTOM_ENVIRONMENT_AUTHENTICATION = (
    'HTTP_X_APPENGINE_INBOUND_APPID', ['wirestone-spi'])

import bootstrap
bootstrap.AppBootstrapper.prepareImports()