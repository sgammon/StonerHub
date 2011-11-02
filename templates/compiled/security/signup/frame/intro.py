from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup/frame/intro.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('security/signup/frame/panel.html', 'source/security/signup/frame/intro.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        if 0: yield None
        yield u"\n\t<p>This wizard will help you set up your Wirestone Universal Content Repository account.</p>\n\t<script>\n\t\tloadPanel('intro');\n\t\t\n\t\tfunction loadNavigation()\n\t\t{\n\t\t\t$('#unregisteredNav').addClass('hidden');\n\t\t\t$('#registeredNav').removeClass('hidden');\n\t\t}\n\t\t\n\t</script>\n"

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u"<h2><span class='iconButtonBox currentStep'>Introduction</span><span>Basic Info</span><span>Profile</span><span>Settings</span></h2>"

    blocks = {'panel_content': block_panel_content, 'panel_header': block_panel_header}
    debug_info = '1=9&6=15&3=19'
    return locals()