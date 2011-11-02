from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/dev.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/dev.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\n<div  id="content_header" class="header col full">\n\t<div id=\'left\'>\n\t\t'
        for event in context.blocks['header'][0](context):
            yield event
        yield u"\n\t</div>\n\t\n\t<div id='right'>\n\t\t<div id='stackBoxes'>\n\t\t\t<div class='stackBox' id='devZone'><p>Developer Mode</p></div>\n\t\t</div>\n\t\t"
        for event in context.blocks['header_right'][0](context):
            yield event
        yield u'\n\t</div>\t\n</div>\n\n<div id=\'content_body_wrapper\' class="col full">\n\n\t<div id=\'content_body\' class="m-trbl">\n\t\t\n\t\t<div id=\'content_body_header\'>\n\t\t\t'
        for event in context.blocks['content_body_header'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t\t\n\t\t<div id=\'content_body_content\' class="content">\n\t\t\t'
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t</div>\n\n</div>\n\n\n'

    def block_header_right(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t<b>Module:</b> '
        for event in context.blocks['module'][0](context):
            yield event
        yield u'\n\t\t'

    def block_content_body_header(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\t\t\t\t<h2><a href="%s">&lt; Back to Development Console</a></h2>\n\t\t\t' % (
            context.call(l_link, 'dev-index'), 
        )

    def block_module(context, environment=environment):
        if 0: yield None

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    def block_header(context, environment=environment):
        if 0: yield None

    blocks = {'body': block_body, 'header_right': block_header_right, 'content_body_header': block_content_body_header, 'module': block_module, 'content': block_content, 'header': block_header}
    debug_info = '1=9&3=15&7=18&14=21&25=24&31=27&14=31&15=34&25=38&26=42&15=45&31=48&7=52'
    return locals()