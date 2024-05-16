from sense_hat import SenseHat
import requests
from datetime import datetime
import json

firebase_url = "https://temp-check-4c71c-default-rtdb.europe-west1.firebasedatabase.app"

def get_temperature():
    sense = SenseHat()
    sense.clear()
    return sense.get_temperature()


def put_temperature_data(base_url):
    timestamp = datetime.now()

    url ="{}/{}/{}/{}/{}/{}.json".format(base_url, timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute)

    temperature_data = {}
    temperature_data["temperature"] = get_temperature()
    
    res = requests.put(url, json=temperature_data)
    
    print(url)
    print(res.json())

put_temperature_data(firebase_url)

