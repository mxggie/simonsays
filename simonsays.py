import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

colors = [ 'R' , 'G' , 'B' , 'Y' ]
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def blink_lights(): 
    for i in range(0, len(colors)):
        n = random.randint(0,3)
        colors.append(colors[n])
#        color_string = ''.join(colors)            
        LED.setColor(colors[n])
        time.sleep(0.5)
        LED.noColor()
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        while True: 
            blink_lights()
    except KeyboardInterrupt:
        print 'Game Over'
