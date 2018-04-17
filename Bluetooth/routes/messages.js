'use strict';
var express = require('express');
var router = express.Router();
var mongojs = require('mongojs')
var db = mongojs('mongodb://localhost:27017/test', ['products'])

/* GET users listing. */
router.get('/', function (req, res) {
    res.send('respond with a resource');
});

/* POST send message with bluetooth */
router.post('/', async function (req, res) {
    var data = req.body
    console.log(data);
    db.products.update({ _id: data.name }, { $set: { amount: data.amount } }, { upsert: true });
    db.products.find(function (err, docs) {
        // docs is an array of all the documents in mycollection
        console.log(docs);
    });
    res.end("ok");
});

module.exports = router;
