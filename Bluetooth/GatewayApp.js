﻿var handler = require('./CentralModule');

var bleAdressList = ['b8:27:eb:e4:da:19'];
var handlerList = [];
for (bleAdress in bleAdressList) {
    bleHandler = new handler(bleAdress);
    
    setTimeout(handlerList.push(bleHandler), 10000); 
}


    this.intervalId = setInterval(function () {
        for (bleHandler in handlerList) {
            console.log(bleHandler)
            console.log(bleHandler.characteristic)
            bleHandler.read();
        }
    }, 10000);






