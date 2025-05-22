# KY-023 Dual Axis Joystick demo
import machine
import time

JOYSTICK_X = machine.ADC(machine.Pin(36))
JOYSTICK_Y = machine.ADC(machine.Pin(39))
BUTTON = machine.Pin(34, machine.Pin.IN, machine.Pin.PULL_UP)

JOYSTICK_X.atten(machine.ADC.ATTN_11DB)
JOYSTICK_Y.atten(machine.ADC.ATTN_11DB)

while True:
    x_value = JOYSTICK_X.read()
    y_value = JOYSTICK_Y.read()
    button_state = BUTTON.value()
    print("X:", x_value, "Y:", y_value, "Button:", "Not Pressed" if button_state else "Pressed")
    time.sleep(0.2)

  

  

