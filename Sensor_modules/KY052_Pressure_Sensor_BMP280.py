# KY-052 Pressure and Temperature Sensor BMP280
from machine import Pin, I2C
import time
import bmp280

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sensor = bmp280.BMP280(i2c)

while True:
    temperature = sensor.temperature
    pressure = sensor.pressure
    altitude = sensor.altitude
    print("Temperature:", temperature, "°C", "Pressure:", pressure, "hPa", "Altitude:", altitude, "m")
    time.sleep(2)

  

  

