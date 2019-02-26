#!/usr/bin/python2.7

import time
from neopixel import *
import argparse
import requests

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN      = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

url = 'http://192.168.5.130:5000/api/v1/all/get'

def colorUpdate(strip, r):
    data = r.json()
    for i in data:
	strip.setPixelColor(i['id'], Color(i['values']['r'], i['values']['g'], i['values']['b']))
        strip.show()

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:

        while True:
            r = requests.get(url)
            colorUpdate(strip, r)
#            time.sleep(0.01)

    except KeyboardInterrupt:
       exit()
