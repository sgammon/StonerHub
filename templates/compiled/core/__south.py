from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/__south.html'

    def root(context, environment=environment):
        l_util = context.resolve('util')
        l_api = context.resolve('api')
        l_asset = context.resolve('asset')
        l_render_page_object = context.resolve('render_page_object')
        l_tpl = context.resolve('tpl')
        l_page = context.resolve('page')
        if 0: yield None
        yield u'<script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n<script>window.jQuery || document.write(\'<script src="js/libs/jquery-1.6.2.min.js"><\\/script>\')</script>\n\n<!-- Base Scripts -->\n<script src="%s"></script>\n<script src="%s"></script>\n\n<!-- Project Scripts -->\n\n' % (
            context.call(environment.getattr(l_asset, 'script'), 'modernizr', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'base', 'apptools'), 
        )
        if environment.getattr(l_tpl, 'dependencies'):
            if 0: yield None
            yield u'\n'
            l_off = context.resolve('off')
            if 0: yield None
            t_1 = context.eval_ctx.save()
            context.eval_ctx.autoescape = l_off
            yield u'%s%s%s' % (
                (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n\t')), 
                (context.eval_ctx.autoescape and escape or to_string)(environment.getattr(environment.getattr(l_tpl, 'dependencies'), 'south')), 
                (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n')), 
            )
            context.eval_ctx.revert(t_1)
            yield u'\n'
        yield u'\n\n'
        if environment.getattr(l_page, 'analytics'):
            if 0: yield None
            yield u'\n<script>\n\t'
            template = environment.get_template('snippets/google_analytics.js', 'source/core/__south.html')
            for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                yield event
            yield u'\n</script>\n'
        yield u'\n\n<!--[if lt IE 7 ]>\n\t<script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.2/CFInstall.min.js"></script>\n\t<script>window.attachEvent("onload",function(){CFInstall.check({mode:"overlay"})})</script>\n<![endif]-->\n\n'
        if environment.getattr(l_page, 'services'):
            if 0: yield None
            yield u"\n<script type='text/javascript'>\n\t"
            included_template = environment.get_template('macros/page_object.js', 'source/core/__south.html').module
            l_render_page_object = getattr(included_template, 'render_page_object', missing)
            if l_render_page_object is missing:
                l_render_page_object = environment.undefined("the template %r (imported on line 29 in 'source/core/__south.html') does not export the requested name 'render_page_object'" % included_template.__name__, name='render_page_object')
            context.vars['render_page_object'] = l_render_page_object
            context.exported_vars.discard('render_page_object')
            yield u'\n\t%s\n</script>\n' % (
                context.call(l_render_page_object, environment.getattr(environment.getattr(l_page, 'services'), 'services_manifest'), environment.getattr(environment.getattr(l_page, 'services'), 'config'), l_util, environment.getattr(l_api, 'users')), 
            )

    blocks = {}
    debug_info = '5=15&6=16&10=18&11=26&12=27&16=33&18=36&27=41&29=44&30=51'
    return locals()