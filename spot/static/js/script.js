var loc
function EmbassyMap(data) {
  if (data[1]){ 
    var mapOptions =
    {
        mapTypeId: google.maps.MapTypeId.HYBRID
    }
    map1 = new google.maps.Map(document.getElementById("map1"), mapOptions);

    var address = data[1];
    var geocoder1 = new google.maps.Geocoder();
    geocoder1.geocode( { 'address': address}, function(results, status) {
        loc = results[0].geometry.location;
        console.log(loc);
        if (status == google.maps.GeocoderStatus.OK) {
          map1.setCenter(loc);
          map1.setZoom(18);
        }
        var marker = new google.maps.Marker({
          position: loc,
          map: map1,
          title: 'Embassy of ' + data[0]
      });
    });
  }
}

function CountryMap(data) {
  var mapOptions =
  {
      mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map2 = new google.maps.Map(document.getElementById("map2"), mapOptions);

  var address = data[0];
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
          map2.setCenter(results[0].geometry.location);
          map2.fitBounds(results[0].geometry.bounds);
      }
  }); 
}