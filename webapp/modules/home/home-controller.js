'use strict';

appModule.controller('homeCtrl', function($scope, $location, $http, $window, $mdToast) {
	$scope.signups = function () {
     var url = 'http://api.findtorun.fun/signup?email='+$scope.email+'&first_name='+$scope.first_name+'&last_name='+$scope.last_name+'&city='+$scope.city;
/*     var data = {
        "email": $scope.email,
        "first_name": $scope.first_name,
        "last_name": $scope.last_name,
        "city": $scope.city
    };
*/    $http({
     method : "GET",
     url : url,
 }).then(function(response) {
     $scope.msg = response.data;
     $mdToast.show(
        $mdToast.simple()
        .textContent('You are successfully signup. Please login now')
        .position('bottom right')
        .hideDelay(5000)
        );
     $window.location.href = '#/login';
 }, function(response) {
     $scope.msg = response.statusText;
 });
};
});