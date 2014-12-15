var barBuilder = angular.module("barBuilder", []);

barBuilder.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


barBuilder.controller("MainCtrl", function($scope, $compile, $rootScope) {

    $scope.colorChoices = [
        {
            "background": "#e74c3c",
            "icon" : "#ffffff",
            "text" : "#ecf0f1",
            "buttonBackground" : "#34495e",
            "buttonText" : "#ecf0f1",
            "iconBackground": "#34495e",
        },
        {
            "background": "#1abc9c",
            "icon" : "#ffffff",
            "text" : "#ffffff",
            "buttonBackground" : "#2980b9",
            "buttonText" : "#ffffff",
            "iconBackground": "#34495e",
        },
        {
            "background": "#DF5473",
            "icon" : "#ffffff",
            "text" : "#ffffff",
            "buttonBackground" : "#593C7C",
            "buttonText" : "#ffffff",
            "iconBackground": "#34495e",
        },
        {
            "background": "#070336",
            "icon" : "#ffffff",
            "text" : "#43C6BE",
            "buttonBackground" : "#165F8A",
            "buttonText" : "#ffffff",
            "iconBackground": "#34495e",
        },
        {
            "background": "#9FD96C",
            "icon" : "#ffffff",
            "text" : "#095069",
            "buttonBackground" : "#059b9b",
            "buttonText" : "#ffffff",
            "iconBackground": "#34495e",
        },
        {
            "background": "#ff4900",
            "icon" : "#ffffff",
            "text" : "#fdfdfd",
            "buttonBackground" : "#00AF64",
            "buttonText" : "#fdfdfd",
            "iconBackground": "#34495e",
        },
        {
            "background": "#FFAA00",
            "icon" : "#ffffff",
            "text" : "#120873",
            "buttonBackground" : "#235D79",
            "buttonText" : "#fdfdfd",
            "iconBackground": "#34495e",
        },


    ];

    $scope.iconChoices = [
        staticUrl + "img/icons/Arrowhead-Right-01-128.png",
        staticUrl + "img/icons/Arrowhead-Right-128.png",
        staticUrl + "img/icons/Basket-128.png",
        staticUrl + "img/icons/Beverage-Beer-02-128.png",
        staticUrl + "img/icons/Beverage-Cocktail-01-128.png",
        staticUrl + "img/icons/Beverage-Coffee-02-128.png",
        staticUrl + "img/icons/Branch-Engineering-128.png",
        staticUrl + "img/icons/Cheese-01-128.png",
        staticUrl + "img/icons/Cup-128.png",
        staticUrl + "img/icons/Customize-02-128.png",
        staticUrl + "img/icons/Dollar-128.png",
        staticUrl + "img/icons/Euro-128.png",
        staticUrl + "img/icons/Facebook-128.png",
        staticUrl + "img/icons/Graduate-Hat-128.png",
        staticUrl + "img/icons/Hand-03-128.png",
        staticUrl + "img/icons/Message-Mail-128.png",
        staticUrl + "img/icons/Mug-128.png",
        staticUrl + "img/icons/Pizza-01-128.png",
        staticUrl + "img/icons/Robot-01-128.png",
        staticUrl + "img/icons/Shape-Star2-128.png",
        staticUrl + "img/icons/Shape70-128.png",
        staticUrl + "img/icons/Spaceship-01-128.png",
        staticUrl + "img/icons/Wine-Glass-02-128.png",
        staticUrl + "img/icons/Wine-Glass-03-128.png",
        staticUrl + "img/icons/Yoga-08-128.png",
        staticUrl + "img/icons/Yoga-04-128.png",
        staticUrl + "img/icons/Yin-Yang-128.png",
        staticUrl + "img/icons/Tree-128.png",
        staticUrl + "img/icons/Toolbox-01-128.png",
        staticUrl + "img/icons/Thumbs-Up-128.png",
        staticUrl + "img/icons/Saloon-128.png",
        staticUrl + "img/icons/Ship-128.png",
        staticUrl + "img/icons/Pirate-01-128.png",
        staticUrl + "img/icons/Paper-Plane-128.png",
        staticUrl + "img/icons/Paint-Brush-03-128.png",
        staticUrl + "img/icons/Palm Tree-128.png",
        staticUrl + "img/icons/Magnet-128.png",
        staticUrl + "img/icons/House-128.png",
        staticUrl + "img/icons/Hat-05-128.png",
        staticUrl + "img/icons/Hanger-128.png",
        staticUrl + "img/icons/Hammer-128.png",
        staticUrl + "img/icons/Guitar-128.png",
        staticUrl + "img/icons/Gift-128.png",
        staticUrl + "img/icons/Genie-Lamp-128.png",
        staticUrl + "img/icons/Flower-128.png",
        staticUrl + "img/icons/Foot Print-128.png",
        staticUrl + "img/icons/Electric-Guitar-01-128.png",
        staticUrl + "img/icons/Drama-128.png",
        staticUrl + "img/icons/Dice-128.png",
        staticUrl + "img/icons/Danger-128.png",
        staticUrl + "img/icons/Crown-King-128.png",
        staticUrl + "img/icons/Color-128.png",
        staticUrl + "img/icons/Bowl-128.png",
        staticUrl + "img/icons/Box -128.png",
        staticUrl + "img/icons/Beamed-Notes-128.png",
        staticUrl + "img/icons/Bell-128.png",
    ];

    $scope.colors = initialColors;
    $scope.content = initialContent;
    // $scope.colors = $scope.colorChoices[0];
    // $scope.content = {
    //     "messageText": "This is the sample text that we're defaulting in",
    //     "buttonText": "Buy Now",
    //     "buttonLink": "http://www.WiggleBar.com",
    //     "iconUrl": $scope.iconChoices[0]
    // }
    $scope.targetColor = '#ebebeb'; //What is this?

    //This stuff really should be refactored out into directives

    if (typeof expandEmbed != "undefined" && expandEmbed === true) {
        $scope.showEdit = false;
        $scope.showEmbed = true;
    } else {
        $scope.showEdit = true;
        $scope.showEmbed = false;
    }

    $scope.toggleBuilder = function () {
        $scope.showEdit = !$scope.showEdit;
        $scope.showEmbed = !$scope.showEmbed;
    };

    $scope.showBar = function () {
        nb.init(0);
        bar = $("#nb-notification-bar");
        $compile(bar)($scope);
    };
});

