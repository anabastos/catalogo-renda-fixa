'use strict'

let myApp = angular.module('CatalogoApp', [])

myApp.controller('CatalogoCtrl', 
	function($scope, $http) {
		$scope.addRecord = function(){
			$http({
				method: 'POST',
				url: '/insert_record',
				data: {
					form: $scope.form
				}
			}).then(function(response) {
			}, function(error) {
				console.log(error)
			})
		}

		$scope.show_catalogo = function() {
			$http({
				method: 'GET',
				url: '/get_records'
			}).then(function(response) {
				$scope.catalogo = response.data
			}, function(error) {
				console.log(error)
			})
		}

		$scope.show_catalogo()
	}
)
.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//').endSymbol('//')
    })