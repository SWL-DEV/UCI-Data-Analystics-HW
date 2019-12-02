// from data.js
var tableData = data;

// var data = [{
//     datetime: "1/1/2010",
//     city: "benton",
//     state: "ar",
//     country: "us",
//     shape: "circle",
//     durationMinutes: "5 mins.",
//     comments: "4 bright green circles high in the sky going in circles then one bright green light at my front door."
//   },

// YOUR CODE HERE!


var button = d3.select('#filter-btn');

button.on("click", function() {

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  // Create a filter for tableData to find datetime which matches the inputValue
  function dateFilter(input) {
    return input.datetime === inputValue;
  }
  
  var filteredData = tableData.filter(dateFilter);
  
  console.log(filteredData);


});