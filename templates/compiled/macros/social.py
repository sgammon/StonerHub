from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/social.html'

    def root(context, environment=environment):
        t_1 = environment.filters['truncate']
        if 0: yield None
        def macro(l_user, l_item, l_you, l_firstname_only, l_link_name, l_link_content, l_timesince):
            t_2 = []
            l_util = context.resolve('util')
            l_link = context.resolve('link')
            pass
            t_2.append(
                u"<div class='activityItem'>", 
            )
            if context.call(environment.getattr(l_item, 'kind')) == 'SocialAction':
                pass
                if context.call(environment.getattr(l_item, 'class_name')) == 'Comment':
                    pass
                    t_2.append(
                        u"<span class='iconButtonBox commentTextButtonBox'>", 
                    )
                if context.call(environment.getattr(l_item, 'class_name')) == 'Like':
                    pass
                    t_2.append(
                        u"<span class='iconButtonBox likeButtonBox'>", 
                    )
                if context.call(environment.getattr(l_item, 'class_name')) == 'Share':
                    pass
                    t_2.append(
                        u"<span class='iconButtonBox shareButtonBox'>", 
                    )
            if context.call(environment.getattr(l_item, 'kind')) == 'ContentItem':
                pass
                t_2.append(
                    u"<span class='iconButtonBox contentItemCreatedButtonBox'>", 
                )
            if context.call(environment.getattr(l_item, 'kind')) == 'QueuedBlob':
                pass
                t_2.append(
                    u"<span class='iconButtonBox uploadedItemButtonBox'>\n\t", 
                )
            t_2.append(
                u'\n\t\n\t', 
            )
            if l_you == True:
                pass
                if l_link_name:
                    pass
                    t_2.extend((
                        u'<a href="', 
                        to_string(context.call(l_link, 'user-profile')), 
                        u'">You</a>', 
                    ))
                else:
                    pass
                    t_2.append(
                        u'You', 
                    )
                t_2.append(
                    u'\n\t\t', 
                )
            else:
                pass
                t_2.append(
                    u'\n\t\t\t', 
                )
                if l_link_name:
                    pass
                    t_2.append(
                        u'\n\t\t\t\t', 
                    )
                    if l_firstname_only:
                        pass
                        t_2.extend((
                            u' \n\t\t\t\t\t<a href="', 
                            to_string(context.call(l_link, 'user-public-profile', username=environment.getattr(l_user, 'username'))), 
                            u'">', 
                            to_string(environment.getattr(l_user, 'firstname')), 
                            u'</a>\n\t\t\t\t', 
                        ))
                    else:
                        pass
                        t_2.extend((
                            u'\n\t\t\t\t\t<a href="', 
                            to_string(context.call(l_link, 'user-public-profile', username=environment.getattr(l_user, 'username'))), 
                            u'">', 
                            to_string(environment.getattr(l_user, 'firstname')), 
                            u' ', 
                            to_string(environment.getattr(l_user, 'lastname')), 
                            u'</a>\n\t\t\t\t', 
                        ))
                    t_2.append(
                        u'\n\t\t\t', 
                    )
                else:
                    pass
                    t_2.append(
                        u'\n\t\t\t\t', 
                    )
                    if l_firstname_only:
                        pass
                        t_2.extend((
                            u'\n\t\t\t\t\t', 
                            to_string(environment.getattr(l_user, 'firstname')), 
                            u'\n\t\t\t\t', 
                        ))
                    else:
                        pass
                        t_2.extend((
                            u'\n\t\t\t\t\t', 
                            to_string(environment.getattr(l_user, 'firstname')), 
                            u' ', 
                            to_string(environment.getattr(l_user, 'lastname')), 
                            u'\n\t\t\t\t', 
                        ))
                    t_2.append(
                        u'\n\t\t\t', 
                    )
                t_2.append(
                    u'\n\t\t', 
                )
            t_2.append(
                u'\n\n\t', 
            )
            if context.call(environment.getattr(l_item, 'kind')) == 'SocialAction':
                pass
                t_2.append(
                    u'\n\t\t', 
                )
                if context.call(environment.getattr(l_item, 'class_name')) == 'Like':
                    pass
                    t_2.append(
                        u'liked', 
                    )
                t_2.append(
                    u'\n\t\t', 
                )
                if context.call(environment.getattr(l_item, 'class_name')) == 'Comment':
                    pass
                    t_2.append(
                        u'commented on', 
                    )
                t_2.append(
                    u'\n\t\t', 
                )
                if context.call(environment.getattr(l_item, 'class_name')) == 'Share':
                    pass
                    t_2.append(
                        u'shared', 
                    )
                t_2.append(
                    u'\n\t\t', 
                )
                if l_link_content:
                    pass
                    t_2.extend((
                        u'\n\t\t\t<a href="', 
                        to_string(context.call(l_link, 'content-item-view', repo=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(context.call(environment.getattr(l_item, 'parent')), 'repository'), 'key')), 'name')), key=context.call(environment.getattr(context.call(environment.getattr(l_item, 'parent')), 'key')))), 
                        u'">\n\t\t\t\t<span class=\'iconButtonBox formatButton_', 
                        to_string(environment.getattr(environment.getattr(context.call(environment.getattr(l_item, 'parent')), 'format'), 'name')), 
                        u"'>", 
                        to_string(environment.getattr(context.call(environment.getattr(l_item, 'parent')), 'title')), 
                        u'</span>\n\t\t\t</a>\n\t\t', 
                    ))
                else:
                    pass
                    t_2.extend((
                        u"\n\t\t\t<span class='iconButtonBox formatButton_", 
                        to_string(environment.getattr(environment.getattr(context.call(environment.getattr(l_item, 'parent')), 'format'), 'name')), 
                        u"'>", 
                        to_string(environment.getattr(context.call(environment.getattr(l_item, 'parent')), 'title')), 
                        u'</span>\n\t\t', 
                    ))
                t_2.append(
                    u'\n\t', 
                )
            t_2.append(
                u'\n\t\n\t', 
            )
            if context.call(environment.getattr(l_item, 'kind')) == 'ContentItem':
                pass
                t_2.append(
                    u'\n\t\t\tcreated ', 
                )
                if l_link_content:
                    pass
                    t_2.extend((
                        u'<a href="', 
                        to_string(context.call(l_link, 'content-item-view', repo=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_item, 'repository'), 'key')), 'name')), key=context.call(environment.getattr(l_item, 'key')))), 
                        u'"><span class=\'iconButtonBox formatButton_', 
                        to_string(environment.getattr(environment.getattr(l_item, 'format'), 'name')), 
                        u"'>", 
                        to_string(environment.getattr(l_item, 'title')), 
                        u'</span></a>', 
                    ))
                else:
                    pass
                    t_2.extend((
                        u"<span class='iconButtonBox formatButton_", 
                        to_string(environment.getattr(environment.getattr(l_item, 'format'), 'name')), 
                        u"'>", 
                        to_string(environment.getattr(l_item, 'title')), 
                    ))
                t_2.append(
                    u'\n\t', 
                )
            t_2.append(
                u'\n\t\n\t', 
            )
            if context.call(environment.getattr(l_item, 'kind')) == 'QueuedBlob':
                pass
                t_2.append(
                    u'\n\t\t\tuploaded ', 
                )
                if l_link_content:
                    pass
                    t_2.extend((
                        u'<a href="', 
                        to_string(context.call(l_link, 'content-create', inject=1, queued=context.call(environment.getattr(l_item, 'key')))), 
                        u'">', 
                    ))
                t_2.append(
                    to_string(t_1(environment.getattr(environment.getattr(l_item, 'blob'), 'filename'), 50)), 
                )
                if l_link_content:
                    pass
                    t_2.append(
                        u'</a>', 
                    )
                t_2.extend((
                    u'\n\t(', 
                    to_string(context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'byteconvert'), environment.getattr(environment.getattr(l_item, 'blob'), 'size'))), 
                    u')', 
                ))
            t_2.append(
                u"\n\t\t<span class='activityTimestamp'>", 
            )
            if l_timesince:
                pass
                t_2.append(
                    to_string(context.call(environment.getattr(environment.getattr(l_util, 'converters'), 'timesince'), environment.getattr(l_item, 'modifiedAt'))), 
                )
            else:
                pass
                t_2.append(
                    to_string(context.call(environment.getattr(environment.getattr(l_util, 'types'), 'str'), environment.getattr(l_item, 'modifiedAt'))), 
                )
            t_2.append(
                u'</span>\n\n\t</span>\n</div>', 
            )
            return concat(t_2)
        context.exported_vars.add('social_feed_entry')
        context.vars['social_feed_entry'] = l_social_feed_entry = Macro(environment, macro, 'social_feed_entry', ('user', 'item', 'you', 'firstname_only', 'link_name', 'link_content', 'timesince'), (False, False, False, True, True, ), False, False, False)

    blocks = {}
    debug_info = '1=9&4=17&5=19&8=24&11=29&16=34&20=39&24=47&26=69&27=74&28=78&30=87&33=102&34=106&36=113&41=127&42=132&43=140&44=148&45=156&46=160&47=162&50=171&54=182&55=187&58=212&59=217&60=234&61=240'
    return locals()