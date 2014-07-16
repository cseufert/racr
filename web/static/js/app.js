var racrApp = angular.module('racrApp', [
    'ngRoute',
    'racrControllers'
]);

racrApp.config([
    '$routeProvider',
    '$locationProvider',
    function($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $routeProvider
            .when('/results/leaderboard', {
                templateUrl: '/static/html/partials/leaderboard.html',
                controller: 'LeaderboardCtrl',
                name: "leaderboard"
            })
            .when('/results/announce', {
                templateUrl: '/static/html/partials/announce.html',
                controller: 'AnnounceCtrl'
            })
            .when('/results/me', {
                templateUrl: '/static/html/partials/myresults.html',
                controller: 'MyResultsCtrl'
            })
            .when('/event/novelty/record', {
                templateUrl: '/static/html/partials/novelty_event.html',
                controller: 'NoveltyEventCtrl'
            })
            .when('/event/field/record', {
                templateUrl: '/static/html/partials/field_record.html',
                controller: 'FieldEventCtrl'
            })
            .when('/event/track/start', {
                templateUrl: '/static/html/partials/track_start.html',
                controller: 'TrackStartCtrl'
            })
            .when('/event/track/record', {
                templateUrl: '/static/html/partials/track_record.html',
                controller: 'TrackRecordCtrl'
            })
            .when('/timetable', {
                templateUrl: '/static/html/partials/timetable.html',
                controller: 'TimetableCtrl'
            })
            .otherwise({
                redirectTo: '/timetable'
            })
    }
])
