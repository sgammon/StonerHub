from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/environ.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/environ.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_state = context.resolve('state')
        l_namespace = context.resolve('namespace')
        if 0: yield None
        yield u"\n<div id='content_padding'>\n\t<div class='box'>\n\n\t\t<p><b>Current Namespace:</b> %s</p>\n\n\t\t<h2>Variables:</h2>\n\t\t<ul>\n\t\t\t" % (
            l_namespace, 
        )
        l_value = l_key = missing
        for (l_key, l_value) in context.call(environment.getattr(l_state, 'items')):
            if 0: yield None
            yield u'\n\t\t\t\t<li><b>%s:</b> %s</li>\n\t\t\t' % (
                l_key, 
                l_value, 
            )
        l_value = l_key = missing
        yield u'\n\t\t</ul>\n\n\t</div>\n</div>\n'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Serving Environment</h1>'

    def block_module(context, environment=environment):
        if 0: yield None
        yield u'System State'

    blocks = {'content': block_content, 'header': block_header, 'module': block_module}
    debug_info = '1=9&7=15&11=20&15=23&16=26&3=32&5=36'
    return locals()