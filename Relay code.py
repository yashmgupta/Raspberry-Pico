# Simple Relay code for 2 Channel DC 5V Relay Module

import utime
from machine import Pin

relay = Pin(2, Pin.OUT)
relay2= Pin(0, Pin.OUT)

relay.high()
utime.sleep(3)
relay2.low()
utime.sleep(3)
relay.low()
utime.sleep(3)
relay2.high()

