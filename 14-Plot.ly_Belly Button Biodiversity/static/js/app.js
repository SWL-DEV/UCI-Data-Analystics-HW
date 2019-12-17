function barPlot() {
    d3.json("../samples.json").then(function(data) {
    
    var id = data.samples.id;
    var otuID = data.samples.otu_ids;
    var values = data.samples.sample_values;
    var label = data.samples.otu_labels;

    var sortedValues = values.sort((a,b) => b - a);

    var slicedValues = sortedValues.slice(0, 10);

    var trace = {
        type: "bar",
        orientation: "h",
        x: slicedValues,
        y: label
    };

    var data = [trace];

    var layout = {

    }
});

}