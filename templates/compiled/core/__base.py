from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/__base.html'

    def root(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'<!doctype html>\n\n<html lang="en"'
        if environment.getattr(environment.getattr(l_page, 'appcache'), 'enabled') == True:
            if 0: yield None
            yield u' manifest="%s"' % (
                environment.getattr(environment.getattr(l_page, 'appcache'), 'location'), 
            )
        yield u'>\n\n<head>\n\t'
        for event in context.blocks['prenorth'][0](context):
            yield event
        yield u'\t\n\t'
        template = environment.get_template('core/__north.html', 'source/core/__base.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t'
        for event in context.blocks['postnorth'][0](context):
            yield event
        yield u'\n</head>\n\n<body>\n'
        for event in context.blocks['_top'][0](context):
            yield event
        yield u'\n\n'
        for event in context.blocks['presouth'][0](context):
            yield event
        yield u'\n'
        template = environment.get_template('core/__south.html', 'source/core/__base.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n'
        for event in context.blocks['postsouth'][0](context):
            yield event
        yield u'\n</body>\n</html>'

    def block_prenorth(context, environment=environment):
        if 0: yield None

    def block__top(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_presouth(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_postsouth(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_postnorth(context, environment=environment):
        if 0: yield None

    blocks = {'prenorth': block_prenorth, '_top': block__top, 'presouth': block_presouth, 'postsouth': block_postsouth, 'postnorth': block_postnorth}
    debug_info = '3=10&6=16&7=19&8=23&12=26&15=29&17=32&18=36&6=40&12=43&15=47&18=51&8=55'
    return locals()