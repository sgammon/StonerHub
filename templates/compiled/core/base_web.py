from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/base_web.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/__base.html', 'source/core/base_web.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block__top(context, environment=environment):
        if 0: yield None
        yield u'\n<div id="wrapper">\n\t'
        for event in context.blocks['_wrapper'][0](context):
            yield event
        yield u'\n</div> <!--! end of #container -->\n'

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    def block__wrapper(context, environment=environment):
        if 0: yield None
        yield u"\n\n\t<div id='superbar'>\n\t\t"
        template = environment.get_template('snippets/superbar.html', 'source/core/base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u"\n\t\t<div class='clear'></div>\n\t</div>\n\t\n\t<div id='content'>\n\t\t"
        for event in context.blocks['body'][0](context):
            yield event
        yield u'\n\t</div>\n\t\n\t'

    blocks = {'_top': block__top, 'body': block_body, '_wrapper': block__wrapper}
    debug_info = '1=9&3=15&5=18&13=22&5=26&8=29&13=33'
    return locals()