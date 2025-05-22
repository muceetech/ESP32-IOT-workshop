# KY-027 Magic Light Cup demo based on mercury tilt sensor
import machine
import time

TILT_SENSOR_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(16, machine.Pin.OUT)

while True:
    if TILT_SENSOR_PIN.value() == 0:
        LED_PIN.on()
        print("Tilt detected - LED ON")
    else:
        LED_PIN.off()
        print("No tilt detected - LED OFF")
    time.sleep(0.2)

  

  

