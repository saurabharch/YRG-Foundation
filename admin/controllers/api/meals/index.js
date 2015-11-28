/**
 * Created by anchaturvedi on 28/11/15.
 */
'use strict';

var MealsModel = require('../../../models/mongodb/meals.js');

module.exports = function(router) {
    router.get('/', function(req, res) {
        MealsModel.find(function(err, data){
            if(err)
                res.send({"message":"error occurred"});
            else
                res.send(data);
        });
    });
};
