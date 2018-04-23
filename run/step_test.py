# from motor2 import Motor2
from motor import StepperMotor
import pigpio
import time

# pi = pigpio.pi()
direction = 1
m1 = StepperMotor(16,12) #, resolution=res) 
while True:
    try:
        # res = raw_input("Enter resolution = ")
        m1.start(direction=direction )
    except KeyboardInterrupt:
        print("switching dir")
        m1.stop()
        direction = 0 if direction else 1
        m1.set_dir(direction)
        time.sleep(1)


