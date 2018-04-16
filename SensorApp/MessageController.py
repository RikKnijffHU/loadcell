import requests 
API_ENDPOINT = "http://localhost:3000/messages"
 
class MessageController(object):
    """description of class"""
    @staticmethod
    def sendMeasurement(data):
        jsonData = {'ProductName':data.name,
                'Amount': data.amount}
        print("send to api")
        # sending post request and saving response as response object
        r = requests.post(url = API_ENDPOINT, data = jsonData)
 
        # extracting response text 
        pastebin_url = r.text
        print("The pastebin URL is:%s"%pastebin_url)

