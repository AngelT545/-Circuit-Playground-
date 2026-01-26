import board
import digitalio
import time

led = neopixel.Neopixel(board.NEOPIXEL,10)
led.brightness=0.1
print(dir(led))
while True: 
    led[0] = (225,0,0)
    time.sleep(.5)
    led[6] = (225,0,0)
    time.sleep(.5)
    led[6] = (0,234,0)
    time.sleep(.5)
    led[0] = (0,0,213)
    time.sleep(.5)
