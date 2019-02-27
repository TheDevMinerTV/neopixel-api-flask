#!/usr/bin/python2.7

import requests
from random import randint
import time

URL = 'localhost'


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

    requests.post('http://' + URL + ':8088/api/v1/all/set_by_array', json=neopixel_data) #, headers=headers
    time.sleep(0.5)
