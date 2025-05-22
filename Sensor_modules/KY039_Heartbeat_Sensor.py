# KY-039 Heartbeat Sensor demo
import machine
import time

SENSOR_PIN = machine.ADC(machine.Pin(34))
SENSOR_PIN.atten(machine.ADC.ATTN_11DB)

while True:
    sensor_value = SENSOR_PIN.read()
    voltage = (sensor_value / 4095) * 3300  # Convert to millivolts
    print("Analog Voltage:", voltage, "mV")
    time.sleep(0.01)

  

  

