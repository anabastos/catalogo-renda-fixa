
(function () {

  'use strict';

  angular.module('CatalogoApp', [])

  .controller('CatalogoCtrl', ['$scope', '$log',
    function($scope, $log) {
    $scope.getNewPerson = function() {
      $log.log("test");
    };
  }

  ]);

}());