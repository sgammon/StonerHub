from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main-twocolumn-nostack.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/main-twocolumn-nostack.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/layouts/main-twocolumn-nostack.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/layouts/main-twocolumn-nostack.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\n'
        for event in context.blocks['top_content_header'][0](context):
            yield event
        yield u'\n\n<div class="col full">\n\n\t<div class="m-trbl">\n\t\t\n\t\t<div id="content_header" class="header">\n\t\t\t'
        for event in context.blocks['header'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\n\n\n<div id='document_pane' class='"
        for event in context.blocks['document_pane_class'][0](context):
            yield event
        yield u' col threequarters clear\'>\n\t\n\t<div id=\'content_body\' class="m-rbl">\n\t\t\n\t\t<div  id="content_header" class=\'header '
        for event in context.blocks['inner_header_class'][0](context):
            yield event
        yield u"'>\n\t\t\t"
        for event in context.blocks['content_body_header'][0](context):
            yield event
        yield u"\n\t\t</div>\n\n\t\t<div id='content_body_content' class='content "
        for event in context.blocks['inner_content_class'][0](context):
            yield event
        yield u"'>\n\t\t\t"
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t</div>\n\t\n</div>\n\n<div id=\'sidebar\' class="col quarter">\n\t\n\t<div class="m-rb">\n\t\t<div id=\'sidebar_header\'>\n\t\t\t'
        for event in context.blocks['sidebar_header'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t\n\t\t<div id='sidebar_content'>\n\t\t\t"
        for event in context.blocks['sidebar_content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t</div>\n\t\n</div>\n'

    def block_document_pane_class(context, environment=environment):
        if 0: yield None
        yield u'defaultDocumentPane'

    def block_inner_header_class(context, environment=environment):
        if 0: yield None
        yield u'defaultInnerHeader'

    def block_inner_content_class(context, environment=environment):
        if 0: yield None
        yield u'defaultInnerContent'

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t<h2>Content Header</h2>\n\t\t\t'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    def block_header(context, environment=environment):
        if 0: yield None

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Header</p>'

    def block_top_content_header(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Content</p>'

    blocks = {'body': block_body, 'document_pane_class': block_document_pane_class, 'inner_header_class': block_inner_header_class, 'inner_content_class': block_inner_content_class, 'content_body_header': block_content_body_header, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'top_content_header': block_top_content_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&2=12&4=21&6=24&14=27&22=30&26=33&27=36&32=39&33=42&43=45&47=48&22=52&26=56&32=60&27=64&33=68&14=72&43=75&6=79&47=83'
    return locals()