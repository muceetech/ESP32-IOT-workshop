from machine import TouchPad, Pin
import time

touch_pin = TouchPad(Pin(15, mode=Pin.IN))
while True:
    touch_value = touch_pin.read()
    print(touch_value)
    time.sleep_ms(500)