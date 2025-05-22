# KY-028 Digital Temperature sensor
import machine
import time

TEMP_SENSOR_ANALOG_PIN = machine.ADC(machine.Pin(36))
TEMP_SENSOR_ANALOG_PIN.atten(machine.ADC.ATTN_11DB)
TEMP_SENSOR_DIGITAL_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
LED_PIN = machine.Pin(16, machine.Pin.OUT)

while True:
    analog_value = TEMP_SENSOR_ANALOG_PIN.read()
    digital_value = TEMP_SENSOR_DIGITAL_PIN.value()
    if digital_value:
        LED_PIN.on()
        print("Temperature threshold exceeded - Analog:", analog_value)
    else:
        LED_PIN.off()
        print("Temperature normal - Analog:", analog_value)
    time.sleep(1)

  

  

