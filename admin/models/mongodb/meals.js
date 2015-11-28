'use strict';

var mongoose = require('mongoose');

var meals = function() {
    var schema = mongoose.Schema({
        'id': Number,
        'name': String,
        'price': Number,
        'contents': [String]
    });
    return mongoose.model('meals', schema);
};

module.exports = meals();
