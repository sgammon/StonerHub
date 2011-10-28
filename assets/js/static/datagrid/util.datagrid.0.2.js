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

var oCache = {
				iCacheLower: -1
			};
			
function fnSetKey( aoData, sKey, mValue )
{
	for ( var i=0, iLen=aoData.length ; i<iLen ; i++ )
	{
		if ( aoData[i].name == sKey )
		{
			aoData[i].value = mValue;
		}
	}
}

function fnGetKey( aoData, sKey )
{
	for ( var i=0, iLen=aoData.length ; i<iLen ; i++ )
	{
		if ( aoData[i].name == sKey )
		{
			return aoData[i].value;
		}
	}
	return null;
}

function processRPCResponse(response)
{
	var result = {};
	
	rpcTracker['dataObjects'] = {};
	result['sEcho'] = response.result['sEcho'];
	result['iTotalRecords'] = response.result['iTotalRecords'];
	result['iTotalDisplayRecords'] = response.result['iTotalDisplayRecords'];
	result['sColumns'] = response.result['sColumns'];	
	result['aaData'] = [];
	
	response.result.data.forEach(function(item) {

		var row = [item.key.value];
		var obj = {};
		
		response.result.gridProto.forEach(function(property){	
			row.push(item.properties[property])
		});
		result['aaData'].push(row);
		
		response.result.modelProto.properties.forEach(function(property){	
			obj[property.name] = item.properties[property.name];
		});
		rpcTracker['dataObjects'][item.key.value] = obj;
		
	});
	
	rpcTracker['gridDataResult'] = result;
	return result
}

function loadSpiDatagrid ( sSource, sMethod, oParams, aoData, fnCallback )
{
	var iPipe = 5; /* Ajust the pipe size */
	
	var bNeedServer = false;
	var sEcho = fnGetKey(aoData, "sEcho");
	var iRequestStart = fnGetKey(aoData, "iDisplayStart");
	var iRequestLength = fnGetKey(aoData, "iDisplayLength");
	var iRequestEnd = iRequestStart + iRequestLength;
	oCache.iDisplayStart = iRequestStart;
	
	/* outside pipeline? */
	if ( oCache.iCacheLower < 0 || iRequestStart < oCache.iCacheLower || iRequestEnd > oCache.iCacheUpper )
	{
		bNeedServer = true;
	}
	
	/* sorting etc changed? */
	if ( oCache.lastRequest && !bNeedServer )
	{
		for( var i=0, iLen=aoData.length ; i<iLen ; i++ )
		{
			if ( aoData[i].name != "iDisplayStart" && aoData[i].name != "iDisplayLength" && aoData[i].name != "sEcho" )
			{
				if ( aoData[i].value != oCache.lastRequest[i].value )
				{
					bNeedServer = true;
					break;
				}
			}
		}
	}
	
	/* Store the request for checking next time around */
	oCache.lastRequest = aoData.slice();
	
	if ( bNeedServer )
	{
		if ( iRequestStart < oCache.iCacheLower )
		{
			iRequestStart = iRequestStart - (iRequestLength*(iPipe-1));
			if ( iRequestStart < 0 )
			{
				iRequestStart = 0;
			}
		}
	
		oCache.iCacheLower = iRequestStart;
		oCache.iCacheUpper = iRequestStart + (iRequestLength * iPipe);
		oCache.iDisplayLength = fnGetKey( aoData, "iDisplayLength" );
		fnSetKey( aoData, "iDisplayStart", iRequestStart );
		fnSetKey( aoData, "iDisplayLength", iRequestLength*iPipe );

		/* Pack datagrid-specific params to the 'query' parameter */
		oParams['query'] = aoData;
	
		/* Make request */
		$.jsonRPC.setup({endPoint: sSource});
		$.jsonRPC.request(sMethod, oParams,{

				success: function(response)
				{
					result = processRPCResponse(response, aoData['sEcho']);
					oCache.lastJson = jQuery.extend(true, {}, result);
					if ( oCache.iCacheLower != oCache.iDisplayStart )
					{
						result.aaData.splice( 0, oCache.iDisplayStart-oCache.iCacheLower );
					}
					result.aaData.splice( oCache.iDisplayLength, result.aaData.length );
					fnCallback(result);
				},
				error: function(response)
				{
					alert('datagrid failure: '+response.error);
				}
			}
		);
		
	}
	else
	{
		json = jQuery.extend(true, {}, oCache.lastJson);
		json.sEcho = sEcho; /* Update the echo for each response */
		json.aaData.splice( 0, iRequestStart-oCache.iCacheLower );
		json.aaData.splice( iRequestLength, json.aaData.length );
		fnCallback(json);
		return;
	}
}