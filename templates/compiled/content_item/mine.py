from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content_item/mine.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/content_item/mine.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/datagrid.html', 'source/content_item/mine.html').module
        l_new_datagrid = getattr(included_template, 'new_datagrid', missing)
        if l_new_datagrid is missing:
            l_new_datagrid = environment.undefined("the template %r (imported on line 2 in 'source/content_item/mine.html') does not export the requested name 'new_datagrid'" % included_template.__name__, name='new_datagrid')
        context.vars['new_datagrid'] = l_new_datagrid
        context.exported_vars.discard('new_datagrid')
        for event in parent_template.root_render_func(context):
            yield event

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'My content'

    def block_postsouth(context, environment=environment):
        l_new_datagrid = context.resolve('new_datagrid')
        l_grid = context.resolve('grid')
        if 0: yield None
        yield u'\n\t%s\n' % (
            context.call(l_new_datagrid, '#results', l_grid), 
        )

    def block_content(context, environment=environment):
        if 0: yield None
        yield u"\n\n<div>\n\t<div id='gridTitle'><h2>Showing: All content you've created, across all repositories</h2></div>\n\t<div id='results'>\n\t\tWaiting for results...\n\t</div>\t\n</div>\n\n"

    def block_header(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<h1>My content</h1> <a href="%s">List of Repositories</a> | <a href="%s">List of Tags</a>' % (
            context.call(l_link, 'repository-list'), 
            context.call(l_link, 'tags-global'), 
        )

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'What am I looking at?'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u'This view lists content <b>you</b> have created.'

    blocks = {'title': block_title, 'postsouth': block_postsouth, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&2=12&4=21&19=25&20=30&8=33&6=37&23=45&25=49'
    return locals()