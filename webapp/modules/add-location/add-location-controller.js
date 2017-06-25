'use strict';

appModule.controller('addLocationCtrl', function($scope, $location, $rootScope, $http, $mdToast, $window) {
	$scope.latlng = [];
	$scope.getpos = function(event){
		$scope.latlng = [event.latLng.lat(), event.latLng.lng()];
	};
	
	$scope.addLocation = function(){
		/*if($scope.latlng.length == 0){
			$err_msg = "Please select a location";
			return true;
		}*/
		var email = $rootScope.lemail;
		var lattitude = $scope.latlng[0].toFixed(3);
		var longitude = $scope.latlng[1].toFixed(3);
		var url = 'http://api.findtorun.fun/update_location?email=' + email + '&lattitude=' + lattitude+ '&longitude=' + longitude;

		$http({
			method : "GET",
			url : url,
		}).then(function(response) {
			$scope.msg = response.data;
			$mdToast.show(
				$mdToast.simple()
				.textContent('Marked Location successfully added!')
				.position('bottom right')
				.hideDelay(3000)
				);
			$window.location.href = '#/participate';
			$scope.latlng = [];
		}, function(response) {
			$scope.msg = response.statusText;
		});
	}
	
});