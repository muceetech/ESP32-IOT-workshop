import dht
import machine
from time import sleep

d = dht.DHT11(machine.Pin(15))
while True:
    d.measure()
    temp = d.temperature() # eg. 23 (°C)
    hum = d.humidity()    # eg. 41 (% RH)
    print(temp,hum)
    sleep(0.5)