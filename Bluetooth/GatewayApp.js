var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];
for (bleAdress in bleAdressList) {
    bleHandler = new handler(bleAdress);
    
    handlerList.push(bleHandler.setup());
}

setTimeout(getMeasurements, 30000);

function getMeasurements() {
    this.intervalId = setInterval(function () {
        for (characteristic in handlerList) {
            console.log(bleHandler)
            console.log(characteristic)
            bleHandler.read();
        }
    }, 10000);
}





