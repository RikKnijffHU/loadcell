import binascii
import pygatt

YOUR_DEVICE_ADDRESS = "B8:27:EB:9F:D1:2E"
# Many devices, e.g. Fitbit, use random addressing - this is required to
# connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(YOUR_DEVICE_ADDRESS, address_type=ADDRESS_TYPE)

for uuid in device.discover_characteristics().keys():
    print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))

