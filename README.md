# neopixel-api-flask

This repository contains a api for neopixels to be controlled over http!

## Setup

1. Install these dependencies on your raspberry pi:

    ```bash
    sudo apt-get install gcc make build-essential python-dev git scons swig
    echo "blacklist snd_bcm2835" | sudo tee /etc/snd-blacklist.conf
    sed -i "s/dtparam=audio=on/#dtparam=audio=on/g"
    sudo reboot
    ```

2. Clone the rpi_ws281x neopixel library to your raspberry pi, install it and reboot.

    ```bash
    git clone https://github.com/jgarff/rpi_ws281x
    cd rpi_ws281x
    sudo scons
    cd python
    sudo python setup.py build
    sudo python setup.py install
    sudo reboot
    ```

3. Then, clone my repository to your pi and maybe to another computer, preferably running GNU / Linux.

    ```bash
    git clone https://github.com/TheDevMinerTV/neopixel-api-flask.git
    cd neopixel-api-flask
    ```

4. Configure the python scripts
    * In server.py
        * LED_COUNT => How many NeoPixels are on your led strip

          Example:

          LED_COUNT = 30
    * In controller.py
        * URL => URL or IP of the computer or pi running server.py (can also be localhost)

          Example:

          URL = "localhost"
        * LED_COUNT => Number of LED pixels
        * LED_PIN => GPIO pin connected to the pixels (18 uses PWM!).
        * LED_FREQ_HZ => LED signal frequency in kilohertz (usually 800khz)
        * LED_DMA => DMA channel to use for generating signal
        * LED_BRIGHTNESS => Brightness
        * LED_INVERT => True to invert the signal (when using a NPN transistor level shifter)
        * LED_CHANNEL => set to '1' for GPIOs 13, 19, 41, 45 or 53

    * In randomizer.py
        * URL => URL or IP of the computer or pi running server.py (can also be localhost)

          Example:

          URL = "localhost"

5. Build the documentation (OPTIONAL)

    ```bash
    ./buildAPIDocs.sh
    ```

6. Start the server!

    ```bash
    ./server.py
    ```

7. Start the controller on the pi!

    ```bash
    sudo ./controller.py
    ```

8. Start the randomizer! (OPTIONAL)

    ```bash
    sudo ./randomizer.py
    ```

9. Develop! (REQUIRED)    :joy:
