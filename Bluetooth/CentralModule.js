var noble = require('noble');   //noble library
var peripheralName = "Thee";     // the local name of the peripheral you want
var targetService = '12ab';         // the service you want
var targetCharacteristic = '000012AB-0000-1000-8000-00805F9B34FB';  // the characteristic you want

var serviceUuids = [targetService];
// allow duplicate peripheral to be returned (default false) on discovery event
var allowDuplicates = false;
class BluetoothHandler {

    constructor(peripheral) {
        var characteristic = null;
        noble.startScanning(serviceUuids, allowDuplicates);


        noble.on('discover', function (peripheral) {
            peripheral.connect(function (error) {

                peripheral.discoverServices(['12ab'], function (error, services) {
                    var service = services[0];


                    service.discoverCharacteristics(null, function (error, characteristics) {
                        characteristic = characteristics[0]
                    });
                });
            });
        });
    }

    sendBleMessage(data) {
        console.log('gelukt')
        this.
        this.characteristic.write(new Buffer(data), true, function (error) {
            console.log('send');
        });
    }
}
module.exports = BluetoothHandler;
