from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/__meta.html'

    def root(context, environment=environment):
        l_page = context.resolve('page')
        l_title = context.resolve('title')
        if 0: yield None
        yield u'<!-- Meta -->\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\n<!-- About StonerHub -->\n<meta name="robots" content="/robots.txt"> <!-- for robots! -->\n<meta name="humans" content="/humans.txt"> <!-- for humans! -->\n\n<meta name="poweredby" content="apptools for appengine (apptools.github.com)">\n<meta name="author" content="sam gammon (momentum.io), neil michel (wire-stone.com)">\n\n<meta name="keywords" content ="stonerhub, wirestone, [wire] stone, universal content repository">\n<meta name="description" content="Quick and secure access to the best knowledge base in the industry">\n\n<!-- OpenGraph -->\n<meta property="og:title" content="'
        if environment.getattr(l_page, 'title'):
            if 0: yield None
            yield to_string(l_title)
        yield u'" />\n<meta property="og:type" content="web application" />\n<meta property="og:url" content="www.stonerhub.com" />\n<meta property="og:image" content="/assets/img/static/layout/wirestone/w-yellow.png" />\n<meta property="og:site_name" content="StonerHub" />\n\n\n<!-- Viewport -->\n<meta name="viewport" content="width=device-width,initial-scale=1">\n\n<!-- Google -->\n<meta name="google-site-verification" content="GNpWBXBMCFjW7thMuE06UvfgI4mktA9EcsevLda9VPU" />'

    blocks = {}
    debug_info = '15=11'
    return locals()