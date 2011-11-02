from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup-step1.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/security/signup-step1.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/security/signup-step1.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/security/signup-step1.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_registration_form = context.resolve('registration_form')
        l_renderForm = context.resolve('renderForm')
        l_notification_settings = context.resolve('notification_settings')
        if 0: yield None
        yield u'\n\t'
        if l_registration_form:
            if 0: yield None
            yield u"\n\t<div class='twoColumnRegistrationForm' id='leftColumn'>\n\t\t%s\n\t</div>\n\t" % (
                context.call(l_renderForm, l_registration_form), 
            )
        yield u'\n\t'
        if l_notification_settings:
            if 0: yield None
            yield u"\n\t<div class='twoColumnRegistrationForm' id='rightColumn'>\n\t\t%s\n\t</div>\n\t" % (
                context.call(l_renderForm, l_notification_settings), 
            )
        yield u'\n'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h1>Create an Account</h1> <span>Step 1: Account information</span>\n'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'Creating an Account'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u"\n<ul id='wizard_steps'>\n\t<li class='current'>\n\t\t\t<span><b>1. Account Information</b></span>\n\t\t\t<br /><p>Tell us a bit about who you are, and set up basic settings.</p>\n\t</li>\n\t<li>\n\t\t\t<span><b>2. Profile Picture</b></span>\n\t\t\t<br /><p>Upload a picture for your account.</p>\n\t</li>\n\t<li>\n\t\t\t<span><b>3. Crop Profile Picture</b></span>\n\t\t\t<br /><p>Crop your profile picture to your liking.</p>\n\t</li>\n</ul>\n\n"

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h2>Please fill in all fields.</h2>\n'

    blocks = {'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content, 'content_body_header': block_content_body_header}
    debug_info = '1=9&2=12&13=21&14=27&16=30&19=33&21=36&6=40&27=44&31=48&50=52'
    return locals()