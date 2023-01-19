let qry_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
// let qry_url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2021-01-01&endtime=2021-01-02&maxlongitude=-69.52148437&minlongitude=-123.83789062&maxlatitude=48.74894534&minlatitude=25.16517337";

let earthquake_count = 0;
let updatedAt = null
d3.json(qry_url).then(function (data) {
  console.log(data);
  console.log(data.features);
  earthquake_count = data.metadata.count;
  var date = new Date(data.metadata.generated);
  updatedAt = date.toString();
  console.log(earthquake_count);
  console.log(updatedAt);
  createFeatures(data.features);
});



function createFeatures(earthquakeData) {

  // Define a function that we want to run once for each feature in the features array.
  // Give each feature a popup that describes the place and time of the earthquake.
  function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>${feature.properties.place}</h3><hr>
    <h3>mag: ${feature.properties.mag}</h3>
    <h3>depth: ${feature.geometry.coordinates[2]}</h3>
    <p>${new Date(feature.properties.time)}</p>`);
  }

  // Create a GeoJSON layer that contains the features array on the earthquakeData object.
  // Run the onEachFeature function once for each piece of data in the array.
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature
  });

  // Send our earthquakes layer to the createMap function/
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Create the base layers.
  var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Create a baseMaps object.
  var baseMaps = {
    "Street Map": street,
    "Topographic Map": topo
  };

  // Create an overlay object to hold our overlay.
  var overlayMaps = {
    Earthquakes: earthquakes
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load.
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street, earthquakes]
  });

  // Create a legend to display information about our map.
  var info = L.control({
    position: "bottomright"
  });

  // When the layer control is added, insert a div with the class of "legend".
  info.onAdd = function () {
    var div = L.DomUtil.create("div", "legend");
    return div;
  };
  // Add the info legend to the map.
  info.addTo(myMap);

  // Create a layer control.
  // Pass it our baseMaps and overlayMaps.
  // Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

  updateLegend(updatedAt, earthquake_count);

}

// Update the legend's innerHTML with the last updated time and station count.
function updateLegend(updatedAt, earthquake_count) {
  document.querySelector(".legend").innerHTML = [
    "<p>Updated: " + updatedAt + "</p>",
    "<p>Count: " + earthquake_count + "</p>",
    "<p class='under_10'>'-10-10'</p>",
    "<p class='under_30'>'10-20'</p>",
    "<p class='under_50'>'30-50'</p>",
    "<p class='under_70'>'50-70'</p>",
    "<p class='under_90'>'70-90'</p>",
    "<p class='over_90'>'90+'</p>"
  ].join("");
}