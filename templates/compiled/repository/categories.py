from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/categories.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/categories.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_len = context.resolve('len')
        l_repository = context.resolve('repository')
        l_categories = context.resolve('categories')
        if 0: yield None
        yield u'\n\n<div id=\'content_body_padding\'>\n\t<h2 class="grid-title">Showing: all categories for repository "%s".</h2>\n\t<div id=\'categories_list\'>\n\n\t\t' % (
            environment.getattr(l_repository, 'name'), 
        )
        if context.call(l_len, l_categories) > 0:
            if 0: yield None
            yield u'\n\t\t\t<ul>\n\t\t\t'
            l_category = l_values = missing
            l_link = context.resolve('link')
            for (l_category, l_values) in context.call(environment.getattr(l_categories, 'items')):
                if 0: yield None
                yield u'\n\t\t\t\t<li><span class=\'iconButtonBox\'><b><a href="%s/%s">%s</a>&nbsp; </b></span> %s document' % (
                    context.call(l_link, 'repository-content', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
                    environment.getattr(l_values, 'filter_path'), 
                    l_category, 
                    environment.getattr(l_values, 'count'), 
                )
                if (environment.getattr(l_values, 'count') > 1 or environment.getattr(l_values, 'count') == 0):
                    if 0: yield None
                    yield u's'
                yield u'.</li>\n\t\t\t'
            l_category = l_values = missing
            yield u'\n\t\t\t</ul>\n\t\t'
        else:
            if 0: yield None
            yield u'\n\t\t\t<b>There are currently no categories for this repository.</b>\n\t\t'
        yield u'\n\t\n\t</div>\n</div>\n\n\n'

    def block_header(context, environment=environment):
        l_link = context.resolve('link')
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'<h1>%s</h1><span><a href="%s">Create a Category</a></span>' % (
            environment.getattr(l_repository, 'name'), 
            context.call(l_link, 'repository-category-create', repo=context.call(environment.getattr(context.call(environment.getattr(l_repository, 'key')), 'name'))), 
        )

    def block_title(context, environment=environment):
        l_repository = context.resolve('repository')
        if 0: yield None
        yield to_string(environment.getattr(l_repository, 'name'))
        yield u' - Categories'

    blocks = {'content': block_content, 'header': block_header, 'title': block_title}
    debug_info = '1=9&7=15&10=21&13=23&15=28&16=31&5=47&3=56'
    return locals()