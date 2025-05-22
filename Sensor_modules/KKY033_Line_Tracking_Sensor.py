# KY-033 Line Tracking Sensor demo
import machine
import time

SENSOR_PIN = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if SENSOR_PIN.value() == 1:
        print("Line detected")
    else:
        print("No line detected")
    time.sleep(0.5)

  

  

