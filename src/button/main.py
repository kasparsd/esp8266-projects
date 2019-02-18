import urequests, usocket
from machine import Pin, Timer

class Toggle:
    def __init__(self, state = False):
        self.state = state
    def get(self):
        return self.state
    def toggle(self):
        self.state = not self.state
        return self.state

url = 'http://10.0.1.11:8123/api/states/binary_sensor.webut'
headers = { 'content-type': 'application/json' }
payload_template = '{ "state": "%s", "attributes": { "friendly_name": "WeBut" } }'

state = Toggle()

def to_state(value):
    return 'on' if value else 'off'

def on_pressed(does):
    print('pressed')
    payload = payload_template % (to_state(state.toggle()))
    resp = urequests.post(url, data=payload, headers=headers)
    print(resp.json())

def debounce(pin):
    timer.init(mode=Timer.ONE_SHOT, period=200, callback=on_pressed)

timer = Timer(0)

button = Pin(0, Pin.IN, Pin.PULL_UP)

button.irq(debounce, Pin.IRQ_RISING)
