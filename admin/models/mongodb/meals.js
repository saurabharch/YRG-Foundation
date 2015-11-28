/**
 * Created by anchaturvedi on 28/11/15.
 */

'use strict';
var mongoose = require('mongoose');

function mongo_MealsModel() {
    var schema = mongoose.Schema({
        'id' : Number,
        'name' : String,
        'price' : Number,
        'contents' : [String]
    });

    return mongoose.model('meals', schema);
};

module.exports = mongo_MealsModel();
