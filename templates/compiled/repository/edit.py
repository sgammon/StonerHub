from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/edit.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/edit.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_renderForm = context.resolve('renderForm')
        l_edit_repo_form = context.resolve('edit_repo_form')
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'\n\n<h2 class="grid-title">%s</h2>\n\n%s\n\n' % (
            environment.getattr(l_repository, 'name'), 
            context.call(l_renderForm, l_edit_repo_form), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Edit Repository</h1>'

    def block_title(context, environment=environment):
        l_repository = context.resolve('repository')
        if 0: yield None
        yield u'Edit the "%s" repository' % (
            environment.getattr(l_repository, 'name'), 
        )

    blocks = {'content': block_content, 'header': block_header, 'title': block_title}
    debug_info = '1=9&7=15&9=21&11=22&5=25&3=29'
    return locals()