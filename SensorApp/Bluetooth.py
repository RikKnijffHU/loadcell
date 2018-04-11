import bluetooth
class Bluetooth(object):
    """description of class"""

serverMACAddress = '28:3f:69:10:7c:94'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
sock.close()

