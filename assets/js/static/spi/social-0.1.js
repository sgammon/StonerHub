
channelMessage = null;
channelPayload = null;
channelError = null;

/* === Channel Functions === */
function OnChannelOpen()
{
}

function OnChannelMessage(message)
{
	payload = JSON.parse(message.data);
	if (payload['type'] == 'SocialNotification')
	{
		if (payload['kind'] == 'Like')
		{
			socialNotification(payload['id'], payload['kind']+'Notification', '+1 New Like Notification');
		}
		else if (payload['kind'] == 'Comment')
		{
			socialNotification(payload['id'], payload['kind']+'Notification', '+1 New Comment Notification');
		}
		else if (payload['kind'] == 'Share')
		{
			socialNotification(payload['id'], payload['kind']+'Notification', '+1 New Share Notification');
		}		
	}
	channelMessage = message;
	channelPayload = payload;
}

function OnChannelError(error)
{
}

function OnChannelClose()
{
}

function CreateSocket(channel)
{
	o = channel.open();
	o.onopen = OnChannelOpen;
	o.onmessage = OnChannelMessage;
	o.onerror = OnChannelError;
	o.onclose = OnChannelClose;
	return o;
}

social = {Socket:CreateSocket};


/* === Social Functions === */
function socialNotification(id, type, text)
{
	notificationCount = notificationCount+1;
	$('#stackBoxes').append("<div class='stackBox "+type+"' id='"+id+"' style='display:none;'><p>"+text+"</p></div>");
	$('#notificationCount').text(notificationCount);
	$('#notifications').show();
	$('#'+id).slideToggle();
	$('#'+id).delay(1000).fadeOut(1000);
}

function likeOperationSuccess(data, textStatus, xhr)
{
	$('#youLike').removeClass('hidden');
	$('.likeButtonBox').toggleClass('likeButtonBox unlikeButtonBox');
	$('#likeUnlikeAction').toggleClass('likeButton unlikeButton').text('Unlike');
}

function likeOperationFailure(xhr, textStatus, error)
{
	alert('There was an error trying to like this document. Error details: '+error+'.');
}

function unlikeOperationSuccess(data, textStatus, xhr)
{
	$('#youLike').addClass('hidden');
	$('.unlikeButtonBox').toggleClass('unlikeButtonBox likeButtonBox');	
	$('#likeUnlikeAction').toggleClass('likeButton unlikeButton').text('Like');
}

function unlikeOperationFailure(xhr, textStatus, error)
{
	alert('There was an error trying to unlike this document. Error details: '+error+'.');
}

function getCommentHtml(comment_key, firstname, lastname, profile_href, profile_pic_href, comment_text)
{
	comment_html = "<div class='commentBox transparent' id='"+comment_key+"'><div class='floatleft profilepic'>";
	comment_html += "<img src='"+profile_pic_href+"' alt='dummy profile pic' />";
	comment_html += "</div><div class='floatleft commentBody'><div class='commentText'>";
	comment_html += "<a href='"+profile_href+"'>"+firstname+" "+lastname+"</a> "+comment_text+"</div>";
	comment_html += "<div class='commentTagline'>Just now - <a href='#' class='commentDelete' onclick='deleteComment(\""+comment_key+"\");'>Delete</a></div></div><div class='clearboth'></div></div>";
	return comment_html;
}

function commentOperationSuccess(data, textStatus, xhr)
{
	$('#commentsContainer').append(
				getCommentHtml(data.response.key,
								PageObj.user.firstname,
								PageObj.user.lastname,
								PageObj.user.profile_href,
								PageObj.user.profile_pic_href,
								$('#commentBodyInput').val()));
	
	$('.commentCount').text(++PageObj.content_item.comment_count);
	$('.commentBox.transparent').animate({opacity:1.0}).removeClass('transparent');	
	$('#commentBodyInput').val('Write a comment...');
}

function commentOperationFailure(xhr, textStatus, error)
{
	alert('There was an error trying to save your comment. Please try again.');
}

function likeUnlike()
{
	if ($('#likeUnlikeAction').hasClass('likeButton'))
	{
		$.ajax({
			type: 'POST',
			url: PageObj.like_action_url,
			async:true,
			success:likeOperationSuccess,
			error:likeOperationFailure
		});
	}
	else if ($('#likeUnlikeAction').hasClass('unlikeButton'))
	{
		$.ajax({
			type: 'POST',
			url: PageObj.unlike_action_url,
			async:true,
			success:unlikeOperationSuccess,
			error:unlikeOperationFailure
		});
	}
}

function uncommentOperationSuccess(data, textStatus, xhr)
{
	$('.commentCount').text(--PageObj.content_item.comment_count);
	$('#'+data.response.key).animate({opacity:0.0, display:'none', visbility:'hidden'}, {complete: $('#'+data.response.key).remove()});
}

function uncommentOperationFailure(xhr, textStatus, error)
{
	alert('There was an error while trying to delete the selected comment. Please try again.');
}

function generateDeleteCommentAction(id)
{
	base_url = PageObj.uncomment_action_url;
	return base_url+'?action_key='+id;
}

function deleteComment(id)
{
	$.ajax({
		type: 'POST',
		url: generateDeleteCommentAction(id),
		async:true,
		success:uncommentOperationSuccess,
		error:uncommentOperationFailure
	});
}

$('#likeUnlikeAction').click(likeUnlike);

$('#commentBodyInput').focus(function (){
	if ($('#commentBodyInput').val() == 'Write a comment...'){$('#commentBodyInput').text('');}
});

$('#commentBodyInput').blur(function (){
	if ($('#commentBodyInput').val() == ''){$('#commentBodyInput').text('Write a comment...');}
});

function makeComment()
{
		$.ajax({
			type: 'POST',
			url: PageObj.comment_action_url,
			async:true,
			success:commentOperationSuccess,
			error:commentOperationFailure,
			data:{body:$('#commentBodyInput').val()}
		});
}