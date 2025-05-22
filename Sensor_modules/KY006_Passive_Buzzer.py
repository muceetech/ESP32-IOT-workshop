import machine
import time

BUZZER_PIN = machine.Pin(18, machine.Pin.OUT)
PWM = machine.PWM(BUZZER_PIN)
PWM.freq(2000)

while True:
    PWM.duty(512)  # 50% duty cycle
    time.sleep(0.5)
    PWM.duty(0)
    time.sleep(0.5)

  

  

