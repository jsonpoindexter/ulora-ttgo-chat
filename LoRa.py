from machine import Pin, SPI, reset
from sx127x import SX127x
import config_lora


def init():
    device_pins = {
        'miso': 19,
        'mosi': 27,
        'ss': 18,
        'sck': 5,
        'dio_0': 26,
        'reset': 16,
        'led': 2,
    }

    device_spi = SPI(baudrate=10000000,
                     polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
                     sck=Pin(device_pins['sck'], Pin.OUT, Pin.PULL_DOWN),
                     mosi=Pin(device_pins['mosi'], Pin.OUT, Pin.PULL_UP),
                     miso=Pin(device_pins['miso'], Pin.IN, Pin.PULL_UP))

    # Restart machine if we get the 'invalid version' error
    try:
        return SX127x(device_spi, pins=device_pins)
    except:
        reset()
