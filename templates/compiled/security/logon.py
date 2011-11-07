from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/logon.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/security/logon.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/security/logon.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/security/logon.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block__wrapper(context, environment=environment):
        l_notice = context.resolve('notice')
        l_renderForm = context.resolve('renderForm')
        l_logon_form = context.resolve('logon_form')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n<div id=\'content\'>\n\t<div id=\'splash\'>\n\t\t\n\t\t<div id=\'unsupportedBrowserWarning\' class=\'hidden\'>\n\n\t\t\t<p>\n\t\t\t\tUnfortunately, the browser you are using to visit this site is not compatible with one or more required features.<br />\n\t\t\t\tPlease visit this site using either <a href=\'http://chrome.google.com\'>Google Chrome</a>, <a href=\'http://www.apple.com/safari/\'>Apple Safari</a>, or <a href=\'http://getfirefox.com\'>Mozilla Firefox</a>.\n\t\t\t</p>\n\t\t\t\n\t\t</div>\n\t\t\n\t\t<div id=\'content_box\'>\n\t\t\n\t\t\t<div id=\'left\'>\n\t\t\t\t<form action="%s" method="post" class=\'spi-form\'>\n\t\t\t\t\t%s\n\t\t\t\t\t<input type=\'submit\' value=\'Log In\' id=\'logon-button\' />\n\t\t\t\t</form>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div id=\'spacer\'></div>\n\t\t\t\n\t\t\t<div id=\'right\'>\n\t\t\t\t<div id=\'ws_logo\'>\n\t\t\t\t\t<div>' % (
            context.call(l_link, 'auth/login', action='spi-phase2'), 
            context.call(l_renderForm, l_logon_form, True, True), 
        )
        if l_notice:
            if 0: yield None
            yield u"<div id='notice'><div><span>%s</span></div></div>" % (
                l_notice, 
            )
        yield u"<img src='/assets/img/static/layout/ws-ucr-beta.png' alt='[wire] stone - Universal Content Repository, Beta' />\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\t\t\n\t\t</div>\n\t\t\n\t</div>\n</div>\n"

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Login'

    blocks = {'_wrapper': block__wrapper, 'title': block_title}
    debug_info = '1=9&2=12&6=21&22=28&23=29&33=31&4=38'
    return locals()