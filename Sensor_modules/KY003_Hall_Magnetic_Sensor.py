import machine
import time

HALL_SENSOR_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(2, machine.Pin.OUT)

while True:
    if HALL_SENSOR_PIN.value() == 0:
        print("Magnetic field detected")
        LED_PIN.on()
    else:
        print("No magnetic field detected")
        LED_PIN.off()
    time.sleep(1)

  

  

