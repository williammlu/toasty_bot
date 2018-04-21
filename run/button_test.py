import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
# 
# GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# 
# while True:
    # input_state = GPIO.input(20)
    # if input_state == 1:
        # print('Button Pressed')
        # time.sleep(0.2)
# 

import pigpio

pin = 20

pi = pigpio.pi()

pi.set_mode(pin, pigpio.INPUT)
pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
while True:
    input_state = pi.read(pin)
    if input_state == 1:
        print('Button Pressed')
        time.sleep(0.2)


