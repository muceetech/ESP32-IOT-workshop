# KY-031 Knock Sensor demo
import machine
import time

KNOCK_SENSOR_PIN = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if KNOCK_SENSOR_PIN.value() == 0:
        print("Knock detected!")
        time.sleep(0.2)  # Debounce delay
    time.sleep(0.05)

  

  

