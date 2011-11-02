from wtforms import fields
from project.core.forms import SPIForm


class FileBugForm(SPIForm):
	
	title = fields.TextField(default='e.g. "My profile picture isn\'t displaying"')
	description = fields.TextAreaField(label='What happened?')