from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main-twocolumn.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/main-twocolumn.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/layouts/main-twocolumn.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/layouts/main-twocolumn.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\n<div class="col full">\n\n\t<div class="m-trbl">\n\t\t\n\t\t<div id="content_header" class="header">\n\t\t\t'
        for event in context.blocks['header'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\n\n\n<div class="col threequarters clear">\n\t\n\t'
        for event in context.blocks['landing_page_search_box'][0](context):
            yield event
        yield u'\n\t\n\t<div id=\'content_body\' class="m-rbl">\n\t\t\n\t\t<div id=\'content_body_content\' class="content">\n\t\t\t'
        for event in context.blocks['content_body_header'][0](context):
            yield event
        yield u'\n\t\t\t'
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\n\n<div id=\'sidebar\' class="col quarter">\n\t\n\t<div class="m-rb">\n\t\t\n\t\t<div id=\'sidebar_header\'>\n\t\t\t'
        for event in context.blocks['sidebar_header'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t\n\t\t<div id='sidebar_content'>\n\t\t\t"
        for event in context.blocks['sidebar_content'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t\n\t\t<div id='lower_sidebar'>\n\t\t\t<a href='http://www.wire-stone.com/' alt-'[wire] stone' class='wsLogoAnchor'><img src='/assets/img/static/layout/wirestone/w-50-blue-on-gray.png' alt='[wire] stone logo' id='wsLogo' /></a>\n\t\t</div>\n\t\t\n\t</div>\n\t\n</div>\n\n\n"

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t'

    def block_landing_page_search_box(context, environment=environment):
        if 0: yield None

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    def block_header(context, environment=environment):
        if 0: yield None

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Header</p>'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Content</p>'

    blocks = {'body': block_body, 'content_body_header': block_content_body_header, 'landing_page_search_box': block_landing_page_search_box, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&2=12&4=21&11=24&21=27&26=30&28=33&40=36&44=39&26=43&21=47&28=50&11=54&40=57&44=61'
    return locals()