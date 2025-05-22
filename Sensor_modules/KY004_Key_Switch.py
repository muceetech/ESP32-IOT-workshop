import machine
import time

BUTTON_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(2, machine.Pin.OUT)

while True:
    if BUTTON_PIN.value() == 0:
        print("Button pressed")
        LED_PIN.on()
    else:
        print("Button released")
        LED_PIN.off()
    time.sleep(0.1)

  

  

