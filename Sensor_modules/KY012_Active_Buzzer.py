import machine
import time

BUZZER_PIN = machine.Pin(15, machine.Pin.OUT)

while True:
    BUZZER_PIN.value(1)  # Turn buzzer on
    time.sleep(4)        # Wait for 4 seconds
    BUZZER_PIN.value(0)  # Turn buzzer off
    time.sleep(2)        # Wait for 2 seconds

  

  

