from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup-step2.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/security/signup-step2.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/security/signup-step2.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/security/signup-step2.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_message = context.resolve('message')
        l_upload_url = context.resolve('upload_url')
        if 0: yield None
        yield u'\n\t\n\t'
        if l_message:
            if 0: yield None
            yield u"\n\t\t<p class='notice'>%s</p><br />\n\t" % (
                l_message, 
            )
        yield u'\n\n\t<form action="%s" method=\'post\' enctype="multipart/form-data">\n\t\t<input type=\'file\' name=\'profile_picture_raw\' id=\'fileUploadInput\' />\n\t\t<br />\n\t\t<input type=\'submit\' value=\'upload\' />\n\t</form>\n' % (
            l_upload_url, 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h1>Create an Account</h1> <span>Step 2: Profile Picture</span>\n'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'Creating an Account'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u"\n<ul id='wizard_steps'>\n\t<li>\n\t\t\t<span><b>1. Account Information</b></span>\n\t\t\t<br /><p>Tell us a bit about who you are.</p>\n\t</li>\n\t<li class='current'>\n\t\t\t<span><b>2. Profile Picture</b></span>\n\t\t\t<br /><p>Upload a picture for all to see.</p>\n\t</li>\n\t<li>\n\t\t\t<span><b>3. Crop Profile Picture</b></span>\n\t\t\t<br /><p>Crop your profile picture to your liking.</p>\n\t</li>\n</ul>\n\n"

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h2>Upload a profile picture</h2>\n'

    blocks = {'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content, 'content_body_header': block_content_body_header}
    debug_info = '1=9&2=12&13=21&15=26&16=29&19=32&6=35&27=39&31=43&50=47'
    return locals()