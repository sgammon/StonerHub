from google.appengine.ext import db
from project.core.data.properties.security import UserReferenceProperty

from project.core.grids import SPIDataGrid
from project.core.grids import get_model_grid


class SPIModelMixin(object):
	pass
	

class CreatedModifiedMixin(SPIModelMixin):
	
	''' Automatically appends createdAt and modifiedAt values to a model. These values are derived on put(). '''
	
	modifiedAt = db.DateTimeProperty(auto_now=True)
	createdAt = db.DateTimeProperty(auto_now_add=True)
	
	
class UserAuditMixin(SPIModelMixin):
	
	modifiedBy = UserReferenceProperty(auto_current_user=True)
	createdBy = UserReferenceProperty(auto_current_user_add=True)
	

class FormGeneratorMixin(SPIModelMixin):

	@classmethod
	def _get_form_config(cls):

		'''

		Converts a _form_config property on a model to a config format compatible with WTForms.

		'Field' in this case is a string referencing a property on a Google App Engine model
		that will eventually be converted into a form control.

		-----------------------------------------		
		_form_config Structure:
		-----------------------------------------

			- form (dict):
				A dict of arguments to pass to the form constructor.

			- exclude (list):
				A list of fields to exclude from the form.

			- fields (list of string or (2 or 3 member) tuple values]):
				This prop is taken to mean a list of the *only* fields to be included in the form.

				- If a string value is encountered, it considers it a regular field name.

				- If a two-member tuple value is encountered:
					- The first value is considered the field name.
					- If the second member is a dict, it is considered field arguments.
					- If the second member is also a string, it is considered a python module path
					  for an external form (wirestone.spi.forms is automatically prepended).

				- If a three-member tuple value is encountered:
					- The first value is considered the field name.
					- The second value is considered a python module path for an external form
					  (wirestone.spi.forms is automatically prepended).
					- The third value must be a dict, and is considered field arguments.


			- script_snippet (string or tuple of 2 strings):
				If a string is found, the form library operates on the 'north' section of a form
				in a template. If a tuple of 2 strings is found, it extracts them as 'north' and
				'south'.

				Once 'north' or ('north', 'south') are extracted, 'snippets/forms/' is prepended
				to the first or both values and included with the form object.

				If the form render macro encounters a form with either the first or both params,
				it includes them above (north) or below (south) of the form tag in a <script>
				element.


		'''

		# Default to 'none' for each cfg value
		cmp_config = {'exclude':None, 'only':None, 'field_list':None, 'field_args':None, 'form_args':None, 'script_snippet': None}

		if hasattr(cls, '_form_config'):

			f_cfg = getattr(cls, '_form_config')

			# Grab form constructor args
			if 'form' in f_cfg:
				cmp_config['form_args'] = f_cfg['form']

			# Grab 'exclude'
			if 'exclude' in f_cfg and 'only' not in f_cfg and 'fields' not in f_cfg: cmp_config['exclude'] = f_cfg['exclude']

			# Grab script snippet
			if 'script_snippet' in f_cfg: north, south = f_cfg['script_snippet'] or f_cfg['script_snippet'], None

			# Grab fields
			if 'fields' in f_cfg:
				cmp_config['field_list'] = []
				for form_field in f_cfg['fields']:

					if isinstance(form_field, tuple):

						# If it's a two member tuple...
						if len(form_field) == 2:

							field_name, value2 = form_field

							# If value2 is a string, it's a reference to an external form...
							if isinstance(value2, basestring):
								form_field = (field_name, value2)

							# Else if value2 is a dict, it's args for the field
							elif isinstance(value2, dict):
								if not isinstance(cmp_config['field_args'], dict): cmp_config['field_args'] = {}
								cmp_config['field_args'][field_name] = value2
								form_field = field_name


						# If it's a three member tuple...	
						if len(form_field) == 3:
							field_name, ext_form, field_args = form_field
							if not isinstance(cmp_config['field_args'], dict): cmp_config['field_args'] = {}
							cmp_config['field_args'][field_name] = field_args
							form_field = (field_name, ext_form)


					cmp_config['field_list'].append(form_field)

		return cmp_config
		

		from tipfy import url_for
		from wirestone.spi.core.data import SPIModelMixin

		from wirestone.spi.core.grids import SPIDataGrid
		from wirestone.spi.core.grids import get_model_grid


class GridGeneratorMixin(SPIModelMixin):

	@classmethod
	def _get_grid_config(cls):

		'''

		Converts a _grid_config property on a model to a config object for generating model forms on the fly.

		'Field' in this case is a string referencing a property on a Google App Engine model
		that could eventually be converted into a grid column.

		-----------------------------------------		
		_grid_config Structure:
		-----------------------------------------

			- grid (dict):
				A dict of arguments to pass to the form constructor.

			- exclude (list):
				A list of fields to exclude from the form.

			- columns (list of string or (2 or 3 member tuples) tuple values):
				This prop is taken to mean a list of the *only* properties/columns to be included in the grid.

				- If a two-member tuple value is encountered:
					- The first value is considered the column label.
					- The second value is considered the property name.

				- If a three-member tuple is encountered:
					- The first value is considered the column label.
					- The second value is considered the property name.
					- The third value is considered arguments to pass to the script column entry in Datagrids.

			- script_snippet (string or tuple of 2 strings):
				If a string is found, the form library operates on the 'north' section of a form
				in a template. If a tuple of 2 strings is found, it extracts them as 'north' and
				'south'.

				Once 'north' or ('north', 'south') are extracted, 'snippets/forms/' is prepended
				to the first or both values and included with the form object.

				If the form render macro encounters a form with either the first or both params,
				it includes them above (north) or below (south) of the form tag in a <script>
				element.


		'''

		# Default to 'none' for each cfg value
		cmp_config = {'columns':None, 'column_args':None, 'grid_args':None, 'script_snippet': (None, None)}

		if hasattr(cls, '_grid_config'):

			g_cfg = getattr(cls, '_grid_config')

			# Grab grid constructor args
			if 'grid' in g_cfg:
				cmp_config['grid_args'] = g_cfg['grid']

			# Grab script snippet
			if 'script_snippet' in g_cfg:
				val = g_cfg['script_snippet']
				if isinstance(val, tuple):
					north, south = g_cfg['script_snippet']
					cmp_config['script_snippet'] = (north, south)
				else:
					north = g_cfg['script_snippet']
					cmp_config['script_snippet'] = (north, None)

			# Grab fields
			if 'columns' in g_cfg:
				cmp_config['columns'] = []
				for column in g_cfg['columns']:

					if isinstance(column, tuple):

						# If it's a two member tuple...
						if len(column) == 2:
							column_name, column_label = column
							column_args = None

						# If it's a three member tuple...
						if len(column) == 3:
							column_name, column_label, column_args = column

					cmp_config['columns'].append((column_name, column_label, column_args))

			return cmp_config

		else:
			return None


	@classmethod
	def generateGrid(cls, **kwargs):

		## Follow config or autogenerate one
		cfg = cls._get_grid_config()
		if cfg is not None:
			grid = SPIDataGrid(config=cfg, **kwargs)				
		else:
			grid = get_model_grid(cls)

		## Return Grid
		return grid