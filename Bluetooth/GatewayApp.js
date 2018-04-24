var handler = require('./BluetoothCentralHandler');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];

 function start() {
    for (bleAdress in bleAdressList) {
        var bleHandler = new handler(bleAdress);
        bleHandler.readPeripheral();
    }
}

start();





