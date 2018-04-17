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
    var data = JSON.parse(req.body)
    console.log(data);
    db.products.update({ _id: data.name }, { $set: { amount: data.Amount } } ,{ upsert: true });
    res.end("ok");
});

module.exports = router;
