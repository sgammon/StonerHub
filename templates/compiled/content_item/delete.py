from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content_item/delete.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/content_item/delete.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        l_repo = context.resolve('repo')
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n<div id=\'content_body_padding\'>\n\t\n\t<h2><a href="%s">&lt; Cancel and return to viewer</a></h2>\n\t<br />\n\t<br />\n\t\n\t<form action="%s" method=\'post\'>\n\t<h2>Are you sure you wish to delete the content item "%s"?</h2><br /><br />\n\t\t<input type=\'hidden\' name=\'delete_confirm\' value=\'true\' />\n\t\t<br />\n\t\t<div><a href="%s">Cancel</a> | <input type=\'submit\' value=\'Delete\' /></div>\n\t</form>\n</div>\n' % (
            context.call(l_link, 'content-item-view', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name')), key=context.call(environment.getattr(l_content_item, 'key'))), 
            context.call(l_link, 'content-item-delete', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name')), key=context.call(environment.getattr(l_content_item, 'key'))), 
            environment.getattr(l_content_item, 'title'), 
            context.call(l_link, 'content-item-view', repo=context.call(environment.getattr(context.call(environment.getattr(l_repo, 'key')), 'name')), key=context.call(environment.getattr(l_content_item, 'key'))), 
        )

    def block_header(context, environment=environment):
        l_content_item = context.resolve('content_item')
        if 0: yield None
        yield u'\n\t\t<h1>%s</h1> <span>%s - %s</span>\n' % (
            environment.getattr(l_content_item, 'title'), 
            environment.getattr(environment.getattr(l_content_item, 'type'), 'name'), 
            environment.getattr(environment.getattr(l_content_item, 'format'), 'name'), 
        )

    def block_title(context, environment=environment):
        l_content_item = context.resolve('content_item')
        if 0: yield None
        yield to_string(environment.getattr(l_content_item, 'title'))
        yield u' - Delete'

    blocks = {'content': block_content, 'header': block_header, 'title': block_title}
    debug_info = '1=9&16=15&19=21&23=22&24=23&27=24&9=27&10=31&4=36'
    return locals()