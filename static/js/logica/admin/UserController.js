var app = angular.module('app', []);

app.controller('UserController', function($scope) {


    $scope.msg = "flabio";
    console.log($scope.msg);
});