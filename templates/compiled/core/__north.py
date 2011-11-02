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
        yield u'\n\n<title>'
        for event in context.blocks['title'][0](context):
            yield event
        yield u" - stonerhub, by [wire] stone</title>\n\n<!-- Stylesheets -->\n<link href='http://fonts.googleapis.com/css?family=Maven+Pro:regular,bold,900' rel='stylesheet' type='text/css'>\n<!-- <link href='http://fonts.googleapis.com/css?family=Pacifico&v1' rel='stylesheet' type='text/css'> -->\n<link href='http://fonts.googleapis.com/css?family=Dancing+Script&v2' rel='stylesheet' type='text/css'>\n\n"
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

    def block_title(context, environment=environment):
        l_title = context.resolve('title')
        if 0: yield None
        if l_title:
            if 0: yield None
            yield to_string(l_title)

    blocks = {'title': block_title}
    debug_info = '1=11&3=15&10=18&11=21&14=24&15=32&16=33&3=39'
    return locals()