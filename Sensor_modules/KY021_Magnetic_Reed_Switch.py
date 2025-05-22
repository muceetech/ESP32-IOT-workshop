# KY-021 Mini Magnetic Reed Switch
import machine
import time

REED_SWITCH_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if REED_SWITCH_PIN.value() == 0:
        print("Magnetic field detected")
        time.sleep(0.1)
    time.sleep(0.1)

  

  

