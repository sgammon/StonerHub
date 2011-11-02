from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup-step4.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/security/signup-step4.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_continue_url = context.resolve('continue_url')
        if 0: yield None
        yield u'\n\t<p>You\'re all finished setting up your new account..<br />\n\t\t<a href="%s">Continue &gt;</a></p>\n' % (
            l_continue_url, 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h1>Create an Account</h1> <span>Account setup complete!</span>\n'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'Creating an Account'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u"\n<ul id='wizard_steps'>\n\t<li>\n\t\t\t<span><b>Account Information</b></span>\n\t\t\t<br /><p>Tell us a bit about who you are.</p>\n\t</li>\n\t<li>\n\t\t\t<span><b>Profile Picture</b></span>\n\t\t\t<br /><p>Upload a picture for all to see.</p>\n\t</li>\t\t\n</ul>\n"

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h2>Please fill in all fields.</h2>\n'

    blocks = {'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content, 'content_body_header': block_content_body_header}
    debug_info = '1=9&12=15&14=19&5=22&18=26&22=30&36=34'
    return locals()