from sense_hat import SenseHat
import requests

firebase_url = "https://temp-check-4c71c-default-rtdb.europe-west1.firebasedatabase.app"

def put_temp_data(url):
    req = requests.put("{}/test.json".format(url), data = {'key':'value'})
    print(req)

put_temp_data(firebase_url)

