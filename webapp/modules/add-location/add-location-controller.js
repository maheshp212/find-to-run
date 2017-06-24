'use strict';

appModule.controller('addLocationCtrl', function($scope, $location, NgMap) {
	$scope.latlng = [-25.363882,131.044922];
	$scope.getpos = function(event){
		$scope.latlng = [event.latLng.lat(), event.latLng.lng()];
	};


	
});