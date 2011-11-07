from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content_item/recent.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/content_item/recent.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/datagrid.html', 'source/content_item/recent.html').module
        l_new_datagrid = getattr(included_template, 'new_datagrid', missing)
        if l_new_datagrid is missing:
            l_new_datagrid = environment.undefined("the template %r (imported on line 2 in 'source/content_item/recent.html') does not export the requested name 'new_datagrid'" % included_template.__name__, name='new_datagrid')
        context.vars['new_datagrid'] = l_new_datagrid
        context.exported_vars.discard('new_datagrid')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        if 0: yield None
        yield u"\n\n<div>\n\t<div id='gridTitle'><h2>Showing: All content across all repositories, sorted by date created in descending order.</h2></div>\n\t<div id='results'>\n\t\tWaiting for results...\n\t</div>\t\n</div>\n\n"

    def block_header(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<h1>Recent content</h1> <a href="%s">List of Repositories</a> | <a href="%s">List of Tags</a>' % (
            context.call(l_link, 'repository-list'), 
            context.call(l_link, 'tags-global'), 
        )

    def block_postsouth(context, environment=environment):
        l_new_datagrid = context.resolve('new_datagrid')
        l_grid = context.resolve('grid')
        if 0: yield None
        yield u'\n\t%s\n' % (
            context.call(l_new_datagrid, '#results', l_grid), 
        )

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Recent content'

    blocks = {'content': block_content, 'header': block_header, 'postsouth': block_postsouth, 'title': block_title}
    debug_info = '1=9&2=12&8=21&6=25&19=33&20=38&4=41'
    return locals()