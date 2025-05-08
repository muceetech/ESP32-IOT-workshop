from machine import Pin, ADC 
from time import sleep 
pot = ADC(Pin(34)) 
while True: 
    pot_value = pot.read() 
    print(pot_value) 
    sleep(0.1) 
