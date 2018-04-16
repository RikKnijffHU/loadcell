var handler = require('./CentralModule');

var bleAdressList = ['B8:27:EB:9F:D1:2E'];
var handlerList = [];
for (bleAdress in bleAdressList) {
    bleHandler = new handler(bleAdress);
    handlerList.push(bleHandler);
}
this.intervalId = setInterval(function () {
    for (bleHandler in handlerList) {
        bleHandler.read();
    }
}, 10000);


