from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/main.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/layouts/main.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/layouts/main.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\n<div class="col full">\n\t\n\t<div class="m-trbl">\n\t\n\t\t<div id="content_header" class="header">\n\t\t\t'
        for event in context.blocks['header'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t\t\n\t</div>\n\t\n\t<div class="m-trbl">\n\t\t\n\t\t<div id=\'content_body\'>\n\t\t\t\n\t\t\t<div id=\'content_body_content\' class="content">\n\t\t\t\t'
        for event in context.blocks['content_body_header'][0](context):
            yield event
        yield u'\n\t\t\t\t'
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t\t\n\t</div>\n\t\n</div>\n\n'

    def block_header(context, environment=environment):
        if 0: yield None

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t'

    blocks = {'body': block_body, 'header': block_header, 'content': block_content, 'content_body_header': block_content_body_header}
    debug_info = '1=9&2=12&4=21&11=24&21=27&23=30&11=34&23=37&21=41'
    return locals()