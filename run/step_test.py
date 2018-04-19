# from motor2 import Motor2
from motor import StepperMotor
from motor import GearBoxMotor
import pigpio
import time

# pi = pigpio.pi()
while True:
    try:
        res = raw_input("Enter resolution = ")
        m1 = StepperMotor(13,06, resolution=res) 
        m1.start()
    except KeyboardInterrupt:
        print("keyboard escape")
        m1.stop()
