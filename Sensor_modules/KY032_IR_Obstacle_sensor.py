# KY-032 Infrared Obstacle sensor demo
import machine
import time

SENSOR_PIN = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if SENSOR_PIN.value() == 0:
        print("Obstacle detected")
    else:
        print("No obstacle")
    time.sleep(0.5)

  

  

