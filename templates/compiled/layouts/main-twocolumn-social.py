from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main-twocolumn-social.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/main-twocolumn-social.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/layouts/main-twocolumn-social.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/layouts/main-twocolumn-social.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        l_content_item = context.resolve('content_item')
        l_len = context.resolve('len')
        l_comments = context.resolve('comments')
        if 0: yield None
        yield u'\n\n\n\n<div class="col full">\n\n\t<div class="m-trbl">\n\t\t\n\t\t<div id="content_header" class="header">\n\t\t\t'
        for event in context.blocks['header'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\n\n\n\n<div class="col threequarters clear">\n\n\t<div id=\'content_body\' class="m-rbl">\n\t\t\n\t\t<div id=\'content_body_content\' class="content">\n\t\t\t'
        for event in context.blocks['content_body_header'][0](context):
            yield event
        yield u'\t\t\t\t\n\t\t\t'
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t</div>\n\n</div>\n\n<div id=\'sidebar\' class="col quarter">\n\t\n\t<div class="m-rb">\n\t\t\n\t\t<div id=\'sidebar_header\'>\n\t\t\t'
        for event in context.blocks['sidebar_header'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t\n\t\t<div id='sidebar_content'>\n\t\t\t"
        for event in context.blocks['sidebar_content'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t\n\t\n\t\t<div id='socialComments'>\n\t\t\t<h2><span class='iconButtonBox commentTextButtonBox'>Comments (<span class='commentCount'>%s</span>):</span></h2>\n\t\n\t\t\t<div id='commentsBox'>\n\t\n\t\t\t\t<div id='commentsContainer'>\t\t\t\n\t\t\t\t" % (
            environment.getattr(l_content_item, 'comment_count'), 
        )
        if context.call(l_len, l_comments) > 0:
            if 0: yield None
            yield u'\n\t\t\t\t\n\t\t\t\t\t'
            l_comment = missing
            l_util = context.resolve('util')
            for l_comment in l_comments:
                if 0: yield None
                yield u'\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t\t\t<div class=\'commentBox\' id=\'%s\'>\n\t\t\t\t\t\t\t<div class=\'floatleft profilepic\'>\n\t\t\t\t\t\t\t\t<img src=\'%s\' alt=\'dummy profile pic\' />\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\'floatleft commentBody\'>\n\t\t\t\t\t\t\t\t<div class=\'commentText\'><a href="#">%s %s</a> %s</div><div class=\'commentTagline\'>%s - <a href="#" class=\'commentDelete\' onclick=\'deleteComment("%s");\'>Delete</a></div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\'clearboth\'></div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t' % (
                    context.call(environment.getattr(l_comment, 'key')), 
                    context.call(environment.getattr(environment.getattr(l_comment, 'user'), 'profilePicHref'), '=s48-c'), 
                    environment.getattr(environment.getattr(l_comment, 'user'), 'firstname'), 
                    environment.getattr(environment.getattr(l_comment, 'user'), 'lastname'), 
                    environment.getattr(l_comment, 'text'), 
                    context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(l_comment, 'createdAt')), 
                    context.call(environment.getattr(l_comment, 'key')), 
                )
            l_comment = missing
            yield u'\n\t\t\t\t\t\n\t\t\t\t'
        yield u"\n\t\t\t\t</div>\t\t\t\n\t\t\t\n\t\t\t\t<div class='commentBox' id='addCommentBox'>\n\t\t\t\t\t<form action='#' method='post'>\n\t\t\t\t\t\t<textarea name='body' id='commentBodyInput'>Write a comment...</textarea><br />\n\t\t\t\t\t\t<div class='floatright' id='commentButton'><span class='iconButtonBox commentButtonBox'><a href='#' id='commentAction' onclick='makeComment();'>Comment</a></span></div>\n\t\t\t\t\t\t<div class='clearboth'></div>\n\t\t\t\t\t</form>\n\t\t\t\t</div>\t\t\t\n\t\t\t\t\n\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t\t\n\t</div>\n\t\n</div>\n\n\n"

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    def block_header(context, environment=environment):
        if 0: yield None

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Header</p>'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Sidebar Content</p>'

    blocks = {'body': block_body, 'content_body_header': block_content_body_header, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&2=12&4=21&13=27&27=30&29=33&40=36&44=39&49=42&54=44&56=49&59=52&61=53&64=54&27=64&29=68&13=72&40=75&44=79'
    return locals()