var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];
for (bleAdress in bleAdressList) {
    bleHandler = new handler(bleAdress);
    
    handlerList.push({ handler: bleHandler, char: bleHandler.setup() });
}

setTimeout(getMeasurements, 30000);

function getMeasurements() {
    this.intervalId = setInterval(function () {
        for (ble in handlerList) {
            console.log(ble.handler)
            console.log(ble.characteristic)
            ble.handler.read(ble.characteristic);
        }
    }, 10000);
}





