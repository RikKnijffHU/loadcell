var bleno = require('bleno');
var mongojs = require('mongojs')
var db = mongojs('mongodb://localhost:27017', ['products'])

class BluetoothPeripheralHandler {

    constructor() {

        // Once bleno starts, begin advertising our BLE address
        bleno.on('stateChange', function (state) {
            console.log('State change: ' + state);
            if (state === 'poweredOn') {
                bleno.startAdvertising('MyDevice', ['12ab']);
            } else {
                bleno.stopAdvertising();
            }
        });

        // Notify the console that we've accepted a connection
        bleno.on('accept', function (clientAddress) {
            console.log("Accepted connection from address: " + clientAddress);
        });

        // Notify the console that we have disconnected from a client
        bleno.on('disconnect', function (clientAddress) {
            console.log("Disconnected from address: " + clientAddress);
        });

        // When we begin advertising, create a new service and characteristic
        bleno.on('advertisingStart', function (error) {
            if (error) {
                console.log("Advertising start error:" + error);
            } else {
                console.log("Advertising start success");
                bleno.setServices([

                    // Define a new service
                    new bleno.PrimaryService({
                        uuid: '12ab',
                        characteristics: [

                            // Define a new characteristic within that service
                            new bleno.Characteristic({
                                value: null,
                                uuid: '34cd',
                                properties: ['read'],
                               
                                onReadRequest: function (offset, callback) {
                                    console.log("Read request received");
                                    var data = JSON.stringify(db.products.find());
                                    console.log(data);
                                    console.log(this.RESULT_SUCCESS);
                                    callback(this.RESULT_SUCCESS, new Buffer(data));
                                }

                            })

                        ]
                    })
                ]);
            }
        });
    }
}
module.exports = BluetoothPeripheralHandler;