var noble = require('noble');   //noble library
var peripheralName = "Thee";     // the local name of the peripheral you want
var targetService = '12ab';         // the service you want
var targetCharacteristic = '000012AB-0000_1000_8000-00805F9B34FB';  // the characteristic you want

var serviceUuids = [targetService];

// allow duplicate peripheral to be returned (default false) on discovery event
var allowDuplicates = false;

noble.startScanning(serviceUuids, allowDuplicates);


noble.on('discover', function (peripheral) {
    peripheral.connect(function (error) {
        console.log('connected to peripheral: ' + peripheral.uuid);
        peripheral.discoverServices([targetCharacteristic], function (error, services) {
            var immediateAlertService = services[0];
            
            console.log(services);
         
            console.log('discovered Immediate Alert service' + immediateAlertService.uuid);

            immediateAlertService.discoverCharacteristics([], function (error, characteristics) {
                var alertLevelCharacteristic = characteristics[0];
                console.log(characteristics);
               
                console.log('discovered Alert Level characteristic');

                // true if for write without response
                //alertLevelCharacteristic.write(new Buffer([0x01]), true, function (error) {
                 //   console.log('set alert level to mid (1)');
               // });
            });
        });
    });
});