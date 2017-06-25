'use strict';

appModule.controller('loginCtrl', function($scope, $location, $rootScope, $http, $window, $mdToast ) {
	$scope.logging = function () {
		$rootScope.lemail = $scope.email;
		var url = 'http://api.findtorun.fun/login?email='+$scope.email;
		$http({
			method : "GET",
			url : url,
		}).then(function(response) {
			$scope.msg = response.data;
			if($scope.msg == 'DoesNotExist') {
				$mdToast.show(
					$mdToast.simple()
					.textContent('User doest exists. Please sign up ')
					.position('bottom right')
					.hideDelay(3000)
					);
				return false;
			}
			$window.location.href = '#/add-location';
		}, function(response) {
			$scope.msg = response.statusText;
		});
	}
});