import time
from machine import Pin, freq
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

pin_ir = Pin(14, Pin.IN) # IR receiver

# Decode the received data and return the corresponding key name
def decodeKeyValue(data):       
    if data == 0x16:
        return "0"
    if data == 0x0C:
        return "1"
    if data == 0x18:
        return "2"
    if data == 0x5E:
        return "3"
    if data == 0x08:
        return "4"
    if data == 0x1C:
        return "5"
    if data == 0x5A:
        return "6"
    if data == 0x42:
        return "7"
    if data == 0x52:
        return "8"
    if data == 0x4A:
        return "9"
    return "ERROR"

# User callback
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(decodeKeyValue(data))
        

ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver

# Show debug information
ir.error_function(print_error)  

# keep the script running until interrupted by a keyboard interrupt (Ctrl+C)
try:
    while True:
        pass
except KeyboardInterrupt:
    ir.close()  # Close the receiver