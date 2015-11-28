'use strict';

var AddonsModel = require('../../../models').Addons;

module.exports = function(router) {
    router.get('/', function(req, res) {
        AddonsModel.find(function(err, data) {
            res.send(err ? {
                'error': 'API Error',
                'message': 'Error occurred'
            } : data);
        });
    });
};
