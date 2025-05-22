import machine
import time

SENSOR_PIN = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(2, machine.Pin.OUT)

while True:
    if SENSOR_PIN.value() == 1:
        print("Object detected")
        LED_PIN.on()
    else:
        LED_PIN.off()
    time.sleep(0.1)

  

  

