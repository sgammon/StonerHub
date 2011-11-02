from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/security.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/security.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_link = context.resolve('link')
        l_user = context.resolve('user')
        if 0: yield None
        yield u'\n\n<div class=\'box\'>\n\n\t<h2>Options:</h2>\n\t<ul>\n\t\t<li><a href="%s">Manage Account Tokens</a></li>\n\t</ul>\n\t\n\t<br />\n\t<hr />\n\t<br />\n\n\t<h2>Current user:</h2>\n\t<ul>\n\t\t<li><b>Nickname:</b> %s</li>\n\t\t<li><b>Is Sys Admin:</b> %s</li>\t\t\t\n\t\t<li><b>Is Dev Admin:</b> %s</li>\n\t\t<li><b>Key:</b> %s</li>\n\t\t<br />\n\t\t<li><b>Role Memberships:</b>\n\t\t\t\n\t\t\t<ul>\n\t\t\t\t<li>None.</li>\n\t\t\t</ul>\n\t\t\t\n\t\t</li>\n\t\t<br />\n\t\t<li><b>Group Memberships:</b>\n\t\t\t\n\t\t\t<ul>\n\t\t\t\t<li>None.</li>\n\t\t\t</ul>\n\t\t\t\n\t\t</li>\n\t</ul>\n\n</div>\n\n\n' % (
            context.call(l_link, 'dev-security-claims'), 
            context.call(environment.getattr(l_user, 'nickname')), 
            environment.getattr(l_user, 'perm_sys_admin'), 
            environment.getattr(l_user, 'perm_dev_admin'), 
            context.call(environment.getattr(l_user, 'key')), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Security Console</h1>'

    def block_module(context, environment=environment):
        if 0: yield None
        yield u'Security'

    blocks = {'content': block_content, 'header': block_header, 'module': block_module}
    debug_info = '1=9&7=15&13=20&22=21&23=22&24=23&25=24&3=27&5=31'
    return locals()