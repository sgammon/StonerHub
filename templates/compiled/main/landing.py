from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/main/landing.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main-twocolumn.html', 'source/main/landing.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/datagrid.html', 'source/main/landing.html').module
        l_new_datagrid = getattr(included_template, 'new_datagrid', missing)
        if l_new_datagrid is missing:
            l_new_datagrid = environment.undefined("the template %r (imported on line 2 in 'source/main/landing.html') does not export the requested name 'new_datagrid'" % included_template.__name__, name='new_datagrid')
        context.vars['new_datagrid'] = l_new_datagrid
        context.exported_vars.discard('new_datagrid')
        for event in parent_template.root_render_func(context):
            yield event

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'Dashboard'

    def block_content_body_header(context, environment=environment):
        if 0: yield None

    def block_postsouth(context, environment=environment):
        l_link = context.resolve('link')
        l_new_datagrid = context.resolve('new_datagrid')
        l_grid = context.resolve('grid')
        if 0: yield None
        yield u'\n\n%s\n\n<script type=\'text/javascript\'>\t\n$(document).ready( function loadInlineUploader()\n{\n\tbodyelement = document.body;\n\tdropelement = document.getElementById(\'inlineupload\');\n\n\tfunction dragEnter(evt)\n\t{\n\t\tevt.stopPropagation();\n\t\tevt.preventDefault();\n\t\t$(\'#inlineupload\').addClass(\'uploadDragDrop\');\n\t\t$(\'#uploadProgress\').hide();\n\t\t$(\'#dragDropHint\').removeClass(\'hidden\');\n\t}\n\t\n\tfunction dragExit(evt)\n\t{\n\t\tevt.stopPropagation();\n\t\tevt.preventDefault();\n\t\t$(\'#inlineupload\').removeClass(\'uploadDragDrop\');\n\t\t$(\'#dragDropHint\').addClass(\'hidden\');\n\t\t$(\'#uploadProgress\').show();\n\t}\n\t\n\tfunction dropItem(evt)\n\t{\n\t\tdragExit(evt);\n\t}\n\t\n\tfunction dragOver(item)\n\t{\n\t\tevt.stopPropagation();\n\t\tevt.preventDefault();\t\t\n\t}\n\n\tbodyelement.addEventListener(\'dragenter\', dragEnter, false);\n\tbodyelement.addEventListener(\'dragexit\', dragExit, false);\n\tdropelement.addEventListener(\'drop\', dropItem, false);\t\n\tdropelement.addEventListener(\'dragOver\', dragOver, false);\n\t\n\tfunction getUploadRPCEndpoint(uploader)\n\t{\n\t\tbase_rpc_url = "%s";\n\t\trpc_url = base_rpc_url+"?createNewUploadSession=false";\n\t\trpc_url += "&uploadCount="+uploader.total.queued.toString();\n\t\treturn rpc_url\n\t}\n\tvar uploader = new plupload.Uploader({\n\t\n\t\truntimes: \'html5,gears,flash,silverlight,browserplus,html4\',\n\t\tbrowse_button: \'inlineUploadTrigger\',\n\t\tdrop_element: \'inlineupload\',\n\t\tcontainer: \'inlineupload\',\n\t\turl: \'#\',\n\t\tuse_query_string: false,\n\t\tmultipart: true,\n\t\tflash_swf_url: \'/assets/ext/static/plupload/runtime.flash-0.1.swf\',\n\t\tsilverlight_xap_url: \'/assets/ext/static/plupload/runtime.silverlight-0.1.xap\',\n\t\tfilters : [\n\t\t\t{title: "Image Files", extensions: "jpg,jpeg,gif,png,tiff,ico,svg"},\n\t\t\t{title: "Document Files", extensions: "doc,docx,dot,pdf,rtf,txt"},\n\t\t\t{title: "Spreadsheet Files", extensions: "xls,xlsx"},\n\t\t\t{title: "Presentation Files", extensions: "ppt,pptx"},\n\t\t\t{title: "Movie Files", extensions: "mpg,mov,avi,wmv"},\n\t\t\t{title: "Drawing Files", extensions: "ai,eps,ps,dxf,ttf"},\n\t\t\t{title: "Archive Files", extensions: "zip"}\n\t\t],\n\t});\n\t\n\tfunction startUploader()\n\t{\n\t\tuploader.start();\n\t}\n\n\t$(\'#startUploadTrigger\').click(startUploader);\n\n\tuploader.init();\n\n\tuploader.bind(\'FilesAdded\', function(up, files){\n\t\tif (files.length > 1)\n\t\t{\n\t\t\t$(\'#uploadProgress\').html(files.length.toString()+\' files ready to upload\').removeClass(\'hidden\');\n\t\t}\n\t\telse\n\t\t{\n\t\t\t$(\'#uploadProgress\').html(\'1 file ready to upload\').removeClass(\'hidden\');\n\t\t}\n\t\tup.refresh();\n\t\t\n\t\t$(\'#uploadTriggerText\').html(\'Add files\');\n\t\t$(\'#startUploadTrigger\').removeClass(\'hidden\');\n\n\t});\n\n\t// Retrieve blobstore upload URL for \n\tuploader.bind(\'UploadFile\', function(up, file)\n\t{\n\n\tmime_type = getMIMEtype(file.name);\n\n\t$.ajax({\n\t\turl: getUploadRPCEndpoint(up),\n\t\tasync: false,\n\t\tsuccess: function(api_response)\n\t\t\t {\n\t\t\t\t// Quick sanity check...\n\t\t\t\tif (api_response.operation == \'generate_ajax_upload_url\')\n\t\t\t\t{\n\t\t\t\t\tif (api_response.result == \'success\')\n\t\t\t\t\t{\n\t\t\t\t\t\t// Set upload URL to returned Blobstore URL\n\t\t\t\t\t\tup.settings.url = api_response.response.upload_url;\n\t\t\t\t\t\tup.settings.multipart_params = {\'blob_content_type\': mime_type};\n\t\t\t\t\t}\n\t\t\t\t\telse\n\t\t\t\t\t{\n\t\t\t\t\t\talert(\'Generate URL operation failed for file "\'+file.name+\'". Reason: \'+api_response.reason);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\telse\n\t\t\t\t{\n\t\t\t\t\talert(\'There was an error generating an AJAX upload URL: Invalid response operation.\');\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t);\n\t});\n\t\n\tuploader.bind(\'UploadProgress\', function(up, file) {\n\t\n\t\t$("#uploadProgress").html(file.percent + "%%");\n\t\tif(file.percent.toString() == \'100\')\n\t\t{\n\t\t\t$("#uploadProgress").html(\'finished!\');\n\t\t}\n\t\n\t});\n\t\n\t uploader.bind(\'FileUploaded\', function(up, file, raw_api_response)\n\t {\n\t\tapi_response = JSON.parse(raw_api_response.response);\n\t\trawRpcResponse = raw_api_response;\n\t\trpcResponse = api_response;\n\n\t\t// Quick sanity check...\n\t\tif (api_response.operation == \'upload_callback\')\n\t\t{\n\n\t\t\tif (api_response.result == \'success\')\n\t\t\t{\n\t\t\t\t$(\'#inlineUploadForm div\').append(generateHiddenInputControl(\'blob_object\', api_response.response.blob.key, getMIMEtype(file.name)));\n\t\t\t}\n\t\t\telse\n\t\t\t{\n\t\t\t\talert(\'There was an error storing the file "\'+file.name+\'". Failure reason: "\'+api_response.response.failure_reason+\'".\');\n\t\t\t}\n\n\t\t}\n\t\telse\n\t\t{\n\t\t\talert(\'operation is wrong... it is: \'+api_response.operation);\n\t\t}\n\t }\n\t)});\n</script>\n' % (
            context.call(l_new_datagrid, '#results', l_grid), 
            context.call(l_link, 'ajax-upload-generate-url'), 
        )

    def block_landing_page_search_box(context, environment=environment):
        if 0: yield None
        yield u'\n<div id="home-search" class="m-rbl">\n\t<form action="/search" method=\'get\' id=\'inlinesearch\'>\n\t\t<input type=\'hidden\' name=\'s\' value=\'quicksearch\' />\n\t\t<input name=\'a\' type=\'hidden\' value=\'sR\' />\n\t\t<input type=\'search\' name=\'query\' placeholder=\'search\' x-webkit-speech id=\'quicksearch\' />\n\t\t\n\t\t<a href="#" class=\'fancybutton mainbutton\' role=\'button\'>\n\t\t\t<span class=\'iconButtonBox searchButtonBox\'></span>\n\t\t</a>\n\t\t\n\t</form>\n\t\n\t<div id=\'inlineupload\'>\n\t\t<a href="#" id=\'inlineUploadTrigger\' class=\'fancybutton mainbutton\' role=\'button\'>\n\t\t\t<span class=\'iconButtonBox uploadButtonBox\'></span>\n\t\t\t<p id=\'uploadTriggerText\'>Upload</p>\n\t\t</a>\n\n\t\t<a href="#" id=\'startUploadTrigger\' class=\'fancybutton mainbutton hidden\' role=\'button\'>\n\t\t\t<span class=\'iconButtonBox checkboxButtonBox\'></span>\n\t\t\t<p>Start</p>\n\t\t</a>\n\t\t\n\t\t<span id=\'dragDropHint\' class=\'hidden\'>(Drag files here)</span>\n\t\t<span id=\'uploadProgress\' class=\'hidden\'>starting upload...</span>\n\t</div>\n\t\t\n</div>\n'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u"\n\n<div>\n\n\t<div id='gridTitle'><h2>Recent Uploads</h2></div>\n\n\t<div id='results'>\n\t\tWaiting for results...\n\t</div>\t\n</div>\n\n"

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n<h1><b>StonerHub - Dashboard</b></h1>\n\n'

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
    debug_info = '1=9&2=12&4=21&11=25&65=28&67=34&111=35&13=38&44=42&6=46&57=50&59=54&62=58'
    return locals()