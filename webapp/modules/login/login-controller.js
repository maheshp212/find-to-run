'use strict';

appModule.controller('loginCtrl', function($scope, $location, $rootScope, $http, $window) {
	$scope.logging = function () {
		$rootScope.lemail = $scope.email;
		var url = 'http://api.findtorun.fun/login?email='+$scope.email;
		$http({
	       method : "GET",
	       url : url,
	   }).then(function(response) {
	       $scope.msg = response.data;
	   	 	$window.location.href = '#/add-location';
	   }, function(response) {
	       $scope.msg = response.statusText;
	   });
	}
});