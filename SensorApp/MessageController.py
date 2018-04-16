import requests 
API_ENDPOINT = "http://localhost:3000/messages"
 
class MessageController(object):
    """description of class"""
    @staticmethod
    def sendMeasurement(data):
        jsonData = {'ProductName':data.name,
                'Amount': data.amount}
        print("send to api")
        requests.post(url = API_ENDPOINT, data = jsonData)

