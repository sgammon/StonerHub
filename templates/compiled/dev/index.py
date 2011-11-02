from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/index.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/dev/index.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\n<div class=\'content_box\'>\n\t<ul>\n\t\t<li><b><a href="%s">Cache Management</a></b></li>\n\t\t<li><b><a href="%s">Serving Environment</a></b></li>\t\t\n\t\t<li><b><a href="%s">Default Data</a></b></li>\t\t\n\t\t<li><b><a href="%s">Security Console</a></b></li>\n\t\t<li><b><a href="%s">Indexer Console</a></b></li>\t\t\n\t\t<li><b><a href="%s">Command Shell</a></b></li>\t\t\n\t</ul>\n</div>\n\n\n' % (
            context.call(l_link, 'dev-cache'), 
            context.call(l_link, 'dev-environ'), 
            context.call(l_link, 'dev-default-data'), 
            context.call(l_link, 'dev-security'), 
            context.call(l_link, 'dev-indexer'), 
            context.call(l_link, 'dev-shell'), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Development Console</h1>'

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'<h2 class="grid-title">Modules</h2>'

    blocks = {'content': block_content, 'header': block_header, 'content_body_header': block_content_body_header}
    debug_info = '1=9&7=15&11=19&12=20&13=21&14=22&15=23&16=24&3=27&5=31'
    return locals()