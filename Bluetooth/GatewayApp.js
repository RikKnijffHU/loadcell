var handler = require('./CentralModule');

var bleAdressList = ['B8:27:EB:E4:DA:19'];
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


