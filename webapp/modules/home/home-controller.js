'use strict';

appModule.controller('homeCtrl', function($scope, $location) {
	$scope.a = AppUtil.gethexa(16);
	$scope.login = function(){
		alert("perla");
	};
});