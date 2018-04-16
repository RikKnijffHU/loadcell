'use strict';
var express = require('express');
var router = express.Router();
var BluetoothHandler = require('../CentralModule');

/* GET users listing. */
router.get('/', function (req, res) {
    res.send('respond with a resource');
});

/* POST send message with bluetooth */
router.post('/', async function (req, res) {
    console.log(req.body);
    var handler = new BluetoothHandler('12ab');
    handler.sendBleMessage('hoi');
});

module.exports = router;
