from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/datagrid.html'

    def root(context, environment=environment):
        t_1 = environment.tests['string']
        if 0: yield None
        def macro(l_selector, l_grid):
            t_2 = []
            l_util = context.resolve('util')
            l_len = context.resolve('len')
            pass
            t_2.append(
                u'\n', 
            )
            (l_method, l_method_args) = context.call(environment.getattr(l_grid, 'get_method'))
            t_2.append(
                u'\n', 
            )
            (l_grid_args, l_grid_args_count) = (context.call(environment.getattr(l_grid, 'get_extra_args')), context.call(l_len, context.call(environment.getattr(l_grid, 'get_extra_args'))))
            t_2.append(
                u'\n\n', 
            )
            if t_1(context.call(environment.getattr(l_grid, 'get_script_snippet'), 'north')):
                pass
                t_2.append(
                    u"\n<script type='text/javascript'>\n\t", 
                )
                template = environment.get_or_select_template(context.call(environment.getattr(l_grid, 'get_script_snippet'), 'north'), 'source/macros/datagrid.html')
                for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                    t_2.append(event)
                t_2.append(
                    u'\n</script>\n', 
                )
            t_2.append(
                u'\n\n<script type=\'text/javascript\'>\n\nvar rpcTracker = {Requests:{}, lastRequest:null};\n\nfunction makeGridRPC(sSource, aoData, fnCallback)\n{\n\t/* Set RPC method & params */\n\tsMethod = "', 
            )
            l_off = context.resolve('off')
            pass
            t_3 = context.eval_ctx.save()
            context.eval_ctx.autoescape = l_off
            t_2.append(
                (context.eval_ctx.autoescape and escape or to_string)(l_method), 
            )
            context.eval_ctx.revert(t_3)
            t_2.append(
                u'";\n\toParams =', 
            )
            if context.call(l_len, l_method_args) > 0:
                pass
                l_util = context.resolve('util')
                l_dict = context.resolve('dict')
                l_off = context.resolve('off')
                pass
                t_4 = context.eval_ctx.save()
                context.eval_ctx.autoescape = l_off
                t_2.append(
                    (context.eval_ctx.autoescape and escape or to_string)(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), context.call(l_dict, l_method_args))), 
                )
                context.eval_ctx.revert(t_4)
            else:
                pass
                t_2.append(
                    u'{}', 
                )
            t_2.extend((
                u';\n\n\t/* Add to RPC tracker and fire */\n\trpcTracker.Requests[aoData[\'sEcho\']] = {source: sSource, grid: aoData, callback: fnCallback, method: sMethod, params:oParams};\n\t$.stonerhub.datatables.load("', 
                to_string(context.call(environment.getattr(l_grid, 'get_service'))), 
                u'", sSource, sMethod, oParams, aoData, fnCallback);\n}\n\ndataGridOptions = {};\nfunction createDatagrid()\n{\n\t/* Manufacture a table */\n\t$(\'', 
                to_string(l_selector), 
                u'\').html(\'<table cellpadding="0" cellspacing="0" border="0" class="display" id="datagrid"></table>\');\n\n\t/* Set up grid options */\n\tdataGridOptions = {\n\t\t"bProcessing": true,\n\t\t"bFilter": false,\n\t\t"bServerSide": true,\n\t\t"bPaginate": true,\n\t\t"bLengthChange": true,\n\t\t"bJQueryUI": true,\n\t\t"bStateSave": true,\n\t\t"sPaginationType": "full_numbers",\n\t\t', 
            ))
            if 'aoColumns' not in l_grid_args:
                pass
                t_2.append(
                    u'\n\t\t\t', 
                )
                if context.call(l_len, context.call(environment.getattr(l_grid, 'get_columns'))) > 0:
                    pass
                    t_2.extend((
                        u'\n\t\t\t\t"aoColumns": ', 
                        to_string(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), context.call(environment.getattr(l_grid, 'getColumnsForMacro')))), 
                        u',\n\t\t\t', 
                    ))
                t_2.append(
                    u'\n\t\t', 
                )
            t_2.append(
                u'\n\t\t\n\t\t', 
            )
            if l_grid_args_count > 0:
                pass
                l_value = l_key = missing
                for (l_key, l_value) in context.call(environment.getattr(l_grid_args, 'items')):
                    pass
                    t_2.extend((
                        u"'", 
                        to_string(l_key), 
                        u"': ", 
                        to_string(l_value), 
                        u',', 
                    ))
                l_value = l_key = missing
            t_2.extend((
                u'\n\t\t\n\t\t"sAjaxSource": "', 
                to_string(context.call(environment.getattr(l_grid, 'get_service_endpoint'))), 
                u'",\n\t\t"fnServerData": makeGridRPC,\n\t};\n\t\n\tconsole.log(\'Datagrid Options: \', dataGridOptions);\n\t\n\t/* Initialize datagrid */\n\t$(\'', 
                to_string(l_selector), 
                u" #datagrid').dataTable(dataGridOptions);\n}\n\n/* Build datagrid on page ready */\n$(document).ready(createDatagrid());\n\n</script>\n\n", 
            ))
            if t_1(context.call(environment.getattr(l_grid, 'get_script_snippet'), 'south')):
                pass
                t_2.append(
                    u"\n<script type='text/javascript'>\n\t", 
                )
                template = environment.get_or_select_template(context.call(environment.getattr(l_grid, 'get_script_snippet'), 'south'), 'source/macros/datagrid.html')
                for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                    t_2.append(event)
                t_2.append(
                    u'\t\n</script>\n', 
                )
            t_2.append(
                u'\n\n', 
            )
            return concat(t_2)
        context.exported_vars.add('new_datagrid')
        context.vars['new_datagrid'] = l_new_datagrid = Macro(environment, macro, 'new_datagrid', ('selector', 'grid'), (), False, False, False)

    blocks = {}
    debug_info = '1=9&2=17&3=21&5=25&7=30&18=44&19=50&23=69&30=71&42=74&43=79&44=83&48=92&49=95&50=99&54=107&61=109&69=112&71=117'
    return locals()