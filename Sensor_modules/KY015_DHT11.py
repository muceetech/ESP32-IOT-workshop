import dht
import machine
import time

sensor = dht.DHT11(machine.Pin(4))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature:", temp, "°C", " Humidity:", humidity, "%")
    except OSError as e:
        print("Failed to read sensor.")
    time.sleep(2)

  

  

