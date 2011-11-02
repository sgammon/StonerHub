from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/upload.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro(l_upload_selector, l_parent_form_selector, l_upload_form_selector, l_runtimes, l_max_file_size, l_chunk_size, l_unique_names, l_nextbutton):
            t_1 = []
            l_link = context.resolve('link')
            pass
            t_1.extend((
                u'\n\n<script type="text/javascript">\n\ntotal_uplaod_files = 0;\nvar uploadSessionKey = null;\n\nfunction setUploadRPCEndpoint(key)\n{\n\tuploadSessionKey = key;\n\t$(\'', 
                to_string(l_parent_form_selector), 
                u' div\').append(generateHiddenInputControl(\'upload_session_key\', uploadSessionKey));\n}\n\nfunction getUploadRPCEndpoint(uploader)\n{\n\tbase_rpc_url = "', 
                to_string(context.call(l_link, 'ajax-upload-generate-url')), 
                u'";\n\tif (uploadSessionKey == null)\n\t{\n\t\trpc_url = base_rpc_url+"?createNewUploadSession=true";\n \t\trpc_url += "&uploadCount="+uploader.total.queued.toString();\n\t}\n\telse\n\t{\n\t\trpc_url = base_rpc_url+"?uploadSession="+uploadSessionKey\n\t}\n\treturn rpc_url\n}\n\nfunction bindUploaderEvents(uploader)\n{\n\t\n\t  // Retrieve blobstore upload URL for\n\t  uploader.bind(\'UploadFile\', function(up, file)\n\t  {\n\t\t\n\t\tmime_type = getMIMEtype(file.name);\n\t\t\n\t\t$.ajax({\n\t\t\turl: getUploadRPCEndpoint(up),\n\t\t\tasync: false,\n\t\t\tsuccess: function(api_response)\n\t\t\t\t\t {\n\t\t\t\t\t\t// Quick sanity check...\n\t\t\t\t\t\tif (api_response.operation == \'generate_ajax_upload_url\')\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\tif (api_response.result == \'success\')\n\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\t// Set upload URL to returned Blobstore URL\n\t\t\t\t\t\t\t\tup.settings.url = api_response.response.upload_url;\n\t\t\t\t\t\t\t\tup.settings.multipart_params = {\'blob_content_type\': mime_type};\n\t\t\t\t\t\t\t\tsetUploadRPCEndpoint(api_response.response.upload_session_key);\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\telse\n\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\talert(\'Generate URL operation failed for file "\'+file.name+\'". Reason: \'+api_response.reason);\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t\telse\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\talert(\'There was an error generating an AJAX upload URL: Invalid response operation.\');\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t);\n\t});\n\n  uploader.bind(\'FileUploaded\', function(up, file, raw_api_response)\n  {\n\t\ttotal_upload_files--;\n\t\tapi_response = JSON.parse(raw_api_response.response);\n\t\t\n\t\t// Quick sanity check...\n\t\tif (api_response.operation == \'upload_callback\')\n\t\t{\n\t\t\t\n\t\t\tif (api_response.result == \'success\')\n\t\t\t{\n\t\t\t\t$(\'', 
                to_string(l_parent_form_selector), 
                u' div\').append(generateHiddenInputControl(\'blob_object\', JSON.stringify(api_response.response.blob), getMIMEtype(file.name)));\n\t\t\t}\n\t\t\telse\n\t\t\t{\n\t\t\t\talert(\'There was an error storing the file "\'+file.name+\'". Failure reason: "\'+api_response.response.failure_reason+\'".\');\n\t\t\t}\n\n\t\t\tif (total_upload_files == 0)\n\t\t\t{\n\t\t\t\t$("', 
                to_string(l_nextbutton), 
                u'").click(function advanceForm() {$(\'', 
                to_string(l_parent_form_selector), 
                u'\').submit();});\n\t\t\t\t$("', 
                to_string(l_nextbutton), 
                u'").removeAttr("disabled").removeAttr(\'aria-disabled\').removeClass(\'fancydisabled\').focus();\n\t\t\t}\n\n\t\t}\n\t\telse\n\t\t{\n\t\t\talert(\'operation is wrong... it is: \'+api_response.operation);\n\t\t}\n  });\n\n  uploader.bind(\'QueueChanged\', function(up, files) {\n\t\n\ttotal_upload_files = uploader.files.length;\n\t\n});\n \n}\n\n\tfunction createPluploadQueue()\n\t{\n\t\treturn $(\'', 
                to_string(l_upload_selector), 
                u"').plupload({\n\t\t\t\n\t\t\truntimes: '", 
                to_string(l_runtimes), 
                u'\',\n\t\t\tbrowse_button: \'spi_uploader_browse\',\n\t\t\tpreinit: bindUploaderEvents,\n\t\t\turl: \'#\',\n\t\t\tuse_query_string: false,\n\t\t\tmultipart: true,\n\t\t\t\n\t\t\tdrop_element: \'#content_body_content\',\n\t\t\tflash_swf_url: \'/assets/ext/static/plupload/runtime.flash-0.2.swf\',\n\t\t\tsilverlight_xap_url: \'/assets/ext/static/plupload/runtime.silverlight-0.2.xap\',\n\t\t\tfilters : [\n\t\t\t\n\t\t\t\t{title: "Image Files", extensions: "jpg,jpeg,gif,png,tiff,ico,svg"},\n\t\t\t\t{title: "Document Files", extensions: "doc,docx,dot,pdf,rtf,txt"},\n\t\t\t\t{title: "Spreadsheet Files", extensions: "xls,xlsx"},\n\t\t\t\t{title: "Presentation Files", extensions: "ppt,pptx"},\n\t\t\t\t{title: "Movie Files", extensions: "mpg,mov,avi,wmv"},\n\t\t\t\t{title: "Drawing Files", extensions: "ai,eps,ps,dxf,ttf"},\n\t\t\t\t{title: "Archive Files", extensions: "zip"}\n\t\t\t\n\t\t\t],\n\t\t\tdragdrop: true\n\t\t\t\n\t\t});\n\t}\n\n\n\n\t$(function() {\n\t\tup = createPluploadQueue();\n\t\tup.trigger(\'Refresh\');\n\t});\n\n</script>\n\n', 
            ))
            return concat(t_1)
        context.exported_vars.add('new_plupload')
        context.vars['new_plupload'] = l_new_plupload = Macro(environment, macro, 'new_plupload', ('upload_selector', 'parent_form_selector', 'upload_form_selector', 'runtimes', 'max_file_size', 'chunk_size', 'unique_names', 'nextbutton'), ('html5,gears,flash,silverlight,html4,browserplus', '2gb', '1mb', True, '#nextStepButton', ), False, False, False)

    blocks = {}
    debug_info = '1=8&11=14&16=16&78=18&87=20&88=24&108=26&110=28'
    return locals()