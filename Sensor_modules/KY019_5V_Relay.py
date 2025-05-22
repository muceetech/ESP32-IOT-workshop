# KY-019 5V Relay Module demo
import machine
import time

RELAY_PIN = machine.Pin(5, machine.Pin.OUT)

while True:
    RELAY_PIN.value(1)
    print("Relay is ON")
    time.sleep(1)
    RELAY_PIN.value(0)
    print("Relay is OFF")
    time.sleep(1)

  

  

