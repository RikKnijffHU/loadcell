'use strict';
var express = require('express');
var router = express.Router();
var BluetoothHandler = require('../CentralModule');
var handler = new BluetoothHandler('12ab');

/* GET users listing. */
router.get('/', function (req, res) {
    res.send('respond with a resource');
});

/* POST send message with bluetooth */
router.post('/', async function (req, res) {
    var data = JSON.stringify(req.body)
    console.log(data);
    handler.sendBleMessage(data)
    res.end("ok")
});

module.exports = router;
