# KY-050 Ultrasonic Distance Sensor demo
import machine
import time

TRIGGER_PIN = machine.Pin(5, machine.Pin.OUT)
ECHO_PIN = machine.Pin(18, machine.Pin.IN)

def measure_distance():
    TRIGGER_PIN.off()
    time.sleep_us(2)
    TRIGGER_PIN.on()
    time.sleep_us(10)
    TRIGGER_PIN.off()

    while ECHO_PIN.value() == 0:
        start_time = time.ticks_us()
    while ECHO_PIN.value() == 1:
        end_time = time.ticks_us()

    duration = end_time - start_time
    distance = duration / 58.2
    return distance

while True:
    dist = measure_distance()
    if 2 <= dist <= 300:
        print("Distance:", dist, "cm")
    else:
        print("Out of range")
    time.sleep(0.5)

  

  

