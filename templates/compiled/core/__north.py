from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/__north.html'

    def root(context, environment=environment):
        l_asset = context.resolve('asset')
        l_tpl = context.resolve('tpl')
        l_page = context.resolve('page')
        if 0: yield None
        template = environment.get_template('core/__meta.html', 'source/core/__north.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\n<!-- Stylesheets -->\n<link href=\'http://fonts.googleapis.com/css?family=Maven+Pro:regular,bold,900\' rel=\'stylesheet\' type=\'text/css\'>\n<!-- <link href=\'http://fonts.googleapis.com/css?family=Pacifico&v1\' rel=\'stylesheet\' type=\'text/css\'> -->\n<link href=\'http://fonts.googleapis.com/css?family=Dancing+Script&v2\' rel=\'stylesheet\' type=\'text/css\'>\n\n<!-- Legacy Stylesheets \n<link rel="stylesheet" href="/assets/style/static/spi/legacy.css">-->\n\n'
        if environment.getattr(l_page, 'ie'):
            if 0: yield None
            yield u'\n\t<link rel="stylesheet" href="%s">\n' % (
                context.call(environment.getattr(l_asset, 'style'), 'ie', 'compiled'), 
            )
        yield u'\n\n'
        if environment.getattr(l_tpl, 'dependencies'):
            if 0: yield None
            yield u'\n'
            l_off = context.resolve('off')
            if 0: yield None
            t_1 = context.eval_ctx.save()
            context.eval_ctx.autoescape = l_off
            yield u'%s%s%s' % (
                (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n\t')), 
                (context.eval_ctx.autoescape and escape or to_string)(environment.getattr(environment.getattr(l_tpl, 'dependencies'), 'north')), 
                (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n')), 
            )
            context.eval_ctx.revert(t_1)
            yield u'\n'

    blocks = {}
    debug_info = '1=11&11=15&12=18&15=21&16=29&17=30'
    return locals()