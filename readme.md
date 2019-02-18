# ESP8266/Wemos Projects

This is a repository containing all my [Wemos D1 mini](https://wiki.wemos.cc/products:d1:d1_mini) projects.

- [Binary button for Home Assistant](src/button)


## Upload Project

Use the [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) tool to upload the project files:

```shell
ampy --port /dev/tty.YOURUSBDEVICE put path/to/file.py
```

where `/dev/tty.YOURUSBDEVICE` is the absolute path to the serial interface of your Wemos device and `path/to/file.py` is the relative path to the file you want to upload.


## Setup MicroPython

Wemos D1 mini boards have Micropython installed by default. To update the Micropython to the latest version:

1. Install [Python](https://www.python.org/downloads) (use [Homebrew](https://brew.sh) on macOS) and [esptool.py](https://github.com/espressif/esptool).

    ```shell
    pip install esptool
    ```

2. Download the [latest firmware binary `.bin` for ESP8266 boards](https://micropython.org/download#esp8266) from the official Micropython website and save it in the `firmware` directory.

3. Finally, upload the firmware: 

    ```shell
    esptool.py --port /dev/tty.YOURUSBDEVICE --baud 460800 write_flash --flash_size=detect --flash_mode dio 0 firmware/esp8266-VERSION-YOU-DOWNLOADED.bin
    ```

    where `/dev/tty.YOURUSBDEVICE` is absolute path the serial interface of your Wemos device, and `esp8266-VERSION-YOU-DOWNLOADED.bin` is the filename of the firmware binary you downloaded.

    Press and release the Reset button on the device to actually upload the firmware.


## Credits

Created by [Kaspars Dambis](https://kaspars.net).
