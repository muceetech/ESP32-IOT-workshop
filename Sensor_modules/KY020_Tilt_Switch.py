# KY-020 Tilt Switch demo
import machine
import time

TILT_SWITCH_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if TILT_SWITCH_PIN.value() == 0:
        print("Inclination recognized")
        time.sleep(1)
    time.sleep(0.1)

  

  

