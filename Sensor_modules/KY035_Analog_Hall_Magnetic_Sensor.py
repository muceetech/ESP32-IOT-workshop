# KY-035 Analog Hall Magnetic Sensor demo
import machine
import time

SENSOR_PIN = machine.ADC(machine.Pin(34))
SENSOR_PIN.atten(machine.ADC.ATTN_11DB)

while True:
    raw_value = SENSOR_PIN.read()
    voltage = (raw_value / 4095) * 3300  # Convert to millivolts
    print("Magnetic Field Voltage:", voltage, "mV")
    time.sleep(1)

  

  

