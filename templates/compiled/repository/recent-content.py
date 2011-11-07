from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/recent-content.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/recent-content.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/datagrid.html', 'source/repository/recent-content.html').module
        l_new_datagrid = getattr(included_template, 'new_datagrid', missing)
        if l_new_datagrid is missing:
            l_new_datagrid = environment.undefined("the template %r (imported on line 2 in 'source/repository/recent-content.html') does not export the requested name 'new_datagrid'" % included_template.__name__, name='new_datagrid')
        context.vars['new_datagrid'] = l_new_datagrid
        context.exported_vars.discard('new_datagrid')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_grid_caption = context.resolve('grid_caption')
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u"\n\n<div id='gridTitle'><h2>"
        if l_grid_caption:
            if 0: yield None
        else:
            if 0: yield None
            yield u'Showing all content from the repository "%s", sorted to see the newest items first.' % (
                environment.getattr(l_repository, 'name'), 
            )
        yield u"</h2></div>\n<div id='content_list'>\n\tWaiting for results...\n</div>\n\n\n"

    def block_header(context, environment=environment):
        l_link = context.resolve('link')
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'<h1>%s</h1> <span>Recent Content</span><span><a href="%s">Browse</a> | <a href="%s">Categories</a> | <a href="%s">Popular Content</a></span>' % (
            environment.getattr(l_repository, 'name'), 
            context.call(l_link, 'repository-content', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
            context.call(l_link, 'repository-categories', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
            context.call(l_link, 'repository-popular-content', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
        )

    def block_postsouth(context, environment=environment):
        l_new_datagrid = context.resolve('new_datagrid')
        l_grid = context.resolve('grid')
        if 0: yield None
        yield u'\n\t%s\n' % (
            context.call(l_new_datagrid, '#content_list', l_grid), 
        )

    def block_title(context, environment=environment):
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'Recent Content - '
        yield to_string(environment.getattr(l_repository, 'name'))

    blocks = {'content': block_content, 'header': block_header, 'postsouth': block_postsouth, 'title': block_title}
    debug_info = '1=9&2=12&8=21&10=26&6=35&18=46&19=51&4=54'
    return locals()