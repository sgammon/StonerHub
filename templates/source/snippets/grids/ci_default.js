/* ==== Anchor Generators ==== */
function createRepositoryAnchor(dataObject) { return '/repositories/'+dataObject.repository.key.name+'/content'; }
function createCategoryAnchor(dataObject) { return createRepositoryAnchor(dataObject)+'/category/'+dataObject.category.key.name; }
function createContentItemAnchor(dataObject, key) { return createRepositoryAnchor(dataObject)+'/'+key; }

/* ==== Render Functions ==== */
function renderTitleColumn(render_obj)
{
	ci_key = render_obj.aData[0];
	content_item = rpcTracker.dataObjects[ci_key];
	cell = '<div class="gridCell ci_result"><a class="ciTitleAnchor iconButtonBox formatButton_'+content_item.format.properties.name+'" href="'+createContentItemAnchor(content_item, ci_key)+'">'+render_obj.aData[1]+'</a>';
	cell += '<br /><span class="parentLinks"><a href="'+createRepositoryAnchor(content_item)+'">'+content_item.repository.properties.name+'</a>';
	if (content_item.category != null)
	{
		cell += '&gt;<a href="'+createCategoryAnchor(content_item)+'">'+content_item.category.properties.name+'</span>';
	}
	return cell
}
function renderDescriptionColumn(render_obj)
{
	return '<p class="ciDescription">'+truncate(rpcTracker.dataObjects[render_obj.aData[0]].description, 80)+'</p>';
}
function getTagLink(tag)
{
	return '<a class="tag_'+tag.kind+'" href="/tags/'+tag.name+'">'+tag.name+'</a>';
}
function renderTagsColumn(render_obj)
{
	var output = [];
	rpcTracker.dataObjects[render_obj.aData[0]].tags.forEach(function(item) {
		output.push(getTagLink(item))
	});
	return output.join(', ')
}
function renderCategoryColumn(render_obj)
{
	if(typeof(rpcTracker.dataObjects[render_obj.aData[0]].category) !== 'undefined' && rpcTracker.dataObjects[render_obj.aData[0]].category !== null)
	{
		return rpcTracker.dataObjects[render_obj.aData[0]].category.properties.name;
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