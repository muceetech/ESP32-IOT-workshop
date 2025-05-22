# KY-029 Dual Color LED demo 
import machine
import time

LED_RED_PIN = machine.Pin(16, machine.Pin.OUT)
LED_GREEN_PIN = machine.Pin(17, machine.Pin.OUT)

while True:
    LED_RED_PIN.on()
    LED_GREEN_PIN.off()
    print("Red LED ON")
    time.sleep(3)
    
    LED_RED_PIN.off()
    LED_GREEN_PIN.on()
    print("Green LED ON")
    time.sleep(3)

  

  

