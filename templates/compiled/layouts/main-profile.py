from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main-profile.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/main-profile.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/layouts/main-profile.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/layouts/main-profile.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\n\n\n<div class="col full">\n\n\t<div class="m-trbl">\n\t\t\n\t\t<div id="content_header" class="header">\n\t\t\t<h1>'
        for event in context.blocks['profile_heading'][0](context):
            yield event
        yield u'</h1>\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\n\n<div id=\'document_pane\' class=\' col threequarters clear\'>\n\n\t<div id=\'content_body\' class="m-rbl">\n\t\t\n\t\t<div  id="content_header" class=\'header userProfileHeader\'>\n\t\t\t<div id=\'profileAvatar\' class=\'userAvatar\'><a href=\'#\'><span></span><img src=\''
        for event in context.blocks['avatar_href'][0](context):
            yield event
        yield u"' /></a>\n\t\t\t</div>\n\t\t</div>\n\n\t\t<div id='content_body_content' class='content userProfileContent'>\n\t\t\t"
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t</div>\n\n</div>\n\n<div id=\'sidebar\' class="col quarter">\n\t\n\t<div id=\'sidebar_header\'>\n\t\t'
        for event in context.blocks['sidebar_header'][0](context):
            yield event
        yield u"\n\t</div>\n\t\n\t<div id='sidebar_content'>\n\t\t"
        for event in context.blocks['sidebar_content'][0](context):
            yield event
        yield u'\n\t</div>\n\t\n</div>\n\t\n\n\n'

    def block_profile_heading(context, environment=environment):
        if 0: yield None
        yield u'User Profile'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Header</p>'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Content</p>'

    def block_avatar_href(context, environment=environment):
        if 0: yield None
        yield u'/assets/img/static/layout/profile-default.png'

    blocks = {'body': block_body, 'profile_heading': block_profile_heading, 'content': block_content, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content, 'avatar_href': block_avatar_href}
    debug_info = '1=9&2=12&6=21&19=24&31=27&36=30&45=33&49=36&19=40&36=44&45=48&49=52&31=56'
    return locals()