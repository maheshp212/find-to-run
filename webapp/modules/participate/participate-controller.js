'use strict';

appModule.controller('participateCtrl', function($scope, $location, NgMap) {
	$scope.a = AppUtil.gethexa(16);

	NgMap.getMap().then(function(map) {
		console.log('map', map);
		$scope.map = map;
	});
	$scope.latlng = [-25.363882,131.044922];

	$scope.clicked = function() {
		alert('Clicked a link inside infoWindow');
	};
	$scope.shops = [
	{id:'foo', name: 'Khajaguda', position:[17.415,78.345]},
	{id:'bar', name: 'TCS', position:[17.419,78.343]}
	];
	$scope.shop = $scope.shops[0];

	$scope.showDetail = function(e, shop) {
		$scope.shop = shop;
		$scope.map.showInfoWindow('foo-iw', shop.id);
	};

/*	$scope.hideDetail = function() {
		$scope.map.hideInfoWindow('foo-iw');
	};
*/
});
