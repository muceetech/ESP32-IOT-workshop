
import time
from machine import ADC, Pin

# ===== DECLARATION =====

GAMMA = 0.7;
RL10 = 50;

# ===== MAIN PROGRAM =====

adc = ADC(Pin(32))        # GPIO32
adc.atten(ADC.ATTN_11DB)  # Full range: 0 - 3.6V
adc.width(ADC.WIDTH_12BIT)

while True:
    value = adc.read()                    # 0-4095
    voltage = (value / 4095) * 3.3        # Convert to volts
    resistance = 2000 * voltage / (3.3 - voltage)
    lux = pow(RL10 * 1e3 * pow(10, GAMMA) / resistance, (1 / GAMMA))
    msg = "{:.0f}".format(lux/10)
    print(msg, "Lux")
    time.sleep(0.1)  # 100 ms sampling
