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

button.on("click", function () {

  // Clear out existing table content if a previous query was run 
  d3.select("tbody").selectAll("*").remove()

  // Select the input element and get the raw HTML node
  var inputElement = d3.select(".form-control");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  // Attempting to search with multiple search boxes:
  // // Select the input element and get the raw HTML node
  // var inputElement = {
  // date: d3.select("#datetime"), 
  // city: d3.select("#city"),
  // state: d3.select("#state"),
  // country: d3.select("#country"),
  // shape: d3.select("#shape"),
  // };

  // // Get the value property of the input element
  // var inputValue = inputElement.value(); (<-- What to do here to have it equal to one of the values??)

  console.log(inputValue);


  // Create a filter for tableData to find various available input which matches the inputValue:
  function inputFilter(input) {
    return input.datetime === inputValue ||
      input.city === inputValue ||
      input.state === inputValue ||
      input.country === inputValue ||
      input.shape === inputValue;

  };

  var filteredData = tableData.filter(inputFilter);

  // If there is a match of keyword entered, then print data to table:
  if (filteredData != "") {
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
  }

  // If no match is found for keyword:
  else {
    console.log("No Matches Found");

    d3.select("tbody").append("tr").append("td").text("No Matches Found");
  };
});