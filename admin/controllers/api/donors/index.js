'use strict';

var DonorModel = require('../../../models').Donor;

module.exports = function(router) {
    router.get('/', function(req, res) {
        DonorModel.find(function(err, data) {
            res.send(err ? {
                'error': 'API Error',
                'message': 'Error occurred'
            } : data);
        });
    });
};
