var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];

async function start(bleAdress) {
    for (bleAdress in bleAdressList) {
        var bleHandler = await getMeasurements(bleAdress)

        handlerList.push(bleHandler)
    }
}

async function getMeasurements(bleAdress) {
    return await new handler(bleAdress);
    
}
start().then(() => {
    this.intervalId = setInterval(function () {
        for (bleHandler in handlerList) {
            console.log(bleHandler)
            console.log(bleHandler.characteristic)
            bleHandler.read();
        }
    }, 10000);
}
)





