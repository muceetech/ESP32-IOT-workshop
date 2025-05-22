# KY-051 Voltage Translator Level Shifter demo
import machine
import time

LOW_VOLT_PIN = machine.Pin(2, machine.Pin.IN)
HIGH_VOLT_PIN = machine.Pin(3, machine.Pin.OUT)

while True:
    low_signal = LOW_VOLT_PIN.value()
    HIGH_VOLT_PIN.value(low_signal)
    print("Low Voltage Signal:", low_signal, "-> High Voltage Output:", HIGH_VOLT_PIN.value())
    time.sleep(0.5)

  

  


