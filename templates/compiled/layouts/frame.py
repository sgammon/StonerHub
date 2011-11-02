from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/frame.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u"<div class='spiFrame "
        for event in context.blocks['frame_class'][0](context):
            yield event
        yield u"'>\n\t\n\t<div class='panelHeader "
        for event in context.blocks['header_class'][0](context):
            yield event
        yield u"'>\n\t\t"
        for event in context.blocks['panel_header'][0](context):
            yield event
        yield u"\n\t</div>\n\t\n\t<div class='panelContent "
        for event in context.blocks['content_class'][0](context):
            yield event
        yield u"'>\n\t\t"
        for event in context.blocks['panel_notice'][0](context):
            yield event
        yield u'\n\t\t'
        for event in context.blocks['panel_content'][0](context):
            yield event
        yield u"\n\t</div>\n\t\n\t<div class='panelFooter "
        for event in context.blocks['footer_class'][0](context):
            yield event
        yield u"'>\n\t\t"
        for event in context.blocks['panel_footer'][0](context):
            yield event
        yield u'\n\t</div>\n\t\n</div>'

    def block_panel_content(context, environment=environment):
        l_lipsum = context.resolve('lipsum')
        if 0: yield None
        yield u'<p>%s</p>' % (
            context.call(l_lipsum, 1), 
        )

    def block_panel_footer(context, environment=environment):
        if 0: yield None
        yield u'<h2>Footer</h2>'

    def block_header_class(context, environment=environment):
        if 0: yield None

    def block_content_class(context, environment=environment):
        if 0: yield None

    def block_footer_class(context, environment=environment):
        if 0: yield None

    def block_frame_class(context, environment=environment):
        if 0: yield None

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u'<h2>Header</h2>'

    def block_notice_class(context, environment=environment):
        if 0: yield None

    def block_panel_notice(context, environment=environment):
        if 0: yield None
        yield u"<div class='panelNotice "
        for event in context.blocks['notice_class'][0](context):
            yield event
        yield u"' style='display:none;'></div>"

    blocks = {'panel_content': block_panel_content, 'panel_footer': block_panel_footer, 'header_class': block_header_class, 'content_class': block_content_class, 'footer_class': block_footer_class, 'frame_class': block_frame_class, 'panel_header': block_panel_header, 'notice_class': block_notice_class, 'panel_notice': block_panel_notice}
    debug_info = '1=9&3=12&4=15&7=18&8=21&9=24&12=27&13=30&9=34&13=41&3=45&7=48&12=51&1=54&4=57&8=61'
    return locals()