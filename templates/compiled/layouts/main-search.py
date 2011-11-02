from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main-search.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', 'source/layouts/main-search.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/layouts/main-search.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/layouts/main-search.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        l_query = context.resolve('query')
        if 0: yield None
        yield u'\n\n<div class="col full">\n\n\t<div class="m-trbl">\n\t\t\n\t\t<div id="content_header" class="header folded">\n\n\t\t\t\n\t\t\t<h1>Search</h1>\n\t\t\t\n\t\t</div>\n\t\t\n\t</div>\n</div>\n\n\t\n<div class="col threequarters clear">\n\n\t<div id="home-search" class="m-rbl">\n\t\t\t\n\n\t\t<div id=\'search-form-wrapper\'>\n\t\t\t<form action="/search" method=\'get\' id=\'search-form\'>\n\t\t\t\t<div id=\'searchleft\'>\n\t\t\t\t\t<input name=\'a\' type=\'hidden\' value=\'sR\' />\n\t\t\t\t\t<input name=\'s\' type=\'hidden\' value=\'main\' />\n\t\t\t\t\t<input name=\'query\' type=\'search\' placeholder=\'e.g. "e-commerce"\'  id=\'search-unibox\' class=\'noquery\' '
        if l_query:
            if 0: yield None
            yield u"value='%s'" % (
                l_query, 
            )
        yield u' x-webkit-speech />\n\t\t\t\t\t<button onclick=\'javscript:doSearch();\' id=\'search-submit\'>Search</button>\n\t\t\t\t</div>\n\t\n\t\t\t\t<div id=\'searchright\' style="display:none">\n\t\t\t\t\t<a href=\'javascript:toggleShowSearchOptions();\' id=\'toggleSearchOptionsPane\'>Show more search options</a>\n\t\t\t\t</div>\n\t\n\t\t\t\t<div class=\'clearboth\'></div>\n\t\n\t\t\t\t<div id=\'search-options-pane\'>\n\t\t\t\t\t<div class=\'box\'>\n\t\t\t\t\t\tOther filters will go in this area.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</form>\t\n\t\n\t\t</div>\n\t\n\t</div>\n\n\n\n\n\n\t\n\t<div id=\'content_body\' class="m-rbl">\n\t\t\n\t\t<div id=\'content_body_content\' class="content">\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\t\t<div id=\'results_pane\' class=" clear">\n\n\t\t\t\t\t\t<div id=\'content_body_search\'>\n\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t'
        for event in context.blocks['content_body_header'][0](context):
            yield event
        yield u'\n\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div id=\'content_body_content\' class="content">\n\t\t\t\t\t\t\t\t'
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\n\n\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\n\n\n\n\n\n<div id=\'sidebar\' class="col quarter">\n\t\n\t<div class="m-rb">\n\t\t\n\t\t\n\t\t\n\t\t\t\t<div id=\'sidebar_pane\'>\n\t\t\t\t\t\n\t\t\t\t\t<div id=\'sidebar_pane_header\'>Filters</div>\n\t\t\t\t\n\t\t\t\t\t<div id=\'sidebar_pane_content\' class=\'folded\'>\n\t\t\t\t\t\n\t\t\t\t\t\t<div class=\'meta_pane\' id=\'repository_filters\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_header\'>\n\t\t\t\t\t\t\t\t<p>Repository <span>+</span></p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_content\'>\n\t\t\t\t\t\t\t\t<p>Repository filters here!</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t\t<div class=\'meta_pane\' id=\'category_filters\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_header\'>\n\t\t\t\t\t\t\t\t<p>Category <span>+</span></p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_content\'>\n\t\t\t\t\t\t\t\t<p>Category filters here!</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t\t<div class=\'meta_pane\' id=\'tag_filters\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_header\'>\n\t\t\t\t\t\t\t\t<p>Tag <span>+</span></p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_content\'>\n\t\t\t\t\t\t\t\t<p>Tag filters here!</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t</div>\t\n\t\t\t\t\t\n\t\t\t\t\t\t<div class=\'meta_pane\' id=\'type_filters\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_header\'>\n\t\t\t\t\t\t\t\t<p>File Type <span>+</span></p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_content\'>\n\t\t\t\t\t\t\t\t<p>Sidebar Content</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t</div>\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t<div class=\'meta_pane\' id=\'user_filters\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_header\'>\n\t\t\t\t\t\t\t\t<p>User <span>+</span></p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_content\'>\n\t\t\t\t\t\t\t\t<p>Sidebar Content</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t</div>\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t<div class=\'meta_pane\' id=\'datetime_filters\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_header\'>\n\t\t\t\t\t\t\t\t<p>Date &amp; Time <span>+</span></p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t\t<div class=\'meta_pane_content\'>\n\t\t\t\t\t\t\t\t<p>Sidebar Content</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\t</div>\t\t\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t</div>\n\n\n\n\n\t\t\n\t</div>\n\t\n</div>\n'

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t\t\t\t\t<h2 class="grid-title">Content Header</h2>\n\t\t\t\t\t\t\t'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'<p>Content</p>'

    blocks = {'body': block_body, 'content_body_header': block_content_body_header, 'content': block_content}
    debug_info = '1=9&2=12&4=21&31=25&70=31&76=34&70=38&76=42'
    return locals()