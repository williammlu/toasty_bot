# from motor2 import Motor2
from motor import StepperMotor
from motor import GearBoxMotor
from contact_switch import ContactSwitch

import pigpio
import time

# pi = pigpio.pi()
m1 = StepperMotor(13,06, resolution="1/32") # white wires
m2 = StepperMotor(26,19) # gray and blue wires
m3 = GearBoxMotor(23) # blue single wire
m4 = StepperMotor(16,12) # red and gray wire

c1 = ContactSwitch(20)

def stop_all():
    m1.stop()
    m2.stop()
    m3.stop()
    m4.stop()
try:
    print("Starting 5 rotations")
    # m2.spin(20,2,False)
    m4.spin(20,2,False)
    # m2.spin(0.25,1,True)
    # m4.spin(0.25,1,True)
    # time.sleep(1)
    # m1.spin(0.25,1,False)
    # m2.spin(0.25,1,False)
    # m4.spin(0.25,1,False)
    print("cycle", k)
except KeyboardInterrupt:
    print("keyboard escape")
    stop_all()

# i = 0
# while True:
    # time.sleep(0.01)
    # m1.pi_start(pulses=500)
    # m2.pi_start()
    # if i%1000 == 0:
        # m1.set_dir(Motor.CW)
    # elif i%1000 == 500:
        # m1.set_dir(Motor.CCW)
    # i += 1

m1.exit()
m2.exit()
m3.exit()
m4.exit()
pi.stop()




