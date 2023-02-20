import requests
import json

if __name__ == "__main__":

    url = 'http://172.30.254.222:8000/postrequest'
    myobj = {'Hi!!': 'namon'}

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text)
