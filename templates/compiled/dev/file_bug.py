from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/file_bug.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/file_bug.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/dev/file_bug.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/dev/file_bug.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'File a Bug Report'

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'<h2>Please be specific, and include steps to reproduce the bug (if possible).</h2>'

    def block_postsouth(context, environment=environment):
        if 0: yield None
        yield u"\n<script type='text/javascript'>\n\n$(document).ready(function (){\n\t\n\t$('#title-box input').focus(function () {\n\t\t$('#title-box input').val('');\n\t});\n\t\n});\n\n</script>\n"

    def block_module(context, environment=environment):
        if 0: yield None
        yield u'Quality Assurance'

    def block_content(context, environment=environment):
        l_renderForm = context.resolve('renderForm')
        l_form = context.resolve('form')
        l_success = context.resolve('success')
        if 0: yield None
        yield u'\n\n'
        if l_success == True:
            if 0: yield None
            yield u"\n<div class='notice'>Bug report submitted successfully. Thanks! :)</div>\n"
        yield u"\n\n<div class='box'>\n\t%s\n</div>\n\n" % (
            context.call(l_renderForm, l_form, submit_value='Submit Report'), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>File a Bug Report</h1>'

    blocks = {'title': block_title, 'content_body_header': block_content_body_header, 'postsouth': block_postsouth, 'module': block_module, 'content': block_content, 'header': block_header}
    debug_info = '1=9&2=12&4=21&10=25&24=29&8=33&12=37&14=43&19=47&6=50'
    return locals()