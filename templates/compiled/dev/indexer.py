from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/indexer.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/indexer.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\n<div class=\'box\'>\n\n\t<h2>Options:</h2>\n\t<ul>\n\t\t<li><a href="%s">Enqueue Test Task</a></li>\n\t</ul>\n\t\n</div>\n\n\n' % (
            context.call(l_link, 'dev-indexer-enqueue-task'), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Indexer Console</h1>'

    def block_module(context, environment=environment):
        if 0: yield None
        yield u'Indexer'

    blocks = {'content': block_content, 'header': block_header, 'module': block_module}
    debug_info = '1=9&7=15&13=19&3=22&5=26'
    return locals()