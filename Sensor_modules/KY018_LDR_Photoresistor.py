# KY-018 Photoresistor demo
import machine
import time

PHOTORESISTOR_PIN = 36  # ADC input pin
adc = machine.ADC(machine.Pin(PHOTORESISTOR_PIN))
adc.atten(machine.ADC.ATTN_11DB)  # Full range 0-3.3V

while True:
    light_intensity = adc.read()
    print("Light Intensity:", light_intensity)
    time.sleep(0.5)

  

  

