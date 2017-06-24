'use strict';

var appModule = angular.module('sample-app', [
        'ngRoute',
        'ngMaterial',
        
    ]);

// app.constant('appConst', {
//         PROJECT_MANAGER: 'Project Manager'
//     });

appModule.config(function($routeProvider, $locationProvider) {

    $locationProvider.hashPrefix('');
    $routeProvider
    .when("/", {
        templateUrl : "modules/home/home.html",
        controller: "homeCtrl"
    })
    
});