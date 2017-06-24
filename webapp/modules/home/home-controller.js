'use strict';

appModule.controller('homeCtrl', function($scope, $location, $http) {
	$scope.logging = function () {
    	var url = 'http://api.findtorun.fun/signup';
      	var data = {
		    "email": $scope.email,
		    "first_name": $scope.first_name,
		    "last_name": $scope.last_name,
		    "city": $scope.city
		};

       	$http({
           method : "GET",
           url : url,
           data: data
       }).then(function(response) {
           $scope.msg = response.data;
       }, function(response) {
           $scope.msg = response.statusText;
       });
  	}
});