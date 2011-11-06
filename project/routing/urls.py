# -*- coding: utf-8 -*-
"""URL definitions."""
from webapp2 import Route
from webapp2_extras.routes import HandlerPrefixRoute

rules = [

	HandlerPrefixRoute('project.handlers.', [
	
		## === Main URLs === ##
		HandlerPrefixRoute('main.', [

	        Route('/', name='landing', handler='Landing'),
	        Route('/newsfeed', name='newsfeed', handler='Newsfeed'),
			Route('/offline', name='offline', handler='Offline'),
			Route('/go', name='shortcut', handler='ShortURL')
		
		]),

		## === Security URLs === ##
		HandlerPrefixRoute('security.', [

			## Login/Logout
			Route('/login', name='auth/login', handler='Login'),
			Route('/logout', name='auth/logout', handler='Logout'),
			
			## Registration
			Route('/register', name='auth/signup', handler='RegisterBeta'),
			Route('/_frame/register/step<step>/ticket/<ticket>', name='auth/signup/frame', handler='RegisterBetaFrame')
		
		]),

		# ==== Service Handlers ==== #

		HandlerPrefixRoute('incoming.', [

			# Incoming Services
			Route('/_ah/mail/<alias>', name='incoming-mail', handler='IncomingMail'),
			Route('/_ah/xmpp/message/chat/', name='incoming-xmpp', handler='IncomingChat')
			
		]),
		
		HandlerPrefixRoute('workers.data.', [
		
			# Cron Handlers
			Route('/_workers/data/ticketManager/collectGarbage', name='ticket-manager-collect-garbage', handler='ticket.CollectGarbage'),
			Route('/_workers/data/sessionManager/collectGarbage', name='session-manager-collect-garbage', handler='session.CollectGarbage'),
			Route('/_workers/data/pipelineManager/collectGarbage', name='pipeline-manager-collect-garbage', handler='pipelines.CollectGarbage'),
			Route('/_workers/data/blobManager/collectGarbage', name='blob-manager-collect-garbage', handler='blob.CollectGarbage')
		
		]),
		
		# Queue Handlers
		Route('/_workers/mail/outbound', name='outbound-mail', handler='workers.mail.OutgoingMail'),

		# Admin Handlers
		Route('/manage', name='admin-index', handler='admin.Index'),

		# ==== Dev Handlers ==== #
		HandlerPrefixRoute('dev.', [
		
			Route('/something-broke-please-fix-it', name='file-bug', handler='FileBug'),
	        Route('/dev', name='dev-index', handler='Index'),
	        Route('/dev/cache', name='dev-cache', handler='Cache'),
	        Route('/dev/environment', name='dev-environ', handler='Environment'),
			Route('/dev/default_data', name='dev-default-data', handler='DefaultData'),
			Route('/dev/security', name='dev-security', handler='Security'),
			Route('/dev/security/claims', name='dev-security-claims', handler='ManageAccountClaims'),
			Route('/dev/security/claims/<action>', name='dev-security-claims-action', handler='ManageAccountClaims'),
			Route('/dev/indexer', name='dev-indexer', handler='IndexerRoot'),
			Route('/dev/indexer/insertTask', name='dev-indexer-enqueue-task', handler='IndexerMakeTask'),
			Route('/dev/security/claims/<key>/<action>', name='dev-security-claims-key-action', handler='ManageAccountClaims'),
			Route('/dev/shell', name='dev-shell', handler='Shell')
			
		]),
		
		## User Handlers
		HandlerPrefixRoute('user.', [
		
			## == User Pages == #
			Route('/me', name='user-profile', handler='Profile'),
	        Route('/people/<username>', name='user-public-profile', handler='Profile'),
			Route('/people/<username>/tags', name='user-public-tags', handler='Tags'),
			Route('/people/<username>/content', name='user-public-content', handler='Content'),
			Route('/people/<username>/comments', name='user-public-comments', handler='Comments'),
			
			# == Utility Frames == #
			Route('/_frame/user/profileEdit', name='user-profile-edit-frame', handler='ProfileFrame'),
			Route('/_frame/user/settingsEdit', name='user-settings-edit-frame', handler='SettingsFrame'),
			Route('/_frame/user/manageSubscriptions', name='user-manage-subscriptions-frame', handler='SubscriptionsFrame'),
	
			# == User Utilities == #
			Route('/me/tags', name='user-tags', handler='Tags'),
			Route('/me/queue', name='user-queue', handler='Queue'),			
			Route('/me/content', name='user-content', handler='Content'),
			Route('/me/comments', name='user-comments', handler='Comments'),
			
			# == User Settings == #			
	        Route('/me/settings', name='user-settings', handler='Settings'),
			Route('/me/settings/<group>', name='user-settings-group', handler='SettingsGroup'),
			Route('/me/settings/<group>/save', name='user-settings-save', handler='SettingsGroup'),

			# == Social Notifications == #
	        Route('/me/notifications', name='user-notifications', handler='Notifications')
		
		]),
		
		## Search Handlers
		HandlerPrefixRoute('search.', [
		
	        Route('/search', name='search-global', handler='Main'),
	        Route('/search/<query>', name='search-query', handler='Main'),
			Route('/search/<filters>', name='search-query-with-filters', handler='Main')
		
		]),
		
		## Repository Handlers
		HandlerPrefixRoute('repository.', [
		
			# == CRUD == #
	        Route('/repositories', name='repository-list', handler='List'),
	        Route('/repositories/create', name='repository-create', handler='Create'),
	        Route('/repositories/<repo>', name='repository-view', handler='View'),
	        Route('/repositories/<repo>/edit', name='repository-edit', handler='Edit'),
	        Route('/repositories/<repo>/edit/permissions', name='repository-edit-permissions', handler='Permissions'),
	        Route('/repositories/<repo>/delete', name='repository-delete', handler='Delete'),

			# == Content/Tags == #
	        Route('/repositories/<repo>/tags', name='repository-tags', handler='Tags'),
			Route('/repositories/<repo>/categories', name='repository-categories', handler='Categories'),
			Route('/repositories/<repo>/category/create', name='repository-category-create', handler='CreateCategory'),
	        Route('/repositories/<repo>/content', name='repository-content', handler='Content'),
			Route('/repositories/<repo>/content/recent', name='repository-recent-content', handler='RecentContent'),
			Route('/repositories/<repo>/content/popular', name='repository-popular-content', handler='PopularContent'),
			Route('/repositories/<repo>/content/<filters:\s>', name='repository-filter-content', handler='FilteredContent')
		
		]),
		
		## Content Handlers
		HandlerPrefixRoute('content.', [
		
			# == Basic Views == #
			Route('/content', name='content-global', handler='Main'),
			Route('/content/all', name='content-all', handler='All'),
			Route('/content/mine', name='content-mine', handler='ByCurrentUser'),
			Route('/content/recent', name='content-recent', handler='Recent'),
			
			# == Content Uploader == #
			Route('/content/create', name='content-create', handler='Create'),
			Route('/content/create/step<progress:\d{1}>', name='content-create-step', handler='Create'),
			Route('/content/create/success', name='content-create-success', handler='CreateSuccess'),
			Route('/content/create/step<progress:\d{1}>/<blobkey>', name='content-create-step-blobkey', handler='Create'),
			Route('/content/create/step<int:\d{1}>/<sessionkey>/<blobkey>', name='content-create-step-blobkey-with-session', handler='Create'),
			Route('/content/create/step<int:\d{1}>/<sessionkey>/<blobkey>/<action>', name='content-create-step-blobkey-with-session-with-action', handler='Create'),

	        # == Content Handlers (Repository-Oriented) == #
	        Route('/repositories/<repo>/content/create', name='content-item-create', handler='Create'),
	        Route('/repositories/<repo>/content/create/step<progress:\d{1}>', name='content-item-create-step', handler='Create'),
	        Route('/repositories/<repo>/content/create/step<int:\d{1}>/<blobkey>', name='content-item-create-step-blobkey', handler='Create'),
	        Route('/repositories/<repo>/content/create/step<int:\d{1}>/<blobkey>/<sessionkey>', name='content-item-create-step-blobkey-with-session', handler='Create'),	
	        Route('/repositories/<repo>/content/create/success', name='content-item-create-success', handler='CreateSuccess'),
	        Route('/repositories/<repo>/content/<key>', name='content-item-view', handler='View'),
	        Route('/repositories/<repo>/content/<key>/edit', name='content-item-edit', handler='Edit'),
	        Route('/repositories/<repo>/content/<key>/edit/permissions', name='content-item-edit-permissions', handler='Permissions'),
	        Route('/repositories/<repo>/content/<key>/delete', name='content-item-delete', handler='Delete'),
		
		]),
		
		## Tag Handlers
		HandlerPrefixRoute('tags.', [
		
			# == Basic Views == #
	        Route('/tags', name='tags-global', handler='tags.GlobalTags'),
	        Route('/tags/all', name='tags-all', handler='tags.GlobalTags'),
	        Route('/tags/mine', name='tags-mine', handler='tags.Mine'),		
	        Route('/tags/popular', name='tags-popular', handler='tags.Popular'),
	        Route('/tags/<tag>', name='tag-view', handler='tags.View'),
	        Route('/tags/<tag>/edit', name='tag-edit', handler='tags.Edit'),
	        Route('/tags/<tag>/delete', name='tag-delete', handler='tags.Delete')
		
		]),
		
		## Blob/Asset Handlers
		HandlerPrefixRoute('media.', [
		
			# == Blob Service == #
			Route('/_media/blob/serve/<blobkey>', name='media-serve-blob', handler='SPIServeHandler'),
			Route('/_media/blob/serve/<blobkey>/<filename>', name='media-serve-blob-filename', handler='SPIServeHandler'),
		
			# == Blob Download Service == #
			Route('/_media/blob/download/<blobkey>', name='media-download-blob', handler='SPIDownloadHandler'),
			Route('/_media/blob/download/<blobkey>/<filename>', name='media-download-blob-filename', handler='SPIDownloadHandler'),

			# == Profile Images Service == #
			Route('/_media/img/profile/serve/<username>-profile.<format>', name='media-serve-profile-pic', handler='ProfilePic')
		
		]),
		
		## AJAX Handlers
		HandlerPrefixRoute('ajax.', [
		
			# == AJAX Upload URL Service == #
			Route('/_ajax/upload/generateURL', name='ajax-upload-generate-url', handler='upload.GenerateUploadURL'),
			Route('/_ajax/upload/callback/uploadSuccess', name='ajax-upload-success', handler='upload.UploadCallback'),			
			Route('/_ajax/upload/callback/uploadSuccess/<string:sessionkey>', name='ajax-upload-success-with-session', handler='upload.UploadCallback'),
			Route('/_ajax/upload/callback/passThrough/<string:blobkey>', name='ajax-upload-success-passthrough', handler='upload.UploadCallback'),
			Route('/_ajax/upload/callback/passThrough/<string:sessionkey>/<string:blobkey>', name='ajax-upload-success-passthrough-with-session', handler='upload.UploadCallback'),			
		
			# == Social Actions/Notifications Service == #
			Route('/_ajax/social/<string:action>/<string:document>', name='ajax-social', handler='social.SocialAction'),
			Route('/_ajax/social/notification/<string:key>/<string:action>', name='ajax-social-notification', handler='social.SocialNotification'),
			Route('/_ajax/social/notifications', name='ajax-social-notifications', handler='social.Notifications'),
			Route('/_ajax/social/likes/<string:key>', name='ajax-social-likes', handler='social.Likes'),
			Route('/_ajax/social/comments/<string:key>', name='ajax-social-comments', handler='social.Comments'),
			Route('/_ajax/social/sharebox', name='ajax-social-sharebox', handler='social.ShareBox'),
			Route('/_ajax/social/subscribe', name='ajax-social-subscribebox', handler='social.SubscribeBox'),
			Route('/_ajax/social/feeds', name='ajax-social-feedsbox', handler='social.FeedsBox'),
		
		])
	
	])
]
