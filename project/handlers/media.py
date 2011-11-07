from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.api import memcache

from project.handlers import WebHandler

from project.models.assets import ProfilePic


class ProfilePic(WebHandler):
	
	''' Outputs a user's profile picture, sized at 48x48 unless otherwise instructed. '''
	
	def get(self, username, format):
		
		key = db.Key.from_path('StoredAsset', 'ProfilePic::Current', parent=db.Key.from_path('User', username))
		r = self.api.memcache.get('SPIMedia//ProfilePic-'+str(key))
		if r is None:
			asset = db.get(key)
		
			if format.lower() != 'png' or format.lower() != 'jpeg':
				self.response.write('<b>Invalid format provided. Options are "png" or "jpeg".')
				return
			if format.lower() == 'jpg':
				format = 'jpeg'
		
			if asset is not None:
				img = self.api.images.Image(str(asset.datastore_data))		
			
				## Hotdog Style
				if img.width > img.height:
				
					left_x = 0.2
					top_y = 0.2
					right_x	= 0.7
					bottom_y = 0.7

					img.crop(left_x, top_y, right_x, bottom_y)				

				## Hamburger Style
				elif img.height > img.width:

					left_x = 0.2
					top_y = 0.2
					right_x	= 0.7
					bottom_y = 0.6
				
					img.crop(left_x, top_y, right_x, bottom_y)
			
				## Already square!! Yay
				img.resize(height=int(self.request.args.get('h', 48)), width=int(self.request.args.get('w', 48)))
			
				###### Perform operations!
				thumbnail = img.execute_transforms(output_encoding=getattr(images, format.upper()))
				r = self.response(thumbnail)
				r.headers['Content-Type'] = 'image/'+format
				self.api.memcache.set('SPIMedia//ProfilePic-'+str(key), r)

			else:
				return self.abort(404)

		return r