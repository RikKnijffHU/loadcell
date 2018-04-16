var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];
for (bleAdress in bleAdressList) {
    bleHandler = new handler(bleAdress);
    handlerList.push(bleHandler);
}

setTimeout(getMeasurements, 30000);

function getMeasurements() {
    this.intervalId = setInterval(function () {
        for (bleHandler in handlerList) {
            bleHandler.read();
        }
    }, 10000);
}





