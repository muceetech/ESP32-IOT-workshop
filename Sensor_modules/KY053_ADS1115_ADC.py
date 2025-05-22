# KY-053 Analog Digital converter ADS1115
import machine
import time
from ads1x15 import ADS1115

i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
adc = ADS1115(i2c, address=0x48)

while True:
    for i in range(4):
        value = adc.read(i)
        print(f"AIN{i}: {value}")
    time.sleep(1)

  

  

