from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/superbar.html'

    def root(context, environment=environment):
        l_sys = context.resolve('sys')
        l_link = context.resolve('link')
        l_social = context.resolve('social')
        l_len = context.resolve('len')
        t_1 = environment.filters['truncate']
        if 0: yield None
        yield u'<div id=\'left\'>\n\n\t<div class="navbar">\n\n\t\t<ul id=\'unregisteredNav\' class=\''
        if environment.getattr(environment.getattr(l_sys, 'security'), 'user') != None:
            if 0: yield None
            yield u'hidden'
        yield u"'>\n\t\t\t<li class='nolink'>Account Registration</li>\t\t\t\n\t\t</ul>\n\n\n\t\t<ul id='registeredNav' class='"
        if environment.getattr(environment.getattr(l_sys, 'security'), 'user') == None:
            if 0: yield None
            yield u'hidden'
        yield u"'>\n\t\t"
        l_nav_count = context.call(l_len, environment.getattr(environment.getattr(environment.getattr(l_sys, 'elements'), 'superbar'), 'navigation'))
        context.vars['nav_count'] = l_nav_count
        context.exported_vars.add('nav_count')
        yield u'\n\n\t\t'
        l_title = l_subnav_count = l_href = l_label = l_subnav = missing
        l_subnav_count = context.resolve('subnav_count')
        for (l_label, l_title, l_href, l_subnav), l_loop in LoopContext(environment.getattr(environment.getattr(environment.getattr(l_sys, 'elements'), 'superbar'), 'navigation')):
            if 0: yield None
            yield u'\n\n\t\t\t'
            if environment.getattr(environment.getattr(l_sys, 'request'), 'path') == l_href:
                if 0: yield None
                yield u"\n\t\t\t\t<li><a href='%s'>%s</a></li>\n\t\t\t" % (
                    l_href, 
                    l_label, 
                )
            else:
                if 0: yield None
                yield u'\n\t\t\t\t'
                if l_subnav != False:
                    if 0: yield None
                    yield u'\n\t\t\t\t<li><a href="%s">%s</a>\n\t\t\t\t\t<ul class=\'subnav leftsub\'>\n\t\t\t\t\t\t' % (
                        l_href, 
                        l_label, 
                    )
                    l_subnav_count = context.call(l_len, l_subnav)
                    t_2 = l_href
                    t_3 = l_label
                    t_4 = l_loop
                    t_5 = l_title
                    for (l_label, l_title, l_href), l_loop in LoopContext(l_subnav):
                        if 0: yield None
                        yield u'<li'
                        if environment.getattr(l_loop, 'index') == l_subnav_count:
                            if 0: yield None
                            yield u" class='last'"
                        yield u'>'
                        if l_href != False:
                            if 0: yield None
                            yield u'<a href="%s">' % (
                                l_href, 
                            )
                        yield to_string(l_label)
                        if l_href != False:
                            if 0: yield None
                            yield u'</a>'
                        yield u'</li>'
                    l_title = t_5
                    l_href = t_2
                    l_loop = t_4
                    l_label = t_3
                    yield u'</ul>\n\n\t\t\t\t'
                else:
                    if 0: yield None
                    yield u'\n\t\t\t\t\t<li>'
                    if l_href != False:
                        if 0: yield None
                        yield u'<a href="%s" title="%s">' % (
                            l_href, 
                            l_title, 
                        )
                    yield to_string(l_label)
                    if l_href != False:
                        if 0: yield None
                        yield u'</a>'
                    yield u'\n\t\t\t\t</li>\n\t\t\t\t'
                yield u'\n\t\t\t'
            yield u'\n\n\t\t'
        l_title = l_subnav_count = l_href = l_label = l_subnav = missing
        yield u'\n\t\t</ul>\n\t</div>\n</div>\n\n<div id=\'right\'>\n\t<div class=\'navbar floatright\' id=\'utilbar\'>\n\t\t\n\t\t<ul id=\'userUnregisteredNav\' class="'
        if environment.getattr(environment.getattr(l_sys, 'security'), 'user') != None:
            if 0: yield None
            yield u'hidden'
        yield u'">\n\t\t\t<li class=\'navButton\'><a href="%s">Unregistered User</a></li>\n\t\t</ul>\n\t\n\t\t<ul id=\'userUtilNav\' class="' % (
            context.call(l_link, 'auth/signup'), 
        )
        if environment.getattr(environment.getattr(l_sys, 'security'), 'user') == None:
            if 0: yield None
            yield u'hidden'
        yield u'">\n\t\t\t\t<li class=\'navButton\'><a class=\'navUsername\' href="%s">%s %s</a>\n\t\t\t\t\t' % (
            context.call(l_link, 'user-profile'), 
            environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'firstname'), 
            environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'lastname'), 
        )
        if environment.getattr(environment.getattr(l_sys, 'security'), 'user') != None:
            if 0: yield None
            yield u'\n\t\t\t\t\t\t<ul class=\'subnav rightsub\'>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<div class=\'miniProfileBadge\'>\n\t\t\t\t\t\t\t\t\t<div class=\'floatleft navProfilePic\'>\n\t\t\t\t\t\t\t\t\t\t<a href="%s" class=\'avatarHref\'><img src="' % (
                context.call(l_link, 'user-profile'), 
            )
            if context.call(environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'profilePicHref'), '=s56-c') != False:
                if 0: yield None
                yield to_string(context.call(environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'profilePicHref'), '=s56-c'))
            else:
                if 0: yield None
                yield u'/assets/img/static/layout/avatar.jpg'
            yield u'" /></a>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class=\'floatleft navProfileLinks\'>\n\t\t\t\t\t\t\t\t\t\t<p><a href="%s">Profile</a> (<a href=\'#\'>Edit</a>)</p>\n\t\t\t\t\t\t\t\t\t\t<p><a href="%s">Notifications</a></p>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class=\'clearboth\'></div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</li>' % (
                context.call(l_link, 'user-profile'), 
                context.call(l_link, 'user-notifications'), 
            )
            if environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'perm_sys_admin') == True:
                if 0: yield None
                yield u'<li><a href="%s">Management Console</a></li>' % (
                    context.call(l_link, 'admin-index'), 
                )
            if environment.getattr(environment.getattr(environment.getattr(l_sys, 'security'), 'user'), 'perm_dev_admin') == True:
                if 0: yield None
                yield u'<li><a href="%s">Development Console</a></li>' % (
                    context.call(l_link, 'dev-index'), 
                )
            yield u'<li><a href="%s">Settings</a></li>\n\t\t\t\t\t\t\t<li class=\'last\'><a href="%s">Log Out</a></li>\t\t\t\t\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t' % (
                context.call(l_link, 'user-settings'), 
                context.call(l_link, 'auth/logout'), 
            )
        yield u'\n\t\t\t\t</li>\n\t\t\t\t\n\t\t\t\t<li class=\'navButton navUnreadNotifications\'><a href="%s"><span class=\'navUserNotificationsCount\'>' % (
            context.call(l_link, 'user-notifications'), 
        )
        if environment.getattr(l_social, 'notifications') == False:
            if 0: yield None
            yield u'0'
        else:
            if 0: yield None
            yield to_string(environment.getattr(environment.getattr(l_social, 'notifications'), 'count'))
        yield u'</span></a>\n\t\t\t\t\t<div id="notifications-pane">\n\t\t\t\t\t\t\n\t\t\t\t\t\t'
        if environment.getattr(l_social, 'notifications') != False:
            if 0: yield None
            yield u'\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t'
            if context.call(l_len, environment.getattr(environment.getattr(l_social, 'notifications'), 'uploads')) > 0:
                if 0: yield None
                yield u'\n\t\t\t\t\t\t\t<div class="group uploads-group">\n\t\t\t\t\t\t\t\t<div class="group-title">Uploads</div>\n\n\t\t\t\t\t\t\t\t'
                l_upload = missing
                l_util = context.resolve('util')
                for l_upload in environment.getattr(environment.getattr(l_social, 'notifications'), 'uploads'):
                    if 0: yield None
                    yield u'\n\t\t\t\t\t\t\t\t<div class="listing">\n\t\t\t\t\t\t\t\t\t<div class="listing-title"><a href="%s">%s</a></div>\n\t\t\t\t\t\t\t\t\t<div class="listing-sub-text">%s</div>\n\t\t\t\t\t\t\t\t\t<div class="listing-right-text">%s</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t' % (
                        context.call(l_link, 'content-create', inject=1, queued=context.call(environment.getattr(environment.getattr(l_upload, 'queued_blob'), 'key'))), 
                        t_1(environment.getattr(environment.getattr(l_upload, 'queued_blob'), 'title'), 40), 
                        t_1(environment.getattr(environment.getattr(environment.getattr(l_upload, 'queued_blob'), 'blob'), 'filename'), 30), 
                        context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'byteconvert'), environment.getattr(environment.getattr(environment.getattr(l_upload, 'queued_blob'), 'blob'), 'size'), 2), 
                    )
                l_upload = missing
                yield u'\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t<!--<div class="listing">\n\t\t\t\t\t\t\t\t\t<div class="listing-title">National Marketing Report is uploaded</div>\n\t\t\t\t\t\t\t\t\t<div class="listing-sub-text">nat.marketing.rep.2011.pdf</div>\n\t\t\t\t\t\t\t\t\t<div class="listing-right-text">232K</div>\n\t\t\t\t\t\t\t\t</div>-->\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t'
            yield u'\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t'
            if context.call(l_len, environment.getattr(environment.getattr(l_social, 'notifications'), 'actions')) > 0:
                if 0: yield None
                yield u'\n\t\t\t\t\t\t\t<div class="group notifications-group">\n\t\t\t\t\t\t\t\t<div class="group-title">Notifications</div>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t'
                l_notification = missing
                l_util = context.resolve('util')
                for l_notification in environment.getattr(environment.getattr(l_social, 'notifications'), 'actions'):
                    if 0: yield None
                    yield u'\n\t\t\t\t\t\t\t\t<div class="listing comment-listing">\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t<div class="listing-title"><a href="%s">%s</a> %s...</div>\n\t\t\t\t\t\t\t\t\t<div class="listing-sub-text"><a title="%s" href="%s">%s</a></div>\n\t\t\t\t\t\t\t\t\t<div class="listing-right-text">%s</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t' % (
                        context.call(l_link, 'user-public-profile', username=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_notification, 'action'), 'user'), 'key')), 'name'))), 
                        environment.getattr(environment.getattr(environment.getattr(l_notification, 'action'), 'user'), 'firstname'), 
                        environment.getattr(l_notification, 'action_verb'), 
                        environment.getattr(environment.getattr(environment.getattr(l_notification, 'action'), 'content_item'), 'title'), 
                        context.call(l_link, 'content-item-view', repo=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_notification, 'action'), 'content_item'), 'repository'), 'key')), 'name')), key=context.call(environment.getattr(environment.getattr(environment.getattr(l_notification, 'action'), 'content_item'), 'key'))), 
                        t_1(environment.getattr(environment.getattr(environment.getattr(l_notification, 'action'), 'content_item'), 'title'), 20), 
                        context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(environment.getattr(l_notification, 'action'), 'createdAt')), 
                    )
                l_notification = missing
                yield u'\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t<!--<div class="listing like-listing">\n\t\t\t\t\t\t\t\t\t<div class="listing-title"><a href"">Paul</a> likes... </div>\n\t\t\t\t\t\t\t\t\t<div class="listing-sub-text">Internal Finacial Report 2010</div>\n\t\t\t\t\t\t\t\t\t<div class="listing-right-text">8/11</div>\n\t\t\t\t\t\t\t\t</div>-->\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t'
            yield u'\n\t\t\t\t\t\t'
        yield u'\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="close-link">Close</div>\n\t\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t</li>\n\n\t\t\t\t<li class=\'navButton wirestoneNavButton\'>\n\t\t\t\t\t<a href=\'#\'><span>[wire] stone</span></a>\n\t\t\t\t\t<ul class=\'subnav rightsub\'>\n\t\t\t\t\t\t<li><a href="http://intranet.wirestone.internal/Pages/Welcome.aspx">Intranet (Internal Only)</a></li>\n\t\t\t\t\t\t<li><a href="https://mail.wirestone.com/">Webmail</a></li>\n\t\t\t\t\t\t<li class=\'last\'><a href="http://www.wire-stone.com">Public Site</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</li>\t\n\t\t</ul>\n\t</div>\n</div>'

    blocks = {}
    debug_info = '5=14&10=18&11=22&13=28&15=31&16=34&18=40&19=43&21=46&22=51&23=54&28=76&41=91&42=95&45=97&46=101&47=105&52=108&55=117&56=118&61=120&62=123&64=125&65=128&67=131&68=132&73=135&76=144&78=147&82=152&84=155&85=157&86=158&99=163&103=168&106=171&107=174&108=177'
    return locals()