from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/create-category.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/create-category.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/repository/create-category.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/repository/create-category.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_renderForm = context.resolve('renderForm')
        l_message = context.resolve('message')
        l_grid_caption = context.resolve('grid_caption')
        l_form = context.resolve('form')
        l_repository = context.resolve('repository')
        t_1 = environment.filters['truncate']
        if 0: yield None
        yield u'\n\n'
        if l_message:
            if 0: yield None
            yield u"\n<div id='notice'>%s</div>\n" % (
                l_message, 
            )
        yield u"\n\n<div id='gridTitle'><h2>"
        if l_grid_caption:
            if 0: yield None
            yield to_string(l_grid_caption)
        else:
            if 0: yield None
            yield u'Create a category in the repository: %s ("%s")' % (
                environment.getattr(l_repository, 'name'), 
                t_1(environment.getattr(l_repository, 'description'), 30), 
            )
        yield u'</h2></div>\n\n%s\n\n' % (
            context.call(l_renderForm, l_form), 
        )

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
        yield u' - Create a Category</h1>\n\n\t\t'
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

    def block_title(context, environment=environment):
        l_repository = context.resolve('repository')
        if 0: yield None
        yield to_string(environment.getattr(l_repository, 'name'))
        yield u' - Create a Category'

    blocks = {'content': block_content, 'header': block_header, 'title': block_title}
    debug_info = '1=9&2=12&20=21&22=30&23=33&26=36&28=46&6=49&7=56&9=63&10=66&14=72&15=73&16=74&4=77'
    return locals()