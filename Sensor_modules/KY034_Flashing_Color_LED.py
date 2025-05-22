# KY-034 Automatic Flashing Color LED demo
import machine
import time

LED_PIN = machine.Pin(13, machine.Pin.OUT)

while True:
    LED_PIN.on()
    print("LED ON")
    time.sleep(4)
    LED_PIN.off()
    print("LED OFF")
    time.sleep(2)

  

  

