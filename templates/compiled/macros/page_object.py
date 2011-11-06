from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/page_object.js'

    def root(context, environment=environment):
        if 0: yield None
        def macro(l_services, l_config, l_util, l_userapi):
            t_1 = []
            l_sys = context.resolve('sys')
            pass
            t_1.append(
                u'\n\n$(document).ready(function (){\n\n\t', 
            )
            l_action = l_cfg = l_opts = l_service = missing
            for (l_service, l_action, l_cfg, l_opts) in l_services:
                pass
                t_1.extend((
                    u"\n\t\t$.apptools.api.rpc.factory('", 
                    to_string(l_service), 
                    u"', '", 
                    to_string(l_action), 
                    u"', [", 
                ))
                l_method = missing
                for l_method in environment.getattr(l_cfg, 'methods'):
                    pass
                    t_1.extend((
                        u"'", 
                        to_string(l_method), 
                        u"',", 
                    ))
                l_method = missing
                t_1.append(
                    u'], ', 
                )
                pass
                t_2 = context.eval_ctx.save()
                context.eval_ctx.autoescape = False
                t_1.append(
                    to_string(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), l_opts)), 
                )
                context.eval_ctx.revert(t_2)
                t_1.append(
                    u');\n\t', 
                )
            l_action = l_cfg = l_opts = l_service = missing
            t_1.append(
                u"\n\n\t$.apptools.events.triggerEvent('API_READY');\n\n\t", 
            )
            if l_userapi != None:
                pass
                t_1.append(
                    u'\n\t\t// Initliaze user object\n\t\t$.apptools.user.setUserInfo({\n\n\t\t\t', 
                )
                if context.call(environment.getattr(l_userapi, 'current_user')) != None:
                    pass
                    t_1.extend((
                        u'\n\t\t\t\tcurrent_user: "', 
                        to_string(context.call(environment.getattr(l_userapi, 'current_user'))), 
                        u'",\n\t\t\t\tis_user_admin: ', 
                        to_string(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), context.call(environment.getattr(l_userapi, 'is_current_user_admin')))), 
                        u',\n\t\t\t', 
                    ))
                else:
                    pass
                    t_1.append(
                        u'\n\t\t\t\tcurrent_user: null,\n\t\t\t\tis_user_admin: false,\n\t\t\t', 
                    )
                t_1.extend((
                    u'\n\t\t\tlogin_url: "', 
                    to_string(context.call(environment.getattr(l_userapi, 'create_login_url'), '/')), 
                    u'",\n\t\t\tlogout_url: "', 
                    to_string(context.call(environment.getattr(l_userapi, 'create_logout_url'), '/')), 
                    u'"\n\n\t\t});\n\t', 
                ))
            t_1.extend((
                u'\n\t// Initialize Sys Object\n\t_PLATFORM_VERSION = "', 
                to_string(environment.getattr(l_sys, 'version')), 
                u'";\n\n\t', 
            ))
            if environment.getattr(l_sys, 'debug'):
                pass
                t_1.append(
                    u'\n\t\t$.apptools.dev.setDebug({logging: true, eventlog: true, verbose: true});\n\t', 
                )
            t_1.append(
                u'\t\n\t\n});\n', 
            )
            return concat(t_1)
        context.exported_vars.add('render_page_object')
        context.vars['render_page_object'] = l_render_page_object = Macro(environment, macro, 'render_page_object', ('services', 'config', 'util', 'userapi'), (None, ), False, False, False)

    blocks = {}
    debug_info = '1=8&5=16&6=20&11=51&15=56&16=60&17=62&22=72&23=74&28=79&30=82'
    return locals()