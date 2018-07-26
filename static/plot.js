var sample = document.querySelector("#selDataset")
var sample = document.querySelector("#metaList")

function optionChanged(newValue){
	//update metadata
	d3.json("/metadata/"+newValue,function(error2,dataset3){
		datasetKeys = Object.keys(dataset3);
		// remove old text
		metaList.innerHTML = '';
		for(var i = 0; i < datasetKeys.length; i++){
			var newP = document.createElement("p");
			newP.innerHTML = datasetKeys[i] + ": " + dataset3[datasetKeys[i]];
			metaList.appendChild(newP);
		}
	}
	)
	// update pieChart
	// update bubblechart
	 // draw pie plot and the bubble chart!
	 d3.json("/samples/"+newValue, function(error, dataset){

	 	//get the top 10
	 	var sampleValues10 = dataset[0].sample_values.slice(0,10);
	 	var otuIDs10 = dataset[0].otu_ids.slice(0,10);

	 	// all of the records - for the bubble chart
	 	var sampleValuesFull = dataset[0].sample_values;

	 	// first ten records for pie chart will go here

	 })
}

	//update piechart
	//update bubblechart
		//draw pie plot and the bubble chart
	d3.json("") {

		// get the top 10
		var sampleValues10 = dataset[0].sample_values.slice(0,10);
		var otuIDs10 = dataset[0].otu_ids.slice(0,10);

		// all of the records - for the bubble chart
		var sampleValuesFull = dataset[0].sample_values;
		var otuIDsFull = dataset[0].otu_ids;

		// first ten records for pie chart will go here
		var otuDesc10 = [];
		var otuDescFull = [];

		// get the descriptions
		d3.json(""){

		}
	}