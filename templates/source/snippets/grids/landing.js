
jsonData = null

function spiPreProcess(data)
{
	jsonData = data

	records = []
	for (index in data.response.records)
	{
		records.push({'cell':[data.response.records[index].properties.title]});
	}
	
	return {'total':records.length, 'page':1, 'rows':records};
}