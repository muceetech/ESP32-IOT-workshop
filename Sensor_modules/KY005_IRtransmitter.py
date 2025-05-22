import machine
import time

IR_TX_PIN = machine.Pin(17, machine.Pin.OUT)

def send_pulse():
    for _ in range(32):
        IR_TX_PIN.value(1)
        time.sleep_us(562)
        IR_TX_PIN.value(0)
        time.sleep_us(562)

while True:
    print("Sending IR signal")
    send_pulse()
    time.sleep(5)

  

  

