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
    .when("/login", {
        templateUrl : "modules/login/login.html",
        controller: "loginCtrl"
    })
    .when("/add-location", {
        templateUrl : "modules/add-location/add-location.html",
        controller: "addLocationCtrl"
    })
    .when("/participate", {
        templateUrl : "modules/participate/participate.html",
        controller: "participateCtrl"
    })
    
});