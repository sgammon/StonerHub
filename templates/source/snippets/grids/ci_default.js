function truncate(p, len) {
  if (p.length > len) {
    p = p.substring(0, len);
    p = p.replace(/\w+$/, '');
    p += '...';
    return p;
  }
  else
  {	return p;
}
}


/* ==== Anchor Generators ==== */
function createRepositoryAnchor(dataObject) { return '/repositories/'+dataObject.repository.key.name+'/content'; }
function createCategoryAnchor(dataObject) { return createRepositoryAnchor(dataObject)+'/category/'+dataObject.category.key.name; }
function createContentItemAnchor(dataObject, key) { return createRepositoryAnchor(dataObject)+'/'+key; }

/* ==== Render Functions ==== */
function renderTitleColumn(render_obj)
{	
	ci_key = render_obj.aData[0];
	content_item = $.stonerhub.models.ContentItem.get(ci_key);
	
	content_item.format = {};
	content_item.format.name = 'PDF'; // @TODO: Switch this to live	
	
	cell = '<div class="gridCell ci_result"><a class="ciTitleAnchor iconButtonBox formatButton_'+content_item.format.name+'" href="'+createContentItemAnchor(content_item, ci_key)+'">'+truncate(render_obj.aData[1], 30)+'</a>';
	cell += '<br /><span class="parentLinks"><a href="'+createRepositoryAnchor(content_item)+'">'+content_item.repository.name+'</a>';
	if (content_item.category != null && typeof(content_item.category) == 'undefined')
	{
		cell += '&gt;<a href="'+createCategoryAnchor(content_item)+'">'+content_item.category.name+'</span>';
	}
	return cell
}
function renderDescriptionColumn(render_obj)
{
	return '<p class="ciDescription">'+truncate($.stonerhub.models.ContentItem.get(render_obj.aData[0]).description, 80)+'</p>';
}
function getTagLink(tag)
{
	return '<a class="tag_'+tag.key.kind+'" href="/tags/'+tag.name+'">'+tag.name+'</a>';
}
function renderTagsColumn(render_obj)
{
	var output = [];
	ci = $.stonerhub.models.ContentItem.get(render_obj.aData[0]);
	if(typeof(ci.tags) != 'undefined')
	{
		ci.tags.forEach(function(item) {
			output.push(getTagLink(item))
		});
		return output.join(', ')		
	}
	else
	{
		return 'None'
	}
}
function renderCategoryColumn(render_obj)
{
	ci = $.stonerhub.models.ContentItem.get(render_obj.aData[0]);
	if(typeof(ci.category) !== 'undefined' && ci.category !== null)
	{
		return ci.category.name;
	}
	else
	{
		return 'None';
	}
}

ciColumns = [{'sName':'key', 'bVisible':false, 'bSortable':false},
			 {'sName':'title','sWidth':'35%','sTitle':'Title','fnRender':renderTitleColumn, 'bSortable':false},
			 {'sName':'description','sWidth':'35%','sTitle':'Description', 'fnRender':renderDescriptionColumn, 'bSortable':false},
			 {'sName':'tags','sTitle':'Tags', 'sWidth':'30%', 'fnRender':renderTagsColumn, 'bSortable':false}];