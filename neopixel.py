import time
from rpi_ws281x import *
import argparse

LED_COUNT      = 150    # Number of LED pixels.
LED_PIN        = 18     # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800    # LED signal frequency in kilohertz (usually 800khz)
LED_DMA        = 10     # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False  # True to invert the signal (when using NPN transistor level shifter)
LED_CHANNEL    = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define function to wipe all leds to off
def colorWipe(strip, color, wait_ms=50):
    """Wipe colors"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(10/1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ*1000, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        while True:
            print ('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)