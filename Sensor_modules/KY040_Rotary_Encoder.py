# KY-040 Rotary Encoder demo
import machine
import time

CLK_PIN = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
DT_PIN = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
SW_PIN = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)

counter = 0
last_state_clk = CLK_PIN.value()

while True:
    current_state_clk = CLK_PIN.value()
    if current_state_clk != last_state_clk:
        if DT_PIN.value() != current_state_clk:
            counter += 1
        else:
            counter -= 1
        print("Position:", counter)
    last_state_clk = current_state_clk

    if SW_PIN.value() == 0:
        print("Button Pressed")
        time.sleep(0.1)
    time.sleep(0.05)

  

  

