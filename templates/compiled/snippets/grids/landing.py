from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/grids/landing.js'

    def root(context, environment=environment):
        if 0: yield None
        yield u"\njsonData = null\n\nfunction spiPreProcess(data)\n{\n\tjsonData = data\n\n\trecords = []\n\tfor (index in data.response.records)\n\t{\n\t\trecords.push({'cell':[data.response.records[index].properties.title]});\n\t}\n\t\n\treturn {'total':records.length, 'page':1, 'rows':records};\n}"

    blocks = {}
    debug_info = ''
    return locals()