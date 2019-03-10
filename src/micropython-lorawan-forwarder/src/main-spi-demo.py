from machine import SPI, Pin
from micropython import const

_REG_OPERATING_MODE = const(0x01)
_REG_VERSION = const(0x42)
_MODE_SLEEP = const(0x00)
_MODE_LORA = const(0x80)
_MODE_STDBY = const(0x01)
_MODE_TX = const(0x83)

BUF = bytearray(2)

device = SPI(1, baudrate=4000000)
cs = Pin(16, Pin.OUT)

def _read_into(address, buf):
    BUF[0] = address & 0x7F # Strip out top bit to set 0 value (read).
    cs.off()
    device.write(BUF[0:1])
    device.readinto(buf)
    cs.on()

def _read_u8(address):
    _read_into(address, BUF)
    return BUF[0]

def _write_u8(address, val):
    BUF[0] = (address | 0x80)  # MSB 1 to Write
    BUF[1] = val
    cs.off()
    device.write(BUF)
    cs.on()

version = _read_u8(_REG_VERSION);

mode_before = _read_u8(_REG_OPERATING_MODE);

_write_u8(_REG_OPERATING_MODE, _MODE_LORA);
mode_after = _read_u8(_REG_OPERATING_MODE);

print(version, mode_before, mode_after)

_write_u8(_REG_OPERATING_MODE, _MODE_SLEEP);
