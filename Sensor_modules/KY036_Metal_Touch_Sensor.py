# KY-036 Metal Touch Sensor demo
import machine
import time

ANALOG_PIN = machine.ADC(machine.Pin(34))
ANALOG_PIN.atten(machine.ADC.ATTN_11DB)
DIGITAL_PIN = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    analog_value = ANALOG_PIN.read()
    voltage = (analog_value / 4095) * 3300  # Convert to millivolts
    digital_value = DIGITAL_PIN.value()
    print("Analog Voltage:", voltage, "mV", "| Digital State:", "Touched" if digital_value == 1 else "Not Touched")
    time.sleep(1)

  

  

