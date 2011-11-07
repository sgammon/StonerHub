from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/repository/create.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/repository/create.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_renderForm = context.resolve('renderForm')
        l_create_repo_form = context.resolve('create_repo_form')
        if 0: yield None
        yield u'\n\n%s\n\n' % (
            context.call(l_renderForm, l_create_repo_form), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Create Repository</h1>'

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h2 class="grid-title">A repository is a database of related content. "Engineering" or "Marketing", for example.</h2>\n'

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Create Repository'

    blocks = {'content': block_content, 'header': block_header, 'content_body_header': block_content_body_header, 'title': block_title}
    debug_info = '1=9&11=15&13=20&5=23&7=27&3=31'
    return locals()