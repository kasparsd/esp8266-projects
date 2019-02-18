import time, urequests
from sht30 import SHT30

sensor = SHT30()

url = 'http://10.0.1.11:8123/api/states/sensor.WE_TEMP'
headers = { 'content-type': 'application/json' }
payload_template = '{ "state": "%f", "attributes": { "friendly_name": "We Temp", "unit_of_measurement": "C" } }'

def send_temp():
    temperature, humidity = sensor.measure()
    payload = payload_template % (temperature)
    resp = urequests.post(url, data=payload, headers=headers)
    print(resp.json())

while True:
    send_temp()
    time.sleep(60)
