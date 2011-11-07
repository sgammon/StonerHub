from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/list.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/repository/list.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_repositories = context.resolve('repositories')
        if 0: yield None
        yield u'\n<div id=\'content_body_padding\'>\n\t<h2 class="grid-title">Showing: All repositories</h2>\n\t'
        if l_repositories:
            if 0: yield None
            yield u'\n\t<dl>\n\t\t'
            l_repo = missing
            l_link = context.resolve('link')
            for l_repo in l_repositories:
                if 0: yield None
                yield u'\n\t\t<dt class="repo-links">\n\t\t\t<b>%s:</b> \n\t\t\t<a href="%s">Browse</a> \n\t\t\t<a href="%s">Add Content</a> \n\t\t\t<a href="%s">View Repo</a> \n\t\t\t<a href="%s">Edit</a> \n\t\t\t<a href="%s">Delete</a>\n\t\t</dt>\n\t\t<dd>\n\t\t\t%s\n\t\t</dd>\n\t\t' % (
                    environment.getattr(l_repo, 'name'), 
                    context.call(l_link, 'repository-content', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name'))), 
                    context.call(l_link, 'content-item-create', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name'))), 
                    context.call(l_link, 'repository-view', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name'))), 
                    context.call(l_link, 'repository-edit', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name'))), 
                    context.call(l_link, 'repository-delete', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name'))), 
                    environment.getattr(l_repo, 'description'), 
                )
            l_repo = missing
            yield u'\n\t</dl>\n\t'
        else:
            if 0: yield None
            yield u'\n\t<b>No repositories :(</b>\n\t'
        yield u'\n</div>\n'

    def block_header(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<h1>Repositories</h1> <a href="%s">Create Repository</a>' % (
            context.call(l_link, 'repository-create'), 
        )

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u"<span class='iconButtonBox infoButtonBox'>What is a Repository?</span>"

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u'\nEvery piece of content is created in a <b>Repository</b>, which groups relevant information together.<br /><br />For example, an organization might have a separate Repository for each department (e.g. "Sales" and "Creative").\n'

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Repositories'

    blocks = {'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content, 'title': block_title}
    debug_info = '1=9&7=15&10=19&12=24&14=27&15=28&16=29&17=30&18=31&19=32&22=33&5=42&33=49&35=53&3=57'
    return locals()