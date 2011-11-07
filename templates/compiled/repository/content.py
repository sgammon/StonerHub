from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/content.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/content.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/datagrid.html', 'source/repository/content.html').module
        l_new_datagrid = getattr(included_template, 'new_datagrid', missing)
        if l_new_datagrid is missing:
            l_new_datagrid = environment.undefined("the template %r (imported on line 2 in 'source/repository/content.html') does not export the requested name 'new_datagrid'" % included_template.__name__, name='new_datagrid')
        context.vars['new_datagrid'] = l_new_datagrid
        context.exported_vars.discard('new_datagrid')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_grid_caption = context.resolve('grid_caption')
        l_repository = context.resolve('repository')
        t_1 = environment.filters['truncate']
        if 0: yield None
        yield u"\n\n<div id='gridTitle'><h2>"
        if l_grid_caption:
            if 0: yield None
            yield to_string(l_grid_caption)
        else:
            if 0: yield None
            yield u'Showing all content from the repository: %s ("%s")' % (
                environment.getattr(l_repository, 'name'), 
                t_1(environment.getattr(l_repository, 'description'), 30), 
            )
        yield u"</h2></div>\n<div id='content_list'>\n\tWaiting for results...\n</div>\n\n\n"

    def block_header(context, environment=environment):
        l_grid_header = context.resolve('grid_header')
        l_link = context.resolve('link')
        l_repository = context.resolve('repository')
        l_grid_subline = context.resolve('grid_subline')
        if 0: yield None
        yield u'\n\t<h1>'
        if l_grid_header:
            if 0: yield None
            yield to_string(l_grid_header)
        else:
            if 0: yield None
            yield to_string(environment.getattr(l_repository, 'name'))
        yield u'</h1>\n\n\t\t'
        if l_grid_subline:
            if 0: yield None
            yield u'\n\t\t\t%s\n\t\t' % (
                l_grid_subline, 
            )
        else:
            if 0: yield None
            yield u'\n\t\t\tRepository:\n\t\t'
        yield u' \n\t\t<a href="%s">Categories</a> \n\t\t<a href="%s">Recent Content</a> \n\t\t<a href="%s">Popular Content</a>\n\n' % (
            context.call(l_link, 'repository-categories', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
            context.call(l_link, 'repository-recent-content', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
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
        yield to_string(environment.getattr(l_repository, 'name'))
        yield u' - Browse Repository Content'

    blocks = {'content': block_content, 'header': block_header, 'postsouth': block_postsouth, 'title': block_title}
    debug_info = '1=9&2=12&20=21&22=27&6=38&7=45&9=52&10=55&14=61&15=62&16=63&30=66&31=71&4=74'
    return locals()