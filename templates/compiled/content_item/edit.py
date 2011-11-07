from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content_item/edit.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn-social.html', 'source/content_item/edit.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_prenorth(context, environment=environment):
        l_sys = context.resolve('sys')
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n<script type="text/javascript">\n\n\tvar PageObj = {\n\t\n\t\t\'ci_key\':"%s",\n\t\t\'like_action_url\': "%s",\n\t\t\'unlike_action_url\': "%s",\n\t\t\'comment_action_url\': "%s",\n\t\t\'uncomment_action_url\': "%s",\t\n\t\t\'wusr_key\': "%s",\n\t\t\'user\': {\'firstname\': \'%s\',\n\t\t\t\t \'lastname\': \'%s\',\n\t\t\t\t \'profile_href\': "%s",\n\t\t\t\t \'profile_pic_href\': "%s"},\n\t\t\'content_item\': {\'comment_count\': %s}\n\t\t\n\t};\n\n</script>\n' % (
            context.call(environment.getattr(l_content_item, 'key')), 
            context.call(l_link, 'ajax-social', action='like', document=context.call(environment.getattr(l_content_item, 'key'))), 
            context.call(l_link, 'ajax-social', action='unlike', document=context.call(environment.getattr(l_content_item, 'key'))), 
            context.call(l_link, 'ajax-social', action='comment', document=context.call(environment.getattr(l_content_item, 'key'))), 
            context.call(l_link, 'ajax-social', action='uncomment', document=context.call(environment.getattr(l_content_item, 'key'))), 
            context.call(environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'key')), 
            environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'firstname'), 
            environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'lastname'), 
            context.call(l_link, 'user-profile'), 
            context.call(environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'profilePicHref')), 
            environment.getattr(l_content_item, 'comment_count'), 
        )

    def block_title(context, environment=environment):
        l_content_item = context.resolve('content_item')
        if 0: yield None
        yield to_string(environment.getattr(l_content_item, 'title'))
        yield u' - Edit'

    def block_content(context, environment=environment):
        l_renderForm = context.resolve('renderForm')
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        l_form = context.resolve('form')
        if 0: yield None
        yield u'\n<div id=\'content_body_padding\'>\n\t\t%s\t<span class=\'iconButtonBox cancelButtonBox\'><a href="%s" id=\'contentItemEdit\'>Cancel Edits</a></span>\t\t\t\t\t\t\t\t\n</div>\n' % (
            context.call(l_renderForm, l_form, submit_value='Save'), 
            context.call(l_link, 'content-item-view', key=context.call(environment.getattr(l_content_item, 'key')), repo=context.call(environment.getattr(environment.getattr(l_content_item, 'repository'), 'key'))), 
        )

    def block_header(context, environment=environment):
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u"\n\t\t<h1>%s</h1> <span>%s - %s</span>\n\t\t<div id='likeBox' class='inline'>\n\n\t\t\t" % (
            environment.getattr(l_content_item, 'title'), 
            environment.getattr(environment.getattr(l_content_item, 'type'), 'name'), 
            environment.getattr(environment.getattr(l_content_item, 'format'), 'name'), 
        )
        if context.call(environment.getattr(l_content_item, 'currentUserLike')) == True:
            if 0: yield None
            yield u'\n\n\t\t\t\t'
            if (environment.getattr(l_content_item, 'like_count') - 1) == 0:
                if 0: yield None
                yield u'\n\t\t\t\t\t<span id=\'youLike\'><a href="%s">You</a> like this.</span>\n\t\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u'\n\n\t\t\t\t'
            if (environment.getattr(l_content_item, 'like_count') - 1) == 1:
                if 0: yield None
                yield u'\n\t\t\t\t\t<span id=\'youLike\'><a href="%s">You</a> and </span><a href=\'#\'>1 person</a> like this.\n\t\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u'\n\n\t\t\t\t'
            if (environment.getattr(l_content_item, 'like_count') - 1) > 1:
                if 0: yield None
                yield u'\n\t\t\t\t\t<span id=\'youLike\'><a href="%s">You</a> and </span> <a href=\'#\'>%speople</a> like this.\n\t\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                    (environment.getattr(l_content_item, 'like_count') - 1), 
                )
            yield u"\n\n\t\t\t\t<span class='iconButtonBox unlikeButtonBox'><a href='#' id='likeUnlikeAction' class='unlikeButton'>Unlike</a></span>\n\t\t\t"
        else:
            if 0: yield None
            yield u'\n\t\t\t\t'
            if environment.getattr(l_content_item, 'like_count') == 1:
                if 0: yield None
                yield u'\n\t\t\t\t\t<span id=\'youLike\' class=\'hidden\'><a href="%s">You</a> and </span><a href=\'#\'>%s person</a> likes this.\n\t\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                    environment.getattr(l_content_item, 'like_count'), 
                )
            yield u'\n\n\t\t\t\t'
            if environment.getattr(l_content_item, 'like_count') > 1:
                if 0: yield None
                yield u'\n\t\t\t\t\t<span id=\'youLike\' class=\'hidden\'><a href="%s">You</a> and </span><a href=\'#\'>%s people</a> likes this.\n\t\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                    environment.getattr(l_content_item, 'like_count'), 
                )
            else:
                if 0: yield None
                yield u'\n\t\t\t\t\t<span id=\'youLike\' class=\'hidden\'><a href="%s">You</a> like this.</span>\n\t\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u"\n\t\t\t\t\t<span class='iconButtonBox likeButtonBox'><a href='#' onclick='likeUnlike();' id='likeUnlikeAction' class='likeButton'>Like</a></span>\n\t\t\t"
        yield u"\n\n\t\t</div> | \n\t\t<div id='sharebox' class='inline'><span class='iconButtonBox shareButtonBox'><a href='#'>Share</a></span></div>\n\t\t<div class='clearboth'></div>\n"

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u"<span class='iconButtonBox infoButtonBox'>File Information</span>"

    def block_sidebar_content(context, environment=environment):
        l_util = context.resolve('util')
        l_content_item = context.resolve('content_item')
        if 0: yield None
        yield u"\n<div>\n\t<b>Meta:</b>\n\t<ul id='fileInfo' class='nakedList'>\n\t\t\n\t\t"
        l_asset = context.call(environment.getattr(l_content_item, 'getAsset'))
        yield u'\n\t\t\n\t\t<li><b>File Name:</b> %s</li>\n\t\t<li><b>File Type:</b> %s - %s</li>\n\t\t<li><b>File Size:</b> %s bytes</li>\n\t\t<li><b>Created:</b> %s</li>\n\t\t<li><b>Created By:</b> <a href="#">%s</a></li>\n\t\t<li><b>Last Modified:</b> %s</li>\n\t\t<li><b>Last Modified By:</b> <a href="#"> %s</a></li>\t\t\n\t</ul>\n\t<b>Social:</b>\n\t<ul id=\'socialInfo\' class=\'nakedList\'>\n\t\t<li><b>Likes:</b> %s</li>\n\t\t<li><b>Comments:</b> <span class=\'commentCount\'>%s</span></li>\n\t\t<li><b>Views:</b> %s</li>\n\t</ul>\n\t<b>Tags:</b>\n\t<ul id=\'taggingInfo\' class=\'nakedList\'>\n\t\t<li><b>Tags</b></li>\n\t</ul>\n</div>\n' % (
            environment.getattr(l_asset, 'filename'), 
            environment.getattr(environment.getattr(l_content_item, 'type'), 'name'), 
            environment.getattr(environment.getattr(l_content_item, 'format'), 'name'), 
            context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'byteconvert'), environment.getattr(l_asset, 'size'), 2), 
            context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(l_content_item, 'createdAt')), 
            context.call(environment.getattr(environment.getattr(l_content_item, 'createdBy'), 'name')), 
            context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(l_content_item, 'modifiedAt')), 
            context.call(environment.getattr(environment.getattr(l_content_item, 'modifiedBy'), 'name')), 
            environment.getattr(l_content_item, 'like_count'), 
            environment.getattr(l_content_item, 'comment_count'), 
            environment.getattr(l_content_item, 'view_count'), 
        )

    blocks = {'prenorth': block_prenorth, 'title': block_title, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&8=15&13=21&14=22&15=23&16=24&17=25&18=26&19=27&20=28&21=29&22=30&23=31&4=34&74=40&76=47&34=51&35=56&38=60&40=63&41=66&44=69&45=72&48=75&49=78&54=85&55=88&58=92&59=95&61=101&83=106&88=110&93=115&95=117&96=118&97=120&98=121&99=122&100=123&101=124&105=125&106=126&107=127'
    return locals()