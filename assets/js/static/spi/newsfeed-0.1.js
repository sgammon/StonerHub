

function renderNewsfeedItem(key, type, kind, user, timesince, contentitem, timestamp)
{
	console.log('NEWFEED', key, type, kind, user, timesince, contentitem, timestamp);

	contexttext = null;

	// Calculate action text
	switch (kind)
	{
		case 'comment':
			actiontext = 'commented on';
			icon = 'commentTextButtonBox';
			contexttext = '<span class="newsfeed_comment"><span class="newsfeed_quote">"</span>'+contentitem.comment_text+'<span class="newsfeed_quote">"</span></span>';
			break;

		case 'like':
			actiontext = 'liked';
			icon = 'likeButtonBox';
			contexttext = null;
			break;
			
		case 'share':
			actiontext = 'shared';
			icon = 'shareButtonBox';
			contexttext = 'with '+'<a href="'+contentitem.target_user.profile_url+'">'+contentitem.target_user.fullname+'</a>';
			break;
			
		case 'created':
			actiontext = 'uploaded';
			icon = 'uploadedContentButtonBox';
			contexttext = null;
			break;
			
		case 'modified':
			actiontext = 'edited';
			icon = 'editedContentButtonBox';
			contexttext = null;
			break;
	}


	// Open divs
	template = '<div id="'+key+'" class="newsfeed_item '+type+'">';

	// Add left-side icon bar
	template += '<div class="newsitem_icons">';
	template += '<span class="newsitem_icon iconButtonBox '+icon+'"></span>';
	template += '</div>'; // Close newsitem_icons

	// Open newsfeed_entry
	template += '<div class="newsfeed_entry">';
	
	// Add Avatar
	template += '<div class="newsitem_avatar">'
	template += '<a href="'+user.profile_url+'">';
	template += '<img src="'+user.avatar_url+'" alt="'+user.fullname+'" width="48" height ="48" class="newsfeed_item_avatar" />';
	template += '</a></div>'; // Close newsitem_avatar

	// Add Content
	template += '<div class="newsitem_content">';
	template += '<span class="newsitem_name"><a href="'+user.profile_url+'">'+user.fullname+'</a></span> <span class="newsitem_action">'+actiontext+'</span>';

	// Add content item title
	template += ' <a href="'+contentitem.view_url+'" title="'+contentitem.title+'">'+contentitem.title+'</a><br />';
	
	// Add content text
	if (contexttext != null)
	{
		template += '<span class="newsitem_context">'+contexttext+'</span> - ';
	}
	template += '<span class="newsitem_timesince">'+timesince+'</span>';
	
	if (user.location != undefined && user.location != null)
	{
		template += ' from <span class="newsitem_geosource">'+user.location+'</span>';
	}
	
	// Close everything
	template += '</div>'; // Close newsitem_content
	template += '</div></div>'; // Close newsfeed_entry, newsfeed_item
	
	return template
}

function renderNewsfeed(response)
{
	newsfeed_items = new Array();
	for (entry in response.result)
	{
		_entry = response.result[entry];
		newsfeed_items.push(renderNewsfeedItem(_entry.key, _entry.type, _entry.kind, _entry.user, _entry.timesince, _entry.content_item, _entry.timestamp));
	}

	newsfeed_html = '';
	for (entry in newsfeed_items)
	{
		newsfeed_html += "\n\n"+newsfeed_items[entry];
	}
	
	$('.newsfeed_loading_wrapper').addClass('hidden');
	$('#newsfeed_entries').html(newsfeed_html);
	$('#newsfeed_entries').removeClass('hidden');
}

function newsfeedFailure(error)
{
	console.log('error', error);
}


_last_request = null;
function retrieveFeedByAjax(method, params, callbacks)
{
	_last_request = {method: method, params: params, callbacks: callbacks};
	function _makeAjaxRequest(m, p, c) {
		$.jsonRPC.setup({endPoint: '/_api/user/Newsfeed'});
		  $.jsonRPC.request(m, p,{

		          success: function(response)
		          {
						callback = c.success;
						callback(response);
		          },
		          error: function(response)
		          {
						callback = c.failure;
						callback(response)
		          }
		      }
		  );
	}
	
	_makeAjaxRequest(method, params, callbacks);
}

function refreshNewsfeed()
{
	$('#newsfeed_entries').addClass('hidden');
	$('.newsfeed_loading_wrapper').removeClass('hidden');
	
	if(_last_request != null)
	{
		retrieveFeedByAjax(_last_request.method, _last_request.params, _last_request.callbacks);
	}
	else
	{
		retrieveNewsfeed();
	}
}

function retrieveNewsfeed(user)
{
	retrieveFeedByAjax('getMainFeed', [user], {success: renderNewsfeed, failure: newsfeedFailure});
}

function retrieveSubscribedNewsfeed()
{
	
}

function retrieveFollowedNewsfeed()
{
	
}

function retrieveSocialNewsfeed()
{
	
}

function retrieveContentNewsfeed()
{
	
}