import machine
import time
import math

SENSOR_PIN = 36  # ADC input pin
adc = machine.ADC(machine.Pin(SENSOR_PIN))
adc.atten(machine.ADC.ATTN_11DB)  # Full range 0-3.3V

def get_temperature():
    raw = adc.read()
    voltage = raw  (3.3 / 4095.0)
    resistance = (3.3 - voltage)  10000 / voltage
    temperature = 1 / (math.log(resistance / 10000) / 3950 + 1 / 298.15) - 273.15
    return temperature

while True:
    print("Temperature:", round(get_temperature(), 2), "°C")
    time.sleep(1)

  

  

