import machine
import time

VIBRATION_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(2, machine.Pin.OUT)

while True:
    if VIBRATION_PIN.value() == 0:
        print("Vibration detected")
        LED_PIN.on()
        time.sleep(0.1)
        LED_PIN.off()
    time.sleep(0.1)

  

  

