// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var chartMargin = {
	top: 30,
	right: 30,
	bottom: 30,
	left: 30,
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right
var ChartHeight = svgHeight - chartMargin.top - chartMargin.bottom

// Select body, append SVG area on it, and set the dimensions
var svg = d3
	.select("body")
	.append("svg")
		.attr("height",svgWidth)
		.attr("width",svgWidth)
	// Append a group to the SVG area and shift('translate') it
	.append("g")
		.attr("transform","translate(" + chartMargin.right + ", " + chartMargin.top + ")");

// Configure a band scale, with a range between 0 and the chartWidth and a padding of 0.1 (10%) 
var xBandScale = d3.scaleBand().range([0, chartWidth]).padding(0.1);

// Create a linear scale, with a range between the chartHeight and 0.
var yLinearScale = d3.scaleLinear().range([chartHeight, 0]);

// Load data from belly button biodiversity.csv
d3.csv("belly_buttom_biodiversity.sqlite", function(error, tv)){
		if (error) throw error;

	console.log(tvData)

	// Cast the hours value to a number for each piece of tvData
	tvData.forEach(function(data) {
		data.hours = +data.hours;
	});

	// Set the domain of the band scale to the names of students 
	xBandScale.domain(tvData.map(function(data) {
		return data.name;
	}));

	// Set the domain of the linear scale to 0 and the largest 
	yLinearScale.domain([0, d3.maxtvData.map(function(data) {
	return data.hours;
	})]);

	// Create two new functions passing our scales in as arguments
	// These will be used to create the chart's axes
	var bottomAxis = d3.axisBottom(xBandScale);
	var leftAxis = d3.axisLeft(yLinearScale).ticks(10);

	// Create one SVG rectangle per piece of tvData
	// Use the linear and band scales to position each rectangles within the chart
	svg
 	.selectAll(".bar")
 		.data(tvData)
 		.enter()
 		.append("rect")
 	  		.attr("class","bar")
 			.attr("x", function(data){
 				return xBandScale(data.name);
 			})
 			.attr("y", function(data){
 				return yLinearScale(data.hours);
 			})
 			.attr("width", xBandScale.bandwidth())
 			.attr("height", function(data){
 				return chartHeight - yLinearScale(data.hours);
 		});
	
	// Append two SVG group elements to the SVG area, create the bottom and left axes
	svg.append("g")
		.call(leftAxis);

	svg.append("g")
	.attr("transform","translate(0" + chartHeight + ")")
	.call(bottomAxis);
});