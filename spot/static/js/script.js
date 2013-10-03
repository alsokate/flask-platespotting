function EmbassyMap() {
  var mapOptions = {
    center: new google.maps.LatLng(38.942404, -77.066349),
    zoom: 16,
    mapTypeId: google.maps.MapTypeId.HYBRID
  };

  var emb_map = new google.maps.Map(document.getElementById("map1"),
      mapOptions);

  var marker = new google.maps.Marker({
    position: emb_map.getCenter(),
    map: emb_map,
    title: 'Embassy of' + ' China'
  });  
}

var geocoder;
var map;

function CountryMap(data) {
  console.log(this, arguments)
  var mapOptions =
  {
      mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("map2"), mapOptions);

  var address = data[0];
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
          map.setCenter(results[0].geometry.location);
          map.fitBounds(results[0].geometry.bounds);
      }
  });
}

google.maps.event.addDomListener(window, 'load', EmbassyMap);