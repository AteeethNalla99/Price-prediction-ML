function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

// Attach event listener properly
$(document).ready(function() {
  $('#estimatePriceBtn').click(onClickedEstimatePrice);
});

function onClickedEstimatePrice(event) {
  event.preventDefault();
  console.log("Estimate price button clicked");
  
  var sqft = parseFloat($('#uiSqft').val());
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = $('#uiLocations').val();
  var estPrice = $('#uiEstimatedPrice');

  // Basic validation
  if (isNaN(sqft)) {
    alert("Please enter a valid area (sqft)");
    return;
  }
  if (!location) {
    alert("Please select a location");
    return;
  }

  estPrice.html("<h2>Estimating...</h2>");

  $.post("http://127.0.0.1:5000/predict_home_price", {
    total_sqft: sqft,
    bhk: bhk,
    bath: bathrooms,
    location: location
  }).done(function(data) {
    estPrice.html("<h2>" + data.estimated_price + " Lakh</h2>");
  }).fail(function(error) {
    estPrice.html("<h2>Error estimating price</h2>");
  });
}


function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  // Use this if  you are using nginx. i.e tutorial 8 and onwards
 $.get("http://127.0.0.1:5000/get_location_names", function(data) {
    if(data && data.locations) {
        var $loc = $('#uiLocations');
        $loc.empty();
        $loc.append('<option value="" disabled selected>Choose a Location</option>');
        data.locations.forEach(function(location) {
            $loc.append($('<option></option>').val(location).text(location));
        });
    }
});
        
      
  }


window.onload = onPageLoad;