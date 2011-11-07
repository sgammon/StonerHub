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

    def block_prenorth(context, environment=environment):
        if 0: yield None
        yield u'\n<meta name="google-site-verification" content="GNpWBXBMCFjW7thMuE06UvfgI4mktA9EcsevLda9VPU" />\n\n<style>\nbody\n{\n\tfont-family:"Lucida Grande", Arial;\n\tbackground: url(\'/assets/img/static/layout/ws-dark-stripes.png\') repeat transparent;\n}\n.hidden { display:none; }\n#wrapper\n{\n\theight:100%;\n\twidth:100%;\n\tdisplay:table;\n\tposition: relative;\n}\n#content\n{\n\ttop:50%;\n\tdisplay:table-cell;\n\tvertical-align:middle;\n\toverflow:hidden;\n}\n#splash\n{\n\twidth:1000px;\n\theight:300px;\n\tbackground:white;\n\tdisplay:table;\n\tmargin-left:20px;\n\t\n}\n#content_box\n{\n\tdisplay:table-cell;\n\tvertical-align:middle;\n}\n#left\n{\n\tfloat:left;\n\tbackground:white;\n\tpadding-left:15px;\n\tborder:1px solid #c2c3c3;\n\twidth:240px;\n\theight:200px;\n\tmargin-left:30px;\n}\n#right\n{\n\tfloat:left;\n\theight:200px;\n\tpadding-left:20px;\n\tbackground:white;\n}\n#ws_logo\n{\n\twidth:100%;\n\theight:100%;\n\tdisplay:table;\n}\n#ws_logo div\n{\n\tdisplay:table-cell;\n\tvertical-align:middle;\n}\n\n/* === Form styles === */\n#username-box\n{\n\tmargin-top:35px !important;\n\tfont-family:"Lucida Grande", Arial;\n\twidth: 200px;\n}\n#password-box\n{\n\tmargin-top:3px !important;\n\tfont-family:"Lucida Grande", Arial;\n\twidth: 200px;\n}\n#password_1-box\n{\n\twidth:200px;\n}\n#password_2-box\n{\n\twidth:200px;\n}\n#logon-button\n{\n\tmargin-top:10px;\n}\n#notice\n{\n\tdisplay:inline;\n\theight:20px;\n\tpadding:15px;\n\tpadding-left:10px;\n}\n#notice div\n{\t\n\tbackground:yellow;\n\tpadding:3px;\n\tpadding-left:5px;\n\tpadding-right:5px;\n\tmin-width:100px;\n}\n#notice div span\n{\n\tbackground: url(\'/assets/img/static/icons/error.png\') no-repeat 0 50%;\n\tpadding-left:25px;\t\n}\n.unsupportedBrowser\n{\n\topacity:0.35 !important;\n}\n#unsupportedBrowserWarning\n{\n\topacity:0.83;\n\tposition:absolute;\n\twidth:1000px;\n\theight:300px;\n\tbackground:#111;\n}\n#unsupportedBrowserWarning p\n{\n\tbackground:#333;\n\tpadding:3px;\n\tmargin-left:15px;\n\tmargin-right:15px;\n\tcolor:#999;\n}\n#unsupportedBrowserWarning p a\n{\n\tcolor:#E5EBF7;\n}\n#unsupportedBrowserWarning p a:hover\n{\n\tcolor:#111;\n\tbackground:#E5EBF7;\n}\n</style>\n\n'

    def block__wrapper(context, environment=environment):
        l_notice = context.resolve('notice')
        l_renderForm = context.resolve('renderForm')
        l_logon_form = context.resolve('logon_form')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\n\t<div id=\'splash\'>\n\t\t\n\t\t<div id=\'unsupportedBrowserWarning\' class=\'hidden\'>\n\n\t\t\t<p>\n\t\t\t\tUnfortunately, the browser you are using to visit this site is not compatible with one or more required features.<br />\n\t\t\t\tPlease visit this site using either <a href=\'http://chrome.google.com\'>Google Chrome</a>, <a href=\'http://www.apple.com/safari/\'>Apple Safari</a>, or <a href=\'http://getfirefox.com\'>Mozilla Firefox</a>.\n\t\t\t</p>\n\t\t\t\n\t\t</div>\n\t\t\n\t\t<div id=\'content_box\'>\n\t\t\n\t\t\t<div id=\'left\'>\n\t\t\t\t<form action="%s" method="post" class=\'spi-form\'>\n\t\t\t\t\t%s\n\t\t\t\t\t<input type=\'submit\' value=\'Log In\' id=\'logon-button\' />\n\t\t\t\t</form>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div id=\'spacer\'></div>\n\t\t\t\n\t\t\t<div id=\'right\'>\n\t\t\t\t<div id=\'ws_logo\'>\n\t\t\t\t\t<div>' % (
            context.call(l_link, 'auth/login', action='spi-phase2'), 
            context.call(l_renderForm, l_logon_form, True, True), 
        )
        if l_notice:
            if 0: yield None
            yield u"<div id='notice'><div><span>%s</span></div></div>" % (
                l_notice, 
            )
        yield u"<img src='/assets/img/static/layout/ws-ucr-beta.png' alt='[wire] stone - Universal Content Repository, Beta' />\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\t\t\n\t\t</div>\n\t\t\n\t</div>\n\t\n\t<script type='text/javascript'>\n\t\t\n\t\t/*\n\t\tif (!$.browser.webkit) {\n\t\t\t$('#splash').addClass('unsupportedBrowser');\n\t\t\t$('#unsupportedBrowserWarning').removeClass('hidden');\n\t\t}\n\t\t*/\n\t\n\t</script>\n\t\n"

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Login'

    blocks = {'prenorth': block_prenorth, '_wrapper': block__wrapper, 'title': block_title}
    debug_info = '1=9&2=12&6=21&151=25&167=32&168=33&178=35&4=42'
    return locals()