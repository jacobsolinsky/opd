    google.maps.event.addDomListener(window, 'load', init);
    var map;
    function init() {
        var mapOptions = {
            center: new google.maps.LatLng(44.939844,-93.187591),
            zoom: 11,
            zoomControl: true,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.DEFAULT,
            },
            disableDoubleClickZoom: true,
            mapTypeControl: true,
            mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            },
            scaleControl: true,
            scrollwheel: true,
            panControl: true,
            streetViewControl: true,
            draggable : true,
            overviewMapControl: true,
            overviewMapControlOptions: {
                opened: false,
            },
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            styles: [{"stylers": [{"hue": "#ff1a00"},{"invert_lightness": true},{"saturation": -100},{"lightness": 33},{"gamma": 0.5}]},{"featureType": "road.highway","elementType": "labels.icon","stylers": [{"visibility": "simplified"},{"weight": "3.01"},{"gamma": "1.15"},{"invert_lightness": false},{"lightness": "-82"},{"saturation": "-12"},{"hue": "#ff0000"}]},{"featureType": "water","elementType": "geometry","stylers": [{"color": "#2D333C"}]}]
			,
        }
        var mapElement = document.getElementById('deliverymap');
        var map = new google.maps.Map(mapElement, mapOptions);
        
	var input = /** @type {HTMLInputElement} */(
    document.getElementById('pac-input'));

    var types = document.getElementById('type-selector');
    	map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    	map.controls[google.maps.ControlPosition.TOP_LEFT].push(types);

    var autocomplete = new google.maps.places.Autocomplete(input);
    	autocomplete.bindTo('bounds', map);

    var infowindow = new google.maps.InfoWindow();
    var marker = new google.maps.Marker({
    	map: map,
    	anchorPoint: new google.maps.Point(0, -29)
    });

    google.maps.event.addListener(autocomplete, 'place_changed', function(m) {
    infowindow.close();
    marker.setVisible(false);
    var place = autocomplete.getPlace();
    if (!place.geometry) {
    	return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
    	map.fitBounds(place.geometry.viewport);
    } else {
    	map.setCenter(place.geometry.location);
    	map.setZoom(12);  // Why 12? Because it doesn't zoom in too far.
    }
    marker.setIcon(/** @type {google.maps.Icon} */({
    	url: 'https://www.google.com/mapfiles/arrow.png',
    	size: new google.maps.Size(71, 71),
    	origin: new google.maps.Point(0, 0),
    	anchor: new google.maps.Point(11, 30),
    	scaledSize: new google.maps.Size(40, 35) // 39x34 ratio
    }));
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);
    if(google.maps.geometry.poly.containsLocation(marker.getPosition(), deliveryArea) == true) {
    var address = '';
    if (place.address_components) {
      address = [
    	(place.address_components[0] && place.address_components[0].short_name || ''),
    	(place.address_components[1] && place.address_components[1].short_name || ''),
    	(place.address_components[2] && place.address_components[2].short_name || '')
      ].join(' ');
    }
// https://davannis.alohaorderonline.com/StartOrder.aspx?SelectOrderMode=Delivery&SelectSite=1
    infowindow.setContent('<div>Awesome! <span style="font-weight: bold; color: #008800; font-style: italic;">' + address + '</span> is in our delivery area.<br>Would you like to <span style="font-weight: bold;">Order Online</span> for <a href="https://clevelandandgrand.davannis.com/" target="_blank">Delivery or Pickup</a>?');
    infowindow.open(map, marker);
    } else {
    var address = '';
    if (place.address_components) {
      address = [
    	(place.address_components[0] && place.address_components[0].short_name || ''),
    	(place.address_components[1] && place.address_components[1].short_name || ''),
    	(place.address_components[2] && place.address_components[2].short_name || '')
      ].join(' ');
    }
    infowindow.setContent('<div>Sorry, <span style="font-weight: bold; color: #008800; font-style: italic;">' + address + '</span> is out of our delivery area.<br>Would you like to <span style="font-weight: bold;">Order Online</span> for <a href="https://clevelandandgrand.davannis.com/" target="_blank">Pickup</a>?');
    infowindow.open(map, marker);
    }



    });

    // Sets a listener on a radio button to change the filter type on Places
    // Autocomplete.
    function setupClickListener(id, types) {
    	var radioButton = document.getElementById(id);
    	google.maps.event.addDomListener(radioButton, 'click', function() {
    	  autocomplete.setTypes(types);
    	});
    }

		
		
		var locations = [
['We are here!', 'undefined', 'undefined', 'undefined', 'undefined', 44.939844,-93.187591, '/wp-content/themes/davannis/images/pizza-map-pin.png']
        ];
        for (i = 0; i < locations.length; i++) {
			if (locations[i][1] =='undefined'){ description ='';} else { description = locations[i][1];}
			if (locations[i][2] =='undefined'){ telephone ='';} else { telephone = locations[i][2];}
			if (locations[i][3] =='undefined'){ email ='';} else { email = locations[i][3];}
           if (locations[i][4] =='undefined'){ web ='';} else { web = locations[i][4];}
           if (locations[i][7] =='undefined'){ markericon ='';} else { markericon = locations[i][7];}
            shopmarker = new google.maps.Marker({
                icon: markericon,
                position: new google.maps.LatLng(locations[i][5], locations[i][6]),
                map: map,
                title: locations[i][0],
                desc: description,
                tel: telephone,
                email: email,
                web: web
            });
link = ''; 
//            bindInfoWindow(shopmarker, map, locations[i][0], description, telephone, email, web, link);
            bindInfoWindow(shopmarker, map, locations[i][0]);
    var coords = [
new google.maps.LatLng(44.949929,-93.202793),
new google.maps.LatLng(44.956026,-93.212326),
new google.maps.LatLng(44.957608,-93.210100),
new google.maps.LatLng(44.959750,-93.206344),
new google.maps.LatLng(44.959802,-93.201828),
new google.maps.LatLng(44.974134,-93.202407),
new google.maps.LatLng(44.971903,-93.194189),
new google.maps.LatLng(44.969140,-93.187451),
new google.maps.LatLng(44.969110,-93.182344),
new google.maps.LatLng(44.969201,-93.173161),
new google.maps.LatLng(44.969565,-93.167539),
new google.maps.LatLng(44.969504,-93.165092),
new google.maps.LatLng(44.969110,-93.163054),
new google.maps.LatLng(44.968897,-93.160479),
new google.maps.LatLng(44.968123,-93.157067),
new google.maps.LatLng(44.968563,-93.157110),
new google.maps.LatLng(44.968487,-93.156552),
new google.maps.LatLng(44.968016,-93.156445),
new google.maps.LatLng(44.968108,-93.152990),
new google.maps.LatLng(44.966726,-93.149085),
new google.maps.LatLng(44.966620,-93.146253),
new google.maps.LatLng(44.941542,-93.146553),
new google.maps.LatLng(44.941534,-93.136339),
new google.maps.LatLng(44.934042,-93.136348),
new google.maps.LatLng(44.934013,-93.137230),
new google.maps.LatLng(44.932046,-93.137469),
new google.maps.LatLng(44.931672,-93.142433),
new google.maps.LatLng(44.932766,-93.143184),
new google.maps.LatLng(44.932929,-93.146585),
new google.maps.LatLng(44.925968,-93.146641),
new google.maps.LatLng(44.926019,-93.148407),
new google.maps.LatLng(44.925729,-93.148489),
new google.maps.LatLng(44.925311,-93.147937),
new google.maps.LatLng(44.924125,-93.147315),
new google.maps.LatLng(44.920453,-93.147379),
new google.maps.LatLng(44.919416,-93.148441),
new google.maps.LatLng(44.914155,-93.150201),
new google.maps.LatLng(44.909691,-93.153934),
new google.maps.LatLng(44.907091,-93.160286),
new google.maps.LatLng(44.905439,-93.165061),
new google.maps.LatLng(44.905192,-93.168489),
new google.maps.LatLng(44.905678,-93.171664),
new google.maps.LatLng(44.900906,-93.172088),
new google.maps.LatLng(44.900724,-93.172785),
new google.maps.LatLng(44.900731,-93.174604),
new google.maps.LatLng(44.899877,-93.174601),
new google.maps.LatLng(44.899811,-93.176988),
new google.maps.LatLng(44.898560,-93.177164),
new google.maps.LatLng(44.898292,-93.177667),
new google.maps.LatLng(44.894157,-93.181744),
new google.maps.LatLng(44.894796,-93.187923),
new google.maps.LatLng(44.898565,-93.191357),
new google.maps.LatLng(44.904037,-93.191872),
new google.maps.LatLng(44.909751,-93.200455),
new google.maps.LatLng(44.916802,-93.201828),
new google.maps.LatLng(44.927666,-93.200277),
new google.maps.LatLng(44.939343,-93.200610)
    ];
    // Construct the polygon
    deliveryArea = new google.maps.Polygon({
        paths: coords,
        clickable: false,
        draggable: false,
        editable: false,
        strokeOpacity: 0.8,
        strokeWeight: 2,
        strokeColor: '#CC0000',
        fillColor: '#CC0000',
        fillOpacity: 0.35
    });

    deliveryArea.setMap(map);

var myControl = document.getElementById('myTextDiv');
map.controls[google.maps.ControlPosition.TOP_LEFT].push(myControl);

     }
 function bindInfoWindow(shopmarker, map, title, desc, telephone, email, web, link) {
      var infoWindowVisible = (function () {
              var currentlyVisible = false;
              return function (visible) {
                  if (visible !== undefined) {
                      currentlyVisible = visible;
                  }
                  return currentlyVisible;
               };
           }());
           iw = new google.maps.InfoWindow();
           google.maps.event.addListener(shopmarker, 'click', function() {
               if (infoWindowVisible()) {
                   iw.close();
                   infoWindowVisible(false);
               } else {
                   var html= "<div class='gm-style-iw-pin'><p>"+title+"</p></div>";
                   iw = new google.maps.InfoWindow({content:html});
                   iw.open(map,shopmarker);
                   infoWindowVisible(true);
               }
        });
        google.maps.event.addListener(iw, 'closeclick', function () {
            infoWindowVisible(false);
        });
 }
}
