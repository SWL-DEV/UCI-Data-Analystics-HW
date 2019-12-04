// var data = [{
//     datetime: "1/1/2010",
//     city: "benton",
//     state: "ar",
//     country: "us",
//     shape: "circle",
//     durationMinutes: "5 mins.",
//     comments: "4 bright green circles high in the sky going in circles then one bright green light at my front door."
//   },

// from data.js
var tableData = data;

// YOUR CODE HERE!

var button = d3.select('#filter-btn');

button.on("click", function() {

  // Clear out existing table content if a previous query was run 
  d3.select("tbody").selectAll("*").remove()

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

  // Get a reference to the table body
  var tbody = d3.select("tbody");

  // Loop through the filteredData
  filteredData.forEach((data) => {

    // For each sighting, add a new row
    var row = tbody.append("tr");

    // For each sighting's date (key) and relevant values
    Object.entries(data).forEach(([key, value]) => {

      // Add a new cell for each value
      var cell = row.append("td");
        cell.text(value);

    
    });

  });

});