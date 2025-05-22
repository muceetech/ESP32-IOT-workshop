# KY-024 Linear Magnetic Hall Sensor demo
import machine
import time

HALL_SENSOR_ANALOG_PIN = machine.ADC(machine.Pin(36))
HALL_SENSOR_ANALOG_PIN.atten(machine.ADC.ATTN_11DB)
HALL_SENSOR_DIGITAL_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    analog_value = HALL_SENSOR_ANALOG_PIN.read()
    digital_value = HALL_SENSOR_DIGITAL_PIN.value()
    print("Analog:", analog_value, "Digital:", "Threshold Reached" if digital_value else "Not Reached")
    time.sleep(1)

  

  

