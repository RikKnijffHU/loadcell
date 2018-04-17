var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];

 function start(bleAdress) {
    for (bleAdress in bleAdressList) {
        
        this.intervalId = setInterval(function () {
            getMeasurements(bleAdress);
        }, 10000);
    }
}

start();

 function getMeasurements(bleAdress) {
    return  new handler(bleAdress);
}





