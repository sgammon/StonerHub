from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/security/signup-step3.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/security/signup-step3.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/security/signup-step3.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/security/signup-step3.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_content_body_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h2>Select an area of the original image to choose your profile picture.</h2>\n'

    def block_postsouth(context, environment=environment):
        l_img_height = context.resolve('img_height')
        l_img_width = context.resolve('img_width')
        if 0: yield None
        yield u"\n\t<script type='text/javascript'>\n\t\tfunction updateCoords(coords)\n\t\t{\n\t\t\tvar rx = 100 / coords.w;\n\t\t\tvar ry = 100 / coords.h;\n\n\t\t\t$('#cropPreview').css({\n\t\t\t\twidth: Math.round(rx * %s) + 'px',\n\t\t\t\theight: Math.round(ry * %s) + 'px',\n\t\t\t\tmarginLeft: '-' + Math.round(rx * coords.x) + 'px',\n\t\t\t\tmarginTop: '-' + Math.round(ry * coords.y) + 'px'\n\t\t\t});\n\t\t\t\n\t\t\t$('#crop-x1').val(coords.x);\n\t\t\t$('#crop-y1').val(coords.y);\n\t\t\t$('#crop-x2').val(coords.x2);\n\t\t\t$('#crop-y2').val(coords.y2);\n\t\t\t$('#crop-w').val(coords.w);\n\t\t\t$('#crop-h').val(coords.h);\t\t\t\n\t\t};\n\t\t$(document).ready(function() {\n\t\t\n\t\t\t$('#cropOriginal').Jcrop({\n\t\t\t\t\n\t\t\t\tonChange:updateCoords,\n\t\t\t\tonSelect:updateCoords,\n\t\t\t\taspectRatio:1,\n\t\t\t\tallowMove:true\n\t\t\t\t\n\t\t\t});\n\t\t\n\t\t});\n\t</script>\n" % (
            l_img_width, 
            l_img_height, 
        )

    def block_content(context, environment=environment):
        l_action_url = context.resolve('action_url')
        l_asset_url = context.resolve('asset_url')
        l_img_height = context.resolve('img_height')
        l_img_width = context.resolve('img_width')
        l_asset_key = context.resolve('asset_key')
        if 0: yield None
        yield u'\n\t<form action="%s" method=\'post\'>\n\t\t<div id=\'cropAction\'>\n\n\t\t\t<div class=\'floatleft\' id=\'cropOriginalBox\'>\n\t\t\t\t<h2>Original:</h2>\n\t\t\t\t<div>\n\t\t\t\t\t<img src=\'%s\' alt=\'Original\' id=\'cropOriginal\' />\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class=\'floatleft\' id=\'cropPreviewBox\'>\n\t\t\t\t<h2>Crop Preview:</h2>\n\t\t\t\t<div id=\'cropPreview100\'>\n\t\t\t\t\t<img src=\'%s\' alt=\'Preview\' id=\'cropPreview\' />\n\t\t\t\t</div>\n\t\t\t\t<br />\n\t\t\t\t<input type=\'submit\' value=\'Use Picture\' />\n\t\t\t</div>\n\t\t\t<div class=\'clearboth\'></div>\n\t\t</div>\n\t\t<div class=\'clearboth\'></div>\n\t\t\n\t\t<input type=\'hidden\' name=\'x1\' id=\'crop-x1\' value=\'0\' />\n\t\t<input type=\'hidden\' name=\'y1\' id=\'crop-y1\' value=\'0\' />\n\t\t<input type=\'hidden\' name=\'x2\' id=\'crop-x2\' value=\'100\' />\n\t\t<input type=\'hidden\' name=\'y2\' id=\'crop-y2\' value=\'100\' />\n\t\t<input type=\'hidden\' name=\'h\' id=\'crop-h\' value="%s" />\n\t\t<input type=\'hidden\' name=\'w\' id=\'crop-w\' value="%s" />\n\t\t<input type=\'hidden\' name=\'asset\' value=\'%s\' />\t\t\n\t\t\n\t</form>\n' % (
            l_action_url, 
            l_asset_url, 
            l_asset_url, 
            l_img_height, 
            l_img_width, 
            l_asset_key, 
        )

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t<h1>Create an Account</h1> <span>Account setup complete!</span>\n'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'Creating an Account'

    def block_sidebar_content(context, environment=environment):
        if 0: yield None
        yield u"\n<ul id='wizard_steps'>\n\t<li>\n\t\t\t<span><b>1. Account Information</b></span>\n\t\t\t<br /><p>Tell us a bit about who you are.</p>\n\t</li>\n\t<li>\n\t\t\t<span><b>2. Profile Picture</b></span>\n\t\t\t<br /><p>Upload a picture for all to see.</p>\n\t</li>\n\t<li class='current'>\n\t\t\t<span><b>3. Crop Profile Picture</b></span>\n\t\t\t<br /><p>Crop your profile picture to your liking.</p>\n\t</li>\n</ul>\n\n"

    blocks = {'content_body_header': block_content_body_header, 'postsouth': block_postsouth, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content}
    debug_info = '1=9&2=12&73=21&79=25&87=30&88=31&13=34&14=42&20=43&27=44&40=45&41=46&42=47&6=50&49=54&53=58'
    return locals()