# KY-054 Phototransistor module demo
import machine
import time
import math

LIGHT_SENSOR_PIN = machine.ADC(machine.Pin(36))
LIGHT_SENSOR_PIN.atten(machine.ADC.ATTN_11DB)

while True:
    raw_value = LIGHT_SENSOR_PIN.read()
    voltage = (raw_value / 4095)  3.3
    resistance = (3.3  10000.0) / (voltage if voltage > 0 else 1)
    current = (3.3 / resistance) * 1000000.0
    lux = math.log(current) / 0.06
    print("Light Intensity:", lux, "lux")
    time.sleep(1)

  

  

