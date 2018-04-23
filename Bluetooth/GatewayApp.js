var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];

function start() {
    new handler(bleAdressList[0]);
}

start();







