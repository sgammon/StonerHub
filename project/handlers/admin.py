from project.handlers import WebHandler


class Index(WebHandler):
	
	def get(self):
		self.render('admin/index.html')