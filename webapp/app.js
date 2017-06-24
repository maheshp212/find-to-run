'use strict';

var appModule = angular.module('sample-app', [
        'ngRoute',
        'ngMaterial',
        'ngMdIcons'
    ]);

// app.constant('appConst', {
//         PROJECT_MANAGER: 'Project Manager'
//     });

appModule.config(function($routeProvider, $locationProvider, $mdThemingProvider) {
     $mdThemingProvider.enableBrowserColor({
      theme: 'myTheme', // Default is 'default'
      palette: 'accent', // Default is 'primary', any basic material palette and extended palettes are available
      hue: '200' // Default is '800'
    });


    $locationProvider.hashPrefix('');
    $routeProvider
    .when("/", {
        templateUrl : "modules/home/home.html",
        controller: "homeCtrl"
    })
    
});