# KY-022 Infrared Receiver demo (Simple only no IR NEC code)
from machine import Pin
import time

IR_PIN = Pin(4, Pin.IN)

def ir_callback(pin):
    print("IR signal detected")

IR_PIN.irq(trigger=Pin.IRQ_FALLING, handler=ir_callback)

while True:
    time.sleep(1)

  

  

