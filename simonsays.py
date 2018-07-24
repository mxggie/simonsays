import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

colors = [ 'R' , 'G' , 'B' , 'Y' ]
freq = [220, 440, 880, 1760]

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin, 1000)

def blink_lights(): 
    n = random.randint(0,3)    
    color_sequence = [colors[n]]
    freq_sequence = [freq[n]]
    while True:
        for i in range(0, len(color_sequence)):             
            LED.setColor(color_sequence[i])
            time.sleep(0.5)
            Buzz.ChangeFrequency(freq_sequence[i])        
            Buzz.start(50)
            time.sleep(0.5)
            Buzz.stop()
            LED.noColor()
            time.sleep(0.5)
        n = random.randint(0,3)            
        color_sequence.append(colors[n])
        freq_sequence.append(freq[n])
        time.sleep(1)

if __name__ == '__main__':
    try:
        while True: 
            blink_lights()
    except KeyboardInterrupt:
        print 'Game Over'
