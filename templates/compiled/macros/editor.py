from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/editor.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro(l_selector):
            t_1 = []
            pass
            t_1.extend((
                u'<script language="javascript">\n$(document).ready(function()\t{\n    $(\'', 
                to_string(l_selector), 
                u"').markItUp(markdownEditorConfig);\n});\n</script>", 
            ))
            return concat(t_1)
        context.exported_vars.add('new_markitup')
        context.vars['new_markitup'] = l_new_markitup = Macro(environment, macro, 'new_markitup', ('selector',), (), False, False, False)

    blocks = {}
    debug_info = '1=8&5=13'
    return locals()