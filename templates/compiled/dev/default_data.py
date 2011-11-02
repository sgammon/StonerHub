from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/default_data.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/default_data.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_functions = context.resolve('functions')
        l_exec_results = context.resolve('exec_results')
        l_success = context.resolve('success')
        l_link = context.resolve('link')
        l_total_keys = context.resolve('total_keys')
        if 0: yield None
        yield u"\n\n<h2>Default Data</h2>\n\n<div class='box'>\n\t\n\t"
        if l_success == False:
            if 0: yield None
            yield u'\n\t<form action="%s" method="post">\n\t\t\n\t\t<p><b>Are you sure you want to run the default data insert tool?</b>\n\t\t\t<br /><br />\n\t\t\tThis will execute the following utility functions:\n\t\t\t<ul>\n\t\t\t\t' % (
                context.call(l_link, 'dev-default-data'), 
            )
            l_func = missing
            for l_func in l_functions:
                if 0: yield None
                yield u'\n\t\t\t\t<li>%s</li>\n\t\t\t\t' % (
                    l_func, 
                )
            l_func = missing
            yield u'\n\t\t\t</ul>\n\t\t</p>\n\t\t\n\t\t<input type=\'submit\' value=\'Execute\' />\n\t\t<small><a href="%s">Cancel</a></small>\n\t\t\n\t</form>\n\t' % (
                context.call(l_link, 'dev-index'), 
            )
        else:
            if 0: yield None
            yield u'\n\t<p><b>Execution Results:</b>\n\t\t<br /><br />\n\t\tCreated a total of %s keys.\n\t\t<ul>\n\t\t\t' % (
                l_total_keys, 
            )
            l_func = l_key_count = missing
            for (l_func, l_key_count) in l_exec_results:
                if 0: yield None
                yield u'\n\t\t\t<li>Function "%s" generated %s keys.</li>\n\t\t\t' % (
                    l_func, 
                    l_key_count, 
                )
            l_func = l_key_count = missing
            yield u'\n\t\t</ul>\n\t\t\n\t\t<a href="%s">Back to Development Console</a>\n\t' % (
                context.call(l_link, 'dev-index'), 
            )
        yield u'\n</div>\n\n\n'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Development Console</h1>'

    def block_module(context, environment=environment):
        if 0: yield None
        yield u'Default Data'

    blocks = {'content': block_content, 'header': block_header, 'module': block_module}
    debug_info = '1=9&7=15&13=23&14=26&20=29&21=32&27=36&33=41&35=44&36=47&40=52&3=56&5=60'
    return locals()