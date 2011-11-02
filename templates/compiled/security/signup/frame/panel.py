from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup/frame/panel.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/frame.html', 'source/security/signup/frame/panel.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/security/signup/frame/panel.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/security/signup/frame/panel.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_footer_class(context, environment=environment):
        if 0: yield None
        yield u'registrationFooter'

    def block_frame_class(context, environment=environment):
        if 0: yield None
        yield u'innerRegistrationPanel'

    def block_panel_footer(context, environment=environment):
        if 0: yield None
        yield u"<div class='floatright'><a class='panelNext' href='javascript:nextAction();'>Next</a></div><div class='clearboth'></div>"

    def block_header_class(context, environment=environment):
        if 0: yield None
        yield u'registrationHeader'

    def block_content_class(context, environment=environment):
        if 0: yield None
        yield u'registrationContent'

    blocks = {'footer_class': block_footer_class, 'frame_class': block_frame_class, 'panel_footer': block_panel_footer, 'header_class': block_header_class, 'content_class': block_content_class}
    debug_info = '1=9&2=12&8=21&5=25&10=29&6=33&7=37'
    return locals()