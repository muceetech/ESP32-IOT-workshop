# KY-026 Flame Sensor
import machine
import time

FLAME_SENSOR_ANALOG_PIN = machine.ADC(machine.Pin(36))
FLAME_SENSOR_ANALOG_PIN.atten(machine.ADC.ATTN_11DB)
FLAME_SENSOR_DIGITAL_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    analog_value = FLAME_SENSOR_ANALOG_PIN.read()
    digital_value = FLAME_SENSOR_DIGITAL_PIN.value()
    print("Analog:", analog_value, "Digital:", "Flame Detected" if digital_value else "No Flame")
    time.sleep(1)

  

  

