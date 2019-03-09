import ujson, urequests, random, network

# MAC ID.
hwaddr = network.WLAN().config('mac')

hostname = 'router.eu.staging.thethings.network'
port = 1700

STATUS_SIZE = 1024
PROTOCOL_VERSION = 1
PKT_PUSH_DATA = 0

report = bytearray(12)

report[0] = PROTOCOL_VERSION
report[3] = PKT_PUSH_DATA

report[1] = random.getrandbits(8)
report[2] = random.getrandbits(8)

report[4] = hwaddr[0]
report[5] = hwaddr[1]
report[6] = hwaddr[2]
report[7] = 0xff
report[8] = 0xff
report[9] = hwaddr[3]
report[10] = hwaddr[4]
report[11] = hwaddr[5]

payload = {
    "stat": {
        "time": "2014-01-12 08:59:28 GMT",
        "lati": 0.0,
        "long": 0.0,
        "alti": 145,
        "rxnb": 2,
        "rxok": 2,
        "rxfw": 2,
        "ackr": 100.0,
        "dwnb": 2,
        "txnb": 2,
        "pfrm": "Mega Platform",
        "mail": "hi@kaspars.net",
        "desc": "Packet test"
    }
}

json = ujson.dumps(payload)

report.extend(json)

print("Report:", report)
