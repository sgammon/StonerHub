from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup/frame/step3-settings.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('security/signup/frame/panel.html', 'source/security/signup/frame/step3-settings.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        if 0: yield None
        yield u'\n\t<p>This panel will eventually contain basic settings for a new user account.</p>\n'

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u"<h2><span class='iconButtonBox okButtonBox'>Introduction</span><span class='iconButtonBox okButtonBox'>Basic Info</span><span class='iconButtonBox okButtonBox'>Profile</span><span class='iconButtonBox currentStep'>Settings</span></h2>"

    def block_panel_footer(context, environment=environment):
        if 0: yield None
        yield u"\n<div class='floatright'>\n\t<a class='panelNext' href='javascript:$.fancybox.close();loadNavigation();'>Finish</a>\n</div>\n<div class='clearboth'></div>\n"

    blocks = {'panel_content': block_panel_content, 'panel_header': block_panel_header, 'panel_footer': block_panel_footer}
    debug_info = '1=9&5=15&3=19&9=23'
    return locals()