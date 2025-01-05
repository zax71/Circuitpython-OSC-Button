import time, board, digitalio, wifi, socketpool, microosc, secret
from adafruit_debouncer import Debouncer

RECIPIANT_IP = "192.168.0.8"
RECIPIANT_PORT = 8080
ssid = secret.ssid
password = secret.password

print("connecting to WiFi", ssid)
wifi.radio.connect(ssid, password)
print("my ip address:", wifi.radio.ipv4_address)


socket_pool = socketpool.SocketPool(wifi.radio)


osc_client = microosc.OSCClient(socket_pool, RECIPIANT_IP, RECIPIANT_PORT)

msg = microosc.OscMsg( "/button/buzzer", [-1], ("i") )  # fmt: skip


pins = [board.GP15, board.GP14, board.GP13, board.GP12]
switches = []
for pin in pins:
    button = digitalio.DigitalInOut(pin)
    button.switch_to_input(pull=digitalio.Pull.DOWN)
    switches.append(Debouncer(button))

while True:
    for id, switch in enumerate(switches):
        switch.update()
        if switch.rose:
            msg.args[0] = id + 1
            osc_client.send(msg)
            print(f"sent: {msg}")
