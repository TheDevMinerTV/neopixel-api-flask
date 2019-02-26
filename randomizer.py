#!/usr/bin/python2.7

import requests
from random import randint
import time

url = 'http://localhost:5000/api/v1/all/set_by_array'
headers = {'Content-Type': 'application/json'}

while True:
    neopixel_data = []
    for i in range(0, 150):
        payload = {
            'id': i,
            'values': {
                'r': randint(0, 255),
                'g': randint(0, 255),
                'b': randint(0, 255)
            }
        }
        neopixel_data.append(payload)

    requests.post(url, json=neopixel_data) #, headers=headers
#    time.sleep(1)
    time.sleep(0.5)
