/**
 * Created by anchaturvedi on 28/11/15.
 */
'use strict';
var mongoose = require('mongoose');

function mongo_AddonsModel() {
    var schema = mongoose.Schema({
        'id' : Number,
        'name' : String,
        'price' : Number
    });

    return mongoose.model('addons', schema);
};

module.exports = mongo_AddonsModel();
