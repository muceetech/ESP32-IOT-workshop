from machine import RTC
from time import sleep 

rtc = RTC()
rtc.datetime((2024, 3, 7, 5, 9, 50, 0, 0)) # set a specific date and time
#(year, month, day, weekday, hours, minutes, seconds, subseconds)
dt=rtc.datetime() # get date and time
while True:
    dt=rtc.datetime() # get date and time
    print(dt[2],'-',dt[1],'-',dt[0])
    print(dt[4],':',dt[5],':',dt[6])
    sleep(1)
    
