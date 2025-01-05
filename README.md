# Circuitpython OSC Button

A set of buttons... That send OSC messages

## Usage
1. Make `secret.py` as the following:
    ```py
    ssid = "wifi name"
    password = "password"
    ```

2. Change `RECIPIANT_IP`, `RECIPIANT_PORT` and `PINS` from `main.py` to your values.
3. Configure an OSC client to listen to your message, I use [Open Stage Control](https://openstagecontrol.ammd.net/).

## Credits

- [CircuitPython MicroOSC](https://github.com/todbot/CircuitPython_MicroOSC) by [Tod Kurt](https://github.com/todbot)
- [Adafruit Debouncer](https://github.com/adafruit/Adafruit_CircuitPython_Debouncer) by the [Adafruit](https://github.com/adafruit) team

