from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/memcache.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/memcache.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_link = context.resolve('link')
        l_stats = context.resolve('stats')
        l_flush = context.resolve('flush')
        if 0: yield None
        yield u"\n\n<div class='box'>\n\n\t<h2>Global Cache Stats:</h2>\n\t<ul>\n\t\t<li><b>Hits:</b> %s</li>\n\t\t<li><b>Misses:</b> %s</li>\t\t\n\t\t<li><b>Byte Hits:</b> %s</li>\n\t\t<li><b>Total Items:</b> %s</li>\t\n\t\t<li><b>Total Bytes:</b> %s</li>\t\t\t\n\t\t<li><b>Oldest Item:</b> %s seconds old</li>\t\t\n\t</ul>\n\t\n\t<br />\n\t<h2>Global Flush:</h2>\n\t\n\t" % (
            environment.getattr(l_stats, 'hits'), 
            environment.getattr(l_stats, 'misses'), 
            environment.getattr(l_stats, 'byte_hits'), 
            environment.getattr(l_stats, 'items'), 
            environment.getattr(l_stats, 'bytes'), 
            environment.getattr(l_stats, 'oldest_item_age'), 
        )
        if l_flush == True:
            if 0: yield None
            yield u"\n\t\t<br /><p class='notice'>Memcache flushed successfully.</p>\n\t"
        yield u'\n\t\n\t<form action="%s" method=\'post\'>\n\t\t<input type=\'hidden\' name=\'action\' value=\'flush_all\' />\n\t\t<input type=\'submit\' value=\'Flush Memcache\'>\n\t</form>\n\n</div>\n\n\n' % (
            context.call(l_link, 'dev-cache'), 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'<h1>Memcache Console</h1>'

    def block_module(context, environment=environment):
        if 0: yield None
        yield u'Cache Management'

    blocks = {'content': block_content, 'header': block_header, 'module': block_module}
    debug_info = '1=9&7=15&13=21&14=22&15=23&16=24&17=25&18=26&24=28&28=32&3=35&5=39'
    return locals()