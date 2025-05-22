import machine
import time

RED_PIN = machine.Pin(18, machine.Pin.OUT)
GREEN_PIN = machine.Pin(19, machine.Pin.OUT)

while True:
    RED_PIN.value(1)
    GREEN_PIN.value(0)
    time.sleep(3)
    RED_PIN.value(0)
    GREEN_PIN.value(1)
    time.sleep(3)

  

  

