'use strict';

var InstitutionModel = require('../../../models').Institutions;

module.exports = function(router) {
    router.get('/', function(req, res) {
        InstitutionModel.find(function(err, data) {
            res.send(err ? {
                'error': 'API Error',
                'message': 'Error occurred'
            } : data);
        });
    });
};
