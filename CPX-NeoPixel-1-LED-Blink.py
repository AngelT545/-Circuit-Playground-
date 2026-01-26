import board
import digitalio
import time
print(dir(board))
print('')
led = digitalio.DigitalInOut(board.LED)
print(dir(led))
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
