import machine
import time

LASER_PIN = machine.Pin(5, machine.Pin.OUT)

while True:
    LASER_PIN.value(1)  # Turn on the laser
    time.sleep(1)        # Wait for one second
    LASER_PIN.value(0)  # Turn off the laser
    time.sleep(1)        # Wait for one second

  

  

