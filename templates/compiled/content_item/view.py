from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content_item/view.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn-social.html', 'source/content_item/view.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_prenorth(context, environment=environment):
        l_sys = context.resolve('sys')
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n<script type="text/javascript">\n\n\tvar PageObj = {\n\t\n\t\t\'ci_key\':"%s",\n\t\t\'like_action_url\': "%s",\n\t\t\'unlike_action_url\': "%s",\n\t\t\'comment_action_url\': "%s",\n\t\t\'uncomment_action_url\': "%s",\t\n\t\t\'wusr_key\': "%s",\n\t\t\'user\': {\'firstname\': \'%s\',\n\t\t\t\t \'lastname\': \'%s\',\n\t\t\t\t \'profile_href\': "%s",\n\t\t\t\t \'profile_pic_href\': "%s",\n\t\t\t\t \'username\': "%s"},\n\t\t\'content_item\': {\'comment_count\': %s}\n\t\t\n\t};\n\n</script>\n' % (
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
            context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'key')), 'name')), 
            environment.getattr(l_content_item, 'comment_count'), 
        )

    def block_title(context, environment=environment):
        l_content_item = context.resolve('content_item')
        if 0: yield None
        yield u'%s - %s Repository' % (
            environment.getattr(l_content_item, 'title'), 
            environment.getattr(environment.getattr(l_content_item, 'repository'), 'name'), 
        )

    def block_postsouth(context, environment=environment):
        if 0: yield None
        yield u'\n<script type="text/javascript">\n\tdialogOptions = {\n\n\t\ttype: \'ajax\',\n\t\tautoDimensions: false,\n\t\twidth:600,\n\t\tscrolling: \'no\',\n\t\ttitleShow: false,\n\t\topacity: true,\n\t\theight: 300,\n\t\tpadding: 0,\n\t\tmargin: 0,\n\t\tshowNavArrows: false,\n\t\tmodal: false\n\t\n\t};\n\tpopins = $(".ciPopin").fancybox(dialogOptions);\n</script>\n'

    def block_content(context, environment=environment):
        l_util = context.resolve('util')
        l_tags = context.resolve('tags')
        l_sys = context.resolve('sys')
        l_spi = context.resolve('spi')
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\n\t<div id=\'shareBox\' class=\'inline floatright\'><a href="%s" class=\'ciPopin\'><span class=\'iconButtonBox shareButtonBox\'>Share</span></a></div>\n\n\n\t<div id=\'likeBox\' class=\'inline floatright\'>\n\t\n\t\t' % (
            context.call(l_link, 'ajax-social-sharebox', ci=context.call(environment.getattr(l_content_item, 'key')), user=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'key')), 'name'))), 
        )
        if context.call(environment.getattr(l_content_item, 'currentUserLike')) == True:
            if 0: yield None
            yield u'\n\t\n\t\t\t'
            if (environment.getattr(l_content_item, 'like_count') - 1) == 0:
                if 0: yield None
                yield u'\n\t\t\t\t<span id=\'youLike\'><a href="%s">You</a> like this.</span>\n\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u'\n\t\n\t\t\t'
            if (environment.getattr(l_content_item, 'like_count') - 1) == 1:
                if 0: yield None
                yield u'\n\t\t\t\t<span id=\'youLike\'><a href="%s">You</a> + <a href=\'#\' class=\'ciPopin\'>1 other person</a> like this.</span>\n\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u'\n\n\t\t\t'
            if (environment.getattr(l_content_item, 'like_count') - 1) > 1:
                if 0: yield None
                yield u'\n\t\t\t\t<span id=\'youLike\'><a href="%s">You</a> + <a href=\'#\' class=\'ciPopin\'>%s people</a> like this.</span>\n\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                    (environment.getattr(l_content_item, 'like_count') - 1), 
                )
            yield u"\n\n\t\t\t<a href='#' id='likeUnlikeAction' class='unlikeButton'><span class='iconButtonBox unlikeButtonBox'>Unlike</span></a>\n\t\t"
        else:
            if 0: yield None
            yield u'\n\t\t\t'
            if environment.getattr(l_content_item, 'like_count') == 1:
                if 0: yield None
                yield u'\n\t\t\t\t<span id=\'youLike\' class=\'hidden\'><a href="%s">You</a> + <a href=\'#\' class=\'ciPopin\'>1 other person</a> like this.</span>\n\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u'\n\t\n\t\t\t'
            if environment.getattr(l_content_item, 'like_count') > 1:
                if 0: yield None
                yield u'\n\t\t\t\t<span id=\'youLike\' class=\'hidden\'><a href="%s">You</a> + <a href=\'#\' class=\'ciPopin\'>%s people</a> like this.</span>\n\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                    environment.getattr(l_content_item, 'like_count'), 
                )
            else:
                if 0: yield None
                yield u'\n\t\t\t\t<span id=\'youLike\' class=\'hidden\'><a href="%s">You</a> like this.</span>\n\t\t\t' % (
                    context.call(l_link, 'user-profile'), 
                )
            yield u"\n\t\t\t\t<a href='#' onclick='likeUnlike();' id='likeUnlikeAction' class='likeButton'><span class='iconButtonBox likeButtonBox'>Like</span></a>\n\t\t"
        yield u'\n\t\n\t</div>\n\t\n\t'
        template = environment.get_or_select_template(context.call(environment.getattr(l_spi, 'resolve_ci_viewer_extension'), environment.getattr(l_content_item, 'type'), environment.getattr(l_content_item, 'format')), 'source/content_item/view.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u"\n\n\t<div id='ci_ext_Tags'>\n\t\t<ul id='taggingInfo' class='nakedList'>\n\t\t\t"
        if context.call(environment.getattr(l_util, 'len'), l_tags) > 0:
            if 0: yield None
            yield u'\n\t\t\t\t'
            l_tag = missing
            for l_tag in l_tags:
                if 0: yield None
                yield u'\n\t\t\t\t\t<li><span class=\'iconButtonBox tag-%s\'><a href="%s" title=\'\'>%s</a></li>\n\t\t\t\t' % (
                    context.call(environment.getattr(l_tag, 'class_name')), 
                    context.call(l_link, 'tag-view', tag=context.call(environment.getattr(l_tag, 'key'))), 
                    environment.getattr(l_tag, 'value'), 
                )
            l_tag = missing
            yield u'\n\t\t\t'
        yield u'\n\t\t\t<li><span class=\'iconButtonBox addTagButtonBox\'><a href="#" class=\'ciPopin\'>add tag...</a></span></li>\n\t\t</ul>\n\t</div>\n\t\n\t<div id=\'ci_ext_Description\'>\n\t\t\n\t\t<h2 class="grid-title">Description</h2>\n\t\t<p>%s</p>\n\n\t</div>\n' % (
            environment.getattr(l_content_item, 'description'), 
        )

    def block_header(context, environment=environment):
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\t\t<h1>%s</h1> \n\t\t\t\t<a href="%s" id=\'contentItemEdit\'>\n\t\t\t\t\t<span class=\'iconButtonBox editButtonBox\'> Edit Info</span></a>\n\t\t\t\t \n\t\t\t\t<a href="%s" id=\'contentItemDownload\'><span class=\'iconButtonBox downloadButtonBox\'> Download</a></span> \n\t\t\t\t\n\t\t\t\t<a href="%s" id=\'contentItemDelete\'>\n\t\t\t\t\t<span class=\'iconButtonBox deleteButtonBox\'> Delete</span></a>\n\t\t\t\t\n' % (
            environment.getattr(l_content_item, 'title'), 
            context.call(l_link, 'content-item-edit', key=context.call(environment.getattr(l_content_item, 'key')), repo=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_content_item, 'repository'), 'key')), 'name'))), 
            context.call(l_link, 'media-download-blob-filename', blobkey=environment.getattr(context.call(environment.getattr(environment.getattr(l_content_item, 'asset'), 'getAsset')), 'key'), filename=environment.getattr(context.call(environment.getattr(l_content_item, 'getAsset')), 'filename')), 
            context.call(l_link, 'content-item-delete', key=context.call(environment.getattr(l_content_item, 'key')), repo=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_content_item, 'repository'), 'key')), 'name'))), 
        )

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u"\n<div class='floatleft'><span class='iconButtonBox infoButtonBox'>Meta</span></div>\n\n\t<div class='floatright'>\n\n\n\t\t<div id='alertsBox' class='inline'>\n\t\t\t<a href='#' id='alertsAction' class='alertsButton'><span class='iconButtonBox alertSubscribeButtonBox'>Alerts</span></a>\n\t\t</div>\n\n\t\t<div id='versionsBox' class='inline'>\n\t\t\t<a href='#' id='versionsAction' class='versionsButton'><span class='iconButtonBox versionsButtonBox'>Versions</span></a>\n\t\t</div>\n\t</div>\n<div class='clearboth'></div>"

    def block_sidebar_content(context, environment=environment):
        l_util = context.resolve('util')
        l_hits = context.resolve('hits')
        l_content_item = context.resolve('content_item')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n<div>\n\t<b>File Info:</b>\n\t<ul id=\'fileInfo\' class=\'nakedList\'>\n\t\t<li><b>File Name:</b> %s</li>\n\t\t<li><b>File Type:</b> %s - %s</li>\n\t\t<li><b>File Size:</b> %s bytes</li>\n\t\t<li><b>Created:</b> %s</li>\n\t\t<li><b>Created By:</b> <a href="%s">%s</a></li>\n\t\t<li><b>Last Modified:</b> %s</li>\n\t\t<li><b>Last Modified By:</b> <a href="%s"> %s</a></li>\t\t\n\t</ul>\n\t<b>Social:</b>\n\t<ul id=\'socialInfo\' class=\'nakedList\'>\n\t\t<li><b>Likes:</b> %s</li>\n\t\t<li><b>Comments:</b> <span class=\'commentCount\'>%s</span></li>\n\t\t<li><b>Views:</b> %s</li>\n\t</ul>\n</div>\n' % (
            environment.getattr(context.call(environment.getattr(l_content_item, 'getAsset')), 'filename'), 
            environment.getattr(environment.getattr(l_content_item, 'type'), 'name'), 
            environment.getattr(environment.getattr(l_content_item, 'format'), 'name'), 
            context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'byteconvert'), environment.getattr(context.call(environment.getattr(l_content_item, 'getAsset')), 'size'), 2), 
            context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(l_content_item, 'createdAt')), 
            context.call(l_link, 'user-public-profile', username=context.call(environment.getattr(environment.getattr(l_content_item, 'createdBy'), 'name'))), 
            context.call(environment.getattr(environment.getattr(l_content_item, 'createdBy'), 'name')), 
            context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(l_content_item, 'modifiedAt')), 
            context.call(l_link, 'user-public-profile', username=context.call(environment.getattr(environment.getattr(l_content_item, 'modifiedBy'), 'name'))), 
            context.call(environment.getattr(environment.getattr(l_content_item, 'modifiedBy'), 'name')), 
            environment.getattr(l_content_item, 'like_count'), 
            environment.getattr(l_content_item, 'comment_count'), 
            l_hits, 
        )

    blocks = {'prenorth': block_prenorth, 'title': block_title, 'postsouth': block_postsouth, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&8=15&13=21&14=22&15=23&16=24&17=25&18=26&19=27&20=28&21=29&22=30&23=31&24=32&4=35&151=43&49=47&51=56&56=58&58=61&59=64&62=67&63=70&66=73&67=76&72=83&73=86&76=89&77=92&79=98&86=102&90=106&91=110&92=113&102=120&35=123&36=128&37=129&40=130&42=131&110=134&129=138&133=145&134=146&135=148&136=149&137=150&138=152&139=153&143=155&144=156&145=157'
    return locals()