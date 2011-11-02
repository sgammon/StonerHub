# -*- coding: utf-8 -*-
from config import config
from webapp2 import import_string


def get_rules():
    """Returns a list of URL rules for the application. The list can be
    defined entirely here or in separate ``urls.py`` files.

    :param app:
        The WSGI application instance.
    :return:
        A list of class:`webapp2.Route` instances.
    """
    #  Here we show an example of joining all rules from the
    # ``apps_installed`` definition set in config.py.
    rules = []

    for app_module in config.get('webapp2')['apps_installed']:
        try:
            # Load the urls module from the app and extend our rules.
            app_rules = import_string('%s.routing' % app_module)
            rules.extend(app_rules.get_rules())
        except ImportError:
            pass

    return rules