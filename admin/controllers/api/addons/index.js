/**
 * Created by anchaturvedi on 28/11/15.
 */


'use strict';

var AddonsModel = require('../../../models/mongodb/addons.js');

module.exports = function(router) {
    router.get('/', function(req, res) {
        AddonsModel.find(function(err, data){
            if(err)
                res.send({"message":"error occurred"});
            else
                res.send(data);
        });
    });
};
