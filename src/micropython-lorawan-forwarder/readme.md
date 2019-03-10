# MicroPython LoraWAN Packet Forwarder for ESP8266

Based on the [Adafruit TinyLoRa library](https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa) adjusted to work with native [MicroPython APIs](http://docs.micropython.org/en/latest/library/index.html) running on [Wemos D1 mini](https://wiki.wemos.cc/products:d1:d1_mini) with the [ESP8266 WeMos Shield](https://github.com/hallard/WeMos-Lora).


## Features

- [x] Send packets from the forwarder to TTN or any other LoRaWAN server. Based on the [Adafruit TinyLoRa implementation](https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa) which already can build and encode packets.
- [ ] Relay packets from local LoRa nodes to [TTN](https://www.thethingsnetwork.org/) or any other LoRaWAN server.
- [ ] Relay packets from TTN or any other LoRaWAN server to local LoRa nodes.
