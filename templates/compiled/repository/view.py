from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/view.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/view.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_category_count = context.resolve('category_count')
        l_repository = context.resolve('repository')
        l_ci_count = context.resolve('ci_count')
        if 0: yield None
        yield u"\n<div id='content_body_padding'>\n\t"
        if l_repository:
            if 0: yield None
            yield u'\n\t<h2 class="grid-title">Details about the "%s" repository</h2>\n\n\t<ul>\n\t\t<li><b>Description:</b> %s</li>\n\t\t<li><b>Number of Content Items:</b> %s</li>\n\t\t<li><b>Number of Categories:</b> %s</li>\n\t</ul>\n\t' % (
                environment.getattr(l_repository, 'name'), 
                environment.getattr(l_repository, 'description'), 
                l_ci_count, 
                l_category_count, 
            )
        else:
            if 0: yield None
            yield u'\n\n\t<p>No repository key given.</p>\n\n\t'
        yield u'\n</div>\n'

    def block_header(context, environment=environment):
        l_link = context.resolve('link')
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'\n\t<h1>%s</h1>\n\t\n\t\t' % (
            environment.getattr(l_repository, 'name'), 
        )
        if l_repository:
            if 0: yield None
            yield u' \n\t\t<span>\n\t\t\t<a href="%s">Edit</a> \n\t\t\t<a href="%s">Content</a>  \n\t\t\t<a href="%s">Permissions</a> \n\t\t\t<a href="%s">Delete</a>\n\t\t</span>\n\t\t' % (
                context.call(l_link, 'repository-edit', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
                context.call(l_link, 'repository-content', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
                context.call(l_link, 'repository-edit-permissions', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
                context.call(l_link, 'repository-delete', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
            )
        yield u'\n\t\n'

    def block_title(context, environment=environment):
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'"%s" Repository' % (
            environment.getattr(l_repository, 'name'), 
        )

    blocks = {'content': block_content, 'header': block_header, 'title': block_title}
    debug_info = '1=9&19=15&21=21&22=24&25=25&26=26&27=27&5=34&6=39&8=41&10=44&11=45&12=46&13=47&3=51'
    return locals()