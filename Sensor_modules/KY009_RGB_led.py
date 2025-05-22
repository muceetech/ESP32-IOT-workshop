import machine
import time

RED_PIN = machine.PWM(machine.Pin(18), freq=1000)
GREEN_PIN = machine.PWM(machine.Pin(19), freq=1000)
BLUE_PIN = machine.PWM(machine.Pin(21), freq=1000)

def set_color(r, g, b):
    RED_PIN.duty(r)
    GREEN_PIN.duty(g)
    BLUE_PIN.duty(b)

while True:
    set_color(1023, 0, 0)  # Red
    time.sleep(1)
    set_color(0, 1023, 0)  # Green
    time.sleep(1)
    set_color(0, 0, 1023)  # Blue
    time.sleep(1)

  

  

