import bluetooth
class Bluetooth(object):
    """description of class"""

serverMACAddress = 'B8:27:EB:E4:DA:19'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while True:
    text = 'hoi' # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
sock.close()

