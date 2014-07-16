var racrControllers = angular.module('racrControllers', []);

racrControllers.controller('TimetableCtrl', ['$scope', '$http', '$rootScope', function($scope, $http, $rootScope) {
    $http.get('/api/1/timetable/').success(function(data) {
        $scope.timetable = data;
    })
    $rootScope.title = "Timetable";
}]);