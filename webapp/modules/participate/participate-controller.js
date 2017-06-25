'use strict';

appModule.controller('participateCtrl', function($scope, $location, NgMap,$http, $mdDialog) {

	NgMap.getMap().then(function(map) {
		$scope.map = map;
	});
	$scope.isOpen = false;

	$scope.shops = [];
	var url = 'http://api.findtorun.fun/get_locations';
	$http({
		method : "GET",
		url : url,
	}).then(function(response) {
	       //$scope.shops = response.data;
	       for(var i=0 ; i<response.data.length; i++){
	       	var obj = {id:'foo'+i, name: 'Khajaguda'+i,'position': response.data[i]};
	       	$scope.shops.push(obj);
	       }
	   }, function(response) {
	   	$scope.msg = response.statusText;
	   });

	
	$scope.showDetail = function(e, shop) {
		$scope.shop = shop;
		$scope.latlng = shop.position;
		$scope.map.showInfoWindow('foo-iw', shop.id);
	};

	$scope.clicked = function() {
		var lattitude = $scope.latlng[0].toFixed(3);
		var longitude = $scope.latlng[1].toFixed(3);
		var url = 'http://api.findtorun.fun/get_users_in_location?lattitude=' + lattitude + '&longitude='+longitude;
		$http({
			method : "GET",
			url : url,
		}).then(function(response) {
			$scope.users = response.data;
		}, function(response) {
			$scope.msg = response.statusText;
		});
		return false;
	};
	$scope.addUserToLocation = function(ev, user) {
		console.log(user);
		$mdDialog.show(
      	$mdDialog.alert()
        .clickOutsideToClose(true)
        .title('Join the run')
        .textContent('You have poked the runner ' + user.first_name + ' ' + user.last_name + 'successfully')
        .ariaLabel('Alert Dialog Demo')
        .ok('Got it!')
        .targetEvent(ev)
    );
	};
});
