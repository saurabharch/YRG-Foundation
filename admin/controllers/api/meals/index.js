'use strict';

var MealsModel = require('../../../models').Meals;

module.exports = function(router) {
    router.get('/', function(req, res) {
        MealsModel.find(function(err, data) {
            res.send(err ? {
                'error': 'API Error',
                'message': 'Error occurred'
            } : data);
        });
    });
};
