# KY-017 Mercury Tilt Switch demo
import machine
import time

TILT_SENSOR_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(2, machine.Pin.OUT)

while True:
    if TILT_SENSOR_PIN.value() == 0:
        print("Tilt detected")
        LED_PIN.on()
    else:
        LED_PIN.off()
    time.sleep(1)

  

  

