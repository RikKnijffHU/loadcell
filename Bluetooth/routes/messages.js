'use strict';
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function (req, res) {
    res.send('respond with a resource');
});

/* POST send message with bluetooth */
router.post('/', function (req, res) {
    console.log(req.body)
});

module.exports = router;
