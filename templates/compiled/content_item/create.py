from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content_item/create.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/content_item/create.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/upload.html', 'source/content_item/create.html').module
        l_new_plupload = getattr(included_template, 'new_plupload', missing)
        if l_new_plupload is missing:
            l_new_plupload = environment.undefined("the template %r (imported on line 2 in 'source/content_item/create.html') does not export the requested name 'new_plupload'" % included_template.__name__, name='new_plupload')
        context.vars['new_plupload'] = l_new_plupload
        context.exported_vars.discard('new_plupload')
        included_template = environment.get_template('macros/editor.html', 'source/content_item/create.html').module
        l_new_markitup = getattr(included_template, 'new_markitup', missing)
        if l_new_markitup is missing:
            l_new_markitup = environment.undefined("the template %r (imported on line 3 in 'source/content_item/create.html') does not export the requested name 'new_markitup'" % included_template.__name__, name='new_markitup')
        context.vars['new_markitup'] = l_new_markitup
        context.exported_vars.discard('new_markitup')
        for event in parent_template.root_render_func(context):
            yield event

    def block_title(context, environment=environment):
        l_progress = context.resolve('progress')
        if 0: yield None
        if l_progress == '1':
            if 0: yield None
            yield u'Upload Files (Step 1)'
        if l_progress == '2':
            if 0: yield None
            yield u'Basic Details (Step 2)'
        if l_progress == '3':
            if 0: yield None
            yield u'Tagging & Related Content (Step 3)'
        yield u'- Add Content Wizard'

    def block_postsouth(context, environment=environment):
        l_categories_list = context.resolve('categories_list')
        l_progress = context.resolve('progress')
        if 0: yield None
        if l_progress == '2':
            if 0: yield None
        yield u"<script type='text/javascript'>\n\t\t"
        if (l_categories_list != '' and l_categories_list != False):
            if 0: yield None
            yield u'\n\t\t\tci_categories = %s;\n\t\t' % (
                l_categories_list, 
            )
        yield u'\n\t\t$(\'#repository-box #repository\').change(function setAutocomplete() {\n\t\t\t/*$(\'#category-box #category\').faceList(ci_categories[$(\'#repository-box #repository\').val()], {selectedItem: "value", searchObj: "value", selectionLimit:1, resultClick: function makeSelection(data){\n\t\t\t\t\n\t\t\t\t$(\'.facelist-selections\').hide();\n\t\t\t\t$(\'#category-box #category\').hide().val(data[\'attributes\'][\'name\']);\n\t\t\t\t$(\'#category-box\').append(\'<div class="category_selection">\'+data[\'attributes\'][\'value\']+\'</div>\');\n\t\t\t\t$(\'#.facelist-selections .facelist-original .as-input\').val(data[\'attributes\'][\'name\']);\n\t\t\t}});*/\n\t\t\t\n\t\t  if (typeof(ci_categories[$(\'#repository-box #repository\').val()]) == \'undefined\')\n\t\t  {\n\t\t\t\toptions = \'<option value="__NULL__" selected="selected">(No Category)</option>\';\n\t\t\t\t$("select#category").html(options);\n\t\t\t\t$(\'select#category\').attr(\'disabled\', \'disabled\');\n\t\t  }\n\t\t  else\n\t\t  {\n\t\t\t\t$(\'select#category\').attr(\'disabled\', \'\');\n\t\t\t  var options = \'\';\n\t\t\t\toptions += \'<option value="__NULL__">(No Category)</option>\';\t\t\n\t\t\t  for (var i=0; i<ci_categories[$(\'#repository-box #repository\').val()].length; i++)\n\t\t\t  {\n\t\t\t\tif(i==0)\n\t\t\t\t{\n\t\t\t\t\toptions += \'<option selected="selected" value="\' + ci_categories[$(\'#repository-box #repository\').val()][i].name + \'">\' + ci_categories[$(\'#repository-box #repository\').val()][i].value + \'</option>\';\n\t\t\t\t}\n\t\t        else\n\t\t\t\t{\n\t\t\t\t\toptions += \'<option value="\' + ci_categories[$(\'#repository-box #repository\').val()][i].name + \'">\' + ci_categories[$(\'#repository-box #repository\').val()][i].value + \'</option>\';\n\t\t\t\t}\n\t\t      }\n\t\t\t\t$("select#category").html(options);\n\t\t  }\n\t\n\t\t});\n\t</script>\n'

    def block_content(context, environment=environment):
        l_current_upload_index = context.resolve('current_upload_index')
        l_form = context.resolve('form')
        l_renderForm = context.resolve('renderForm')
        l_cancel_link = context.resolve('cancel_link')
        l_blob_obj = context.resolve('blob_obj')
        l_new_content_items = context.resolve('new_content_items')
        l_abs_link = context.resolve('abs_link')
        l_link = context.resolve('link')
        l_next_action_url = context.resolve('next_action_url')
        l_total_upload_count = context.resolve('total_upload_count')
        l_progress = context.resolve('progress')
        t_1 = environment.filters['truncate']
        if 0: yield None
        yield u"\n<div id='content_body_padding'>\n\t"
        if l_progress == '1':
            if 0: yield None
            yield u'\n\n\t\t<form id=\'file_upload_form\' action=\'#\'>\n\t\t\t<div id=\'spi_uploader\'>\n\t\t\t\t<p>Your browser doesn\'t support Flash, Silverlight, Gears, BrowserPlus or HTML5. Get a new browser.</p><!-- @TODO: Replace this is single-file-upload interface -->\n\t\t\t</div>\n\t\t\t<br class=\'clearboth\' />\n\t\t</form>\n\n\t\t<form method=\'post\' action=\'%s\' method=\'post\' id=\'create_content_step_1\' class=\'spi-form spi-upload-form\'>\n\t\n\t\t\t<div>\n\t\t\t</div>\n\t\n\t\t\t<input type=\'hidden\' name=\'action\' value=\'split_blobs\' />\n\t\n\t\t\t<a href="#" id=\'nextStepButton\' class=\'fancybutton mainbutton fancydisabled\' role=\'button\' disabled=\'true\' aria-disabled=\'true\'>\n\t\t\t\t<span class=\'iconButtonBox checkboxButtonBox\'></span>\n\t\t\t\t<p>Next Step</p>\n\t\t\t</a>\n\t\t</form>\n\n\t' % (
                l_next_action_url, 
            )
        yield u'\n\n\n\t'
        if l_progress == '2':
            if 0: yield None
            yield u'\n\t\t<div class=\'gridTitle\'>\n\t\t\t<span>File %s of %s (%s) - <a href="%s" target="_blank">Download</a> | <a href="http://docs.google.com/viewer?embedded=true&url=%s" target="_blank">Preview</a></span>\n\t\t</div>\n\t\t<div id=\'stepOneUploadForm\'>\n\t\t\t<form id=\'stepOneForm\' action="%s" method="%s" class="spi-form">\n\t\t\t\t%s\n\t\t\t\t<div class=\'clearboth\'></div>\n\t\t\t\t<div class=\'floatright\' id=\'controls\'>\n\n\t\t\t\t\t<a href="%s" id=\'discardButton\' class=\'fancybutton mainbutton\' role=\'button\'>\n\t\t\t\t\t\t<span class=\'iconButtonBox discardButtonBox\'></span>\n\t\t\t\t\t\t<p>Discard</p>\n\t\t\t\t\t</a>\n\n\t\t\t\t\t<a href="#" id=\'nextStepButton\' class=\'fancybutton mainbutton\' role=\'button\' onclick="javascript:$(\'#stepOneForm\').submit();">\n\t\t\t\t\t\t<span class=\'iconButtonBox checkboxButtonBox\'></span>\n\t\t\t\t\t\t<p>Create</p>\n\t\t\t\t\t</a>\n\n\t\t\t\t</div>\n\t\t\t\t<div class=\'clearboth\'></div>\n\t\t\t</form>\n\t\t</div>\n\t\t<div class=\'clearboth\'></div>\n\t' % (
                l_current_upload_index, 
                l_total_upload_count, 
                t_1(environment.getattr(l_blob_obj, 'filename'), 50, True), 
                context.call(l_link, 'media-serve-blob', blobkey=context.call(environment.getattr(l_blob_obj, 'key'))), 
                context.call(l_abs_link, 'media-serve-blob-filename', blobkey=context.call(environment.getattr(l_blob_obj, 'key')), filename=environment.getattr(l_blob_obj, 'filename')), 
                context.call(environment.getattr(l_form, 'get_action')), 
                context.call(environment.getattr(l_form, 'get_method')), 
                context.call(l_renderForm, l_form, omitSubmitButton=True, omitFormTag=True), 
                l_cancel_link, 
            )
        yield u'\n\n\t'
        if l_progress == '3':
            if 0: yield None
            yield u'\n\t\t<div class=\'gridTitle\'>\n\t\t\t<span>File %s of %s (%s) - <a href="%s" target="_blank">Preview</a></span>\n\t\t</div>\n\t\t<form action="%s" method="%s" id=\'tagsForm\' class=\'spi-form\'>\n\t\t\t%s\n\t\t\t\n\t\t\t\n\t\t\t<br /><br />\n\t\t\t\n\t\t\t<div id=\'tagsFooter\'>\n\t\t\t\t<div class=\'floatleft textleft base100\' style=\'margin-left: 10px; margin-top:-5px;\'><b>Tip:</b> Include the <b>client name</b> as a tag.<br />Tags are comma-separated and support spaces (i.e. "tag, tag two").</p></div>\n\t\t\t\t<div class=\'floatright base100\'>\n\t\t\t\t\t<a href="#" id=\'tagsSubmitButton\' class=\'fancybutton mainbutton\' role=\'button\' onclick="javascript:$(\'#tagsForm\').submit();">\n\t\t\t\t\t\t<span class=\'iconButtonBox checkboxButtonBox\'></span>\n\t\t\t\t\t\t<p>Save</p>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</form>\n\t' % (
                l_current_upload_index, 
                l_total_upload_count, 
                t_1(environment.getattr(l_blob_obj, 'filename'), 50, True), 
                context.call(l_link, 'media-serve-blob', blobkey=context.call(environment.getattr(l_blob_obj, 'key'))), 
                context.call(environment.getattr(l_form, 'get_action')), 
                context.call(environment.getattr(l_form, 'get_method')), 
                context.call(l_renderForm, l_form, omitSubmitButton=True, omitFormTag=True), 
            )
        yield u'\n\n\t'
        if l_progress == 'success':
            if 0: yield None
            yield u"\n\t\t<div class='gridTitle'>\n\t\t\t<h2>Success!</h2> <span>Uploaded %s file" % (
                l_total_upload_count, 
            )
            if l_total_upload_count != 1:
                if 0: yield None
                yield u's'
            yield u'.</span>\n\t\t</div>\n\t\t<br />\n\t\t<p>You created the following content items:\n\t\n\t\t\t<ul>\n\t\t\t\t'
            l_item = missing
            for l_item in l_new_content_items:
                if 0: yield None
                yield u'\n\t\t\t\t<li><b><a href="%s">%s</a></b> in repository %s:<br />\n\t\t\t\t\t %s</li>\n\t\t\t\t' % (
                    context.call(l_link, 'content-item-view', repo=context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_item, 'repository'), 'key')), 'name')), key=context.call(environment.getattr(l_item, 'key'))), 
                    environment.getattr(l_item, 'title'), 
                    environment.getattr(environment.getattr(l_item, 'repository'), 'name'), 
                    t_1(environment.getattr(l_item, 'description'), 200), 
                )
            l_item = missing
            yield u'\n\t\t\t</ul>\n\t\t\t<br /><a href="%s">Upload More Content</a>\n\t\t</p>\n\t' % (
                context.call(l_link, 'content-create'), 
            )
        yield u'\n</div>\n'

    def block_header(context, environment=environment):
        l_progress = context.resolve('progress')
        if 0: yield None
        if l_progress == '1':
            if 0: yield None
            yield u'<h1>Add Content Wizard</h1> <span>Step 1: File Upload</span>'
        if l_progress == '2':
            if 0: yield None
            yield u'<h1>Add Content Wizard</h1> <span>Step 2: Basic File Details</span>'
        if l_progress == '3':
            if 0: yield None
            yield u'<h1>Add Content Wizard</h1> <span>Step 3: Tagging &amp; Search</span>'
        if l_progress == 'success':
            if 0: yield None
            yield u'<h1>Add Content Wizard</h1>\n\t\t<span>Success<span>'

    def block_sidebar_header(context, environment=environment):
        if 0: yield None
        yield u'\n\tUploading Files\n'

    def block_sidebar_content(context, environment=environment):
        l_progress = context.resolve('progress')
        if 0: yield None
        yield u"\n<ul id='wizard_steps'>\n\t<li"
        if l_progress == '1':
            if 0: yield None
            yield u" class='current'"
        yield u'>'
        if l_progress == '1':
            if 0: yield None
            yield u"<span><b>Step 1: File Upload</b></span>\n\t\t\t<br /><p>Start by uploading a list of files you'd like to add. <a href='#'>Tips about Uploading</a></p>"
        else:
            if 0: yield None
            yield u'<span>Step 1: File Upload</span>'
        yield u'</li>\n\t\n\t<li'
        if l_progress == '2':
            if 0: yield None
            yield u" class='current'"
        yield u'>'
        if l_progress == '2':
            if 0: yield None
            yield u"<span><b>Step 2: Basic Information</b></span>\n\t\t\t<br /><p>Add basic information to each content item - name, description, category and type.<br /><a href='#'>Tips about Basic Info</a></p>"
        else:
            if 0: yield None
            yield u'<span>Step 2: Basic Information</span>'
        yield u'</li>\n\t\n\t<li'
        if l_progress == '3':
            if 0: yield None
            yield u" class='current'"
        yield u'>'
        if l_progress == '3':
            if 0: yield None
            yield u"<span><b>Step 3: Tagging &amp; Search</b></span>\n\t\t\t<br /><p>Add meta information like tags, keywords, and clients to make each item findable in search. <a href='#'>Tips about Searchability</a></p>"
        else:
            if 0: yield None
            yield u'<span>Step 3: Tagging &amp; Search</span>'
        yield u'</li>\n\t\n\t<li'
        if l_progress == 'success':
            if 0: yield None
            yield u" class='current'"
        yield u'>'
        if l_progress == 'success':
            if 0: yield None
            yield u'<span><b>Finish</b></span>\n\t\t\t<br /><p>Your newly uploaded content may take a few minutes to appear in search.</p>'
        else:
            if 0: yield None
            yield u'<span>Step 4: Finish</span>'
        yield u'</li>\t\n</ul>\n'

    def block_postnorth(context, environment=environment):
        l_progress = context.resolve('progress')
        l_new_plupload = context.resolve('new_plupload')
        if 0: yield None
        if l_progress == '1':
            if 0: yield None
            yield to_string(context.call(l_new_plupload, '#spi_uploader', '#create_content_step_1', '#file_upload_form'))
        yield u'<style>\n\t\t#category-box\n\t\t{\n\t\t\tmargin-left:10px;\n\t\t\twidth:275px;\n\t\t}\n\t\t#category-box #category\n\t\t{\n\t\t\twidth:275px;\n\t\t}\n\t\t.facelist-selections\n\t\t{\n\t\t\twidth:275px !important;\n\t\t}\n\t</style>\n\t\n'

    blocks = {'title': block_title, 'postsouth': block_postsouth, 'content': block_content, 'header': block_header, 'sidebar_header': block_sidebar_header, 'sidebar_content': block_sidebar_content, 'postnorth': block_postnorth}
    debug_info = '1=9&2=12&3=18&5=27&7=30&11=33&15=36&217=41&218=45&223=48&224=51&74=55&76=70&85=73&101=76&103=79&106=84&107=86&111=87&128=90&130=93&132=97&133=99&150=102&152=105&158=112&159=115&160=118&163=122&50=126&52=129&56=132&60=135&64=138&170=142&177=146&179=150&180=154&188=161&189=165&197=172&198=176&206=183&207=187&25=195&26=199&27=201'
    return locals()