barBuilder.helpers = {};

barBuilder.helpers.clone = function (obj) {
    var result = {};
    for (var key in obj) {
        result[key] = obj[key];
    }
    return result;
};

barBuilder.helpers.elementMatchesAnyInArray = function(element, elementArray) {
    for (var i=0; i < elementArray.length; i++) {
        if (element == elementArray[i]) {
            return true;
        }
    }
    return false;
}



barBuilder.directive('uiColorpicker', function() {
    return {
        restrict: 'E',
        require: 'ngModel',
        scope: false,
        replace: true,
        template: "<span><input class='input-small' /></span>",
        link: function(scope, element, attrs, ngModel) {
            var input = element.find('input');
            var options = angular.extend({
                showInput: true,
                showButtons: false,
                color: ngModel.$viewValue,
                change: function(color) {
                    scope.$apply(function() {
                      ngModel.$setViewValue(color.toHexString());
                    });
                },
                move: function(color) {
                    scope.$apply(function() {
                      ngModel.$setViewValue(color.toHexString());
                    });
                },

            }, scope.$eval(attrs.options));

            ngModel.$render = function() {
              input.spectrum('set', ngModel.$viewValue || '');
            };

            input.spectrum(options);
        }
    };
});


barBuilder.directive("iconPicker", ["$document","$compile",function($document, $compile) {
    return {
        restrict: "E",
        scope: {
            choices: '=',
            choice: '=',
            colors: '=',
        },
        templateUrl: siteUrl + "notifybar/directives/icon-picker.html",
        link: function (scope, element, $compile) {
           //  //console.log(element("#id_icon_upload"));
           angular.element("#hidden_input").remove();
           //  //upload_input.contents();

           //  var upload_input = angular.element("<tag></tag>");
           // // console.log($("#id_icon_upload"));
           //  //element.append(upload_input);
           //  element.html('<a href="#">a</a>');
           //  $compile(element.contents())(scope)//(scope);

            scope.pickerVisible = false;
            scope.uploadVisible = false;

            scope.toggleUpload = function (){
                console.log("working");
                scope.uploadVisible = !scope.uploadVisible;

            }

            scope.togglePicker = function (item) {
                scope.pickerVisible = !scope.pickerVisible;
            }

            scope.chooseIcon = function (item) {
                scope.choice = item;
            }

            $document.bind('click', function(){
                if (barBuilder.helpers.elementMatchesAnyInArray(event.target, element.find(event.target.tagName))) {
                    return;
                }

                scope.pickerVisible = false;
                scope.$apply();
            });
        }
    }
}]);




barBuilder.directive("palettePicker", ["$document", function ($document) {
    return {
        restrict: "E",
        scope: {
            choices: '=',
            choice: '='
        },
        templateUrl: siteUrl + "notifybar/directives/palette-picker.html",
        link: function (scope, element) {
            scope.pickerVisible = false;


            scope.togglePicker = function () {
                scope.pickerVisible = !scope.pickerVisible;
            };

            scope.choosePalette = function (item) {
                scope.choice = barBuilder.helpers.clone(item);
            };

            $document.bind('click', function(){
                if (barBuilder.helpers.elementMatchesAnyInArray(event.target, element.find(event.target.tagName))) {
                    return;
                }

                scope.pickerVisible = false;
                scope.$apply();
            });
        }
    }
}]);


