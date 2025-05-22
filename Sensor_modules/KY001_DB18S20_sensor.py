import machine
import onewire
import ds18x20
import time

pin = machine.Pin(4)
ow = onewire.OneWire(pin)
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
while True:
    ds.convert_temp()
    time.sleep(1)
    for rom in roms:
        print("Temperature:", ds.read_temp(rom))
    time.sleep(2)

  

  


