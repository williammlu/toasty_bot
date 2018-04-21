# from motor2 import Motor2
from motor import StepperMotor
from motor import GearBoxMotor
import pigpio
import time

"""
    Run with `python -i test.py`

"""



m1 = StepperMotor(13,06, resolution="1/32") # white wires
m2 = StepperMotor(26,19) # gray and blue wires
m3 = GearBoxMotor(23) # blue single wire


def quit():
    m1.exit()
    m2.exit()
    m3.exit()



