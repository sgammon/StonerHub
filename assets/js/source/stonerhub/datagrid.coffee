

class DatagridController extends StonerHubController

	constructor: (apptools, stonerhub) ->
	
		@_cache =
			lower: -1
		
		@_getkey = (data, key) =>
			for item in data
				if item.name == key
					return item.value
			return null
	
		@load = (service, source, method, params, query_params, callback) =>
			
			rpc_params = {}			
			need_server = false
			request_start = @_getkey query_params, "iDisplayStart"
			request_length = @_getkey query_params, "iDisplayLength"
			request_end = request_start + request_length
		
			rpc_params.query = {}
			rpc_params.query.limit = request_length
			rpc_params.query.offset = request_start
		
			request = $.apptools.api.rpc.createRPCRequest
				method: method,
				api: service,
				params: rpc_params,
				async: true
				
			$.apptools.dev.verbose 'Stonerhub:Datagrid', 'Grid RPC request: ', request
		
			request.fulfill
				success: (response) =>

					grid_data = []
					for data_item in response.data
						row = [data_item.key.value]
						obj = {}
						for field in response.datagrid.columns
							row.push data_item[field]
							obj[field] = data_item[field]
						grid_data.push row
						$.stonerhub.models[data_item.key.kind].register data_item.key.value, obj
					
													
					$.apptools.dev.verbose 'Stonerhub:Datagrid', 'Translated data map: ', grid_data
					
					response.datagrid.columns.splice(0, 0, 'key')
					
					datatables_result =
						sEcho: @_getkey query_params, 'sEcho'
						iTotalRecords: response.resultset.results_count
						iTotalDisplayRecords: response.resultset.returned_count
						aaData: grid_data
						sColumns: response.datagrid.columns.join(',')
					
					
					console.log('Final result', datatables_result)
					callback datatables_result
				
				failure: (response) =>
					alert 'Datagrid failure. See console.'
					$.apptools.dev.error 'Stonerhub:Datagrid', 'Grid RPC error: ', response