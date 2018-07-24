import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
#This script blinks one of four random colors on the RGB LED

colors = [ 'R' , 'G' , 'B' , 'Y' ]
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

n = random.randint(0,3)
LED.setColor(colors [n])
time.sleep(1)
LED.noColor()
LED.destroy()
