from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/main/newsfeed.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/main/newsfeed.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Newsfeed'

    def block_content_body_header(context, environment=environment):
        if 0: yield None

    def block_postsouth(context, environment=environment):
        l_util = context.resolve('util')
        if 0: yield None
        yield u'\n<script type=\'text/javascript\'>\n\tretrieveNewsfeed("%s");\n</script>\n' % (
            context.call(environment.getattr(context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'api'), 'users'), 'get_current_user')), 'key')), 'name')), 
        )

    def block_landing_page_search_box(context, environment=environment):
        if 0: yield None
        yield u'\n<div id="home-search" class="m-rbl">\n\t<form action="/search" method=\'get\' id=\'inlinesearch\'>\n\t\t<input type=\'hidden\' name=\'s\' value=\'quicksearch\' />\n\t\t<input name=\'a\' type=\'hidden\' value=\'sR\' />\n\t\t<input type=\'search\' name=\'query\' placeholder=\'search\' x-webkit-speech id=\'quicksearch\' />\n\t\t\n\t\t<a href="#" class=\'fancybutton mainbutton\' role=\'button\'>\n\t\t\t<span class=\'iconButtonBox searchButtonBox\'></span>\n\t\t</a>\n\t\t\n\t</form>\n</div>\n'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'\n\n<div id=\'newsfeed\'>\n\n\t<div id=\'newsfeed_controls\'>\n\t\t<form id=\'controlsForm\'>\n\n\t\t<a id=\'refreshLink\' href="#" onclick="refreshNewsfeed();">Refresh</a>\n\t\t<ul>\n\n\t\t\t<li class=\'newsfeed_control\'><input type=\'checkbox\' checked=\'checked\' id=\'showAll\' /> <span class=\'newsfeedFilter\'>Show All</span></li>\n\t\t\t\n\t\t\t<li class=\'newsfeed_control_header\'>Types:</li>\n\t\t\t<li class=\'newsfeed_control\'><input type=\'checkbox\' id=\'showSocial\' /> <span class=\'newsfeedFilter\'>Social</span></li>\n\t\t\t<li class=\'newsfeed_control\'><input type=\'checkbox\' id=\'showContent\' /> <span class=\'newsfeedFilter\'>Content</span></li>\t\t\t\n\t\t\t\n\t\t\t<li class=\'newsfeed_control_header\'>Views:</li>\n\t\t\t<li class=\'newsfeed_control\'><input type=\'checkbox\' id=\'showPublic\' /> <span class=\'newsfeedFilter\'>Public</span></li>\n\t\t\t<li class=\'newsfeed_control\'><input type=\'checkbox\' id=\'showSubscribed\' /> <span class=\'newsfeedFilter\'>Subscribed</span></li>\n\t\t</ul>\n\t\t</form>\n\t</div>\n\n\t<div id=\'newsfeed_entries\' class=\'hidden\'>\n\n\t</div>\n\t\n\t<div class=\'newsfeed_loading_wrapper\'>\n\t\t<div class=\'newsfeed_loading\'>Loading...</div>\n\t</div>\n\t\n</div>\n\n'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n<h1><b>Stonerhub - Newsfeed</b></h1>\n\n'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u"<span class='iconButtonBox infoButtonBox'>Guide for Beta Users</span>"

    def block_sidebar_content(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\tNow that your user account is active and registered, you are free to roam about the cabin.<br />\n\t\n\tIf you encounter a problem, please <a href="%s">file a bug report</a>.\n' % (
            context.call(l_link, 'file-bug'), 
        )

    blocks = {'title': block_title, 'content_body_header': block_content_body_header, 'postsouth': block_postsouth, 'landing_page_search_box': block_landing_page_search_box, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&3=15&10=19&70=22&72=26&12=29&27=33&5=37&62=41&64=45&67=49'
    return locals()