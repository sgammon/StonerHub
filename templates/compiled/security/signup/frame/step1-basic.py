from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup/frame/step1-basic.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('security/signup/frame/panel.html', 'source/security/signup/frame/step1-basic.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        l_renderForm = context.resolve('renderForm')
        l_form = context.resolve('form')
        if 0: yield None
        yield u'\n\t%s\n\t<script>\n\t\tloadPanel(\'basic\');\n\t\tregisterForm(\'.spi-form\', "%s", "%s");\n\t\t$(\'#firstname\').attr(\'autofocus\', \'autofocus\');\n\t</script>\n' % (
            context.call(l_renderForm, l_form, omitSubmitButton=True), 
            context.call(environment.getattr(l_form, 'get_action')), 
            context.call(environment.getattr(l_form, 'get_method')), 
        )

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u"<h2><span class='iconButtonBox okButtonBox'>Introduction</span><span class='iconButtonBox currentStep'>Basic Info</span><span>Profile</span><span>Settings</h2>"

    blocks = {'panel_content': block_panel_content, 'panel_header': block_panel_header}
    debug_info = '1=9&5=15&6=20&9=21&3=25'
    return locals()