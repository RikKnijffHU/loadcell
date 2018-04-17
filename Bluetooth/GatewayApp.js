var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];

 function start(bleAdress) {
    for (bleAdress in bleAdressList) {
        var bleHandler = getMeasurements(bleAdress);
        this.intervalId = setInterval(function () {

            console.log(bleHandler)
            console.log(bleHandler.characteristic)
            bleHandler.read();
        }, 10000);
    }
}

 function getMeasurements(bleAdress) {
    return  new handler(bleAdress);
}





