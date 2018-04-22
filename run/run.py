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
    print("Starting all motors\nLooping and waiting for contact switch")
    need_stop =  0
    def motor_stop_callback(gpio, level, tick):
        global need_stop
        if gpio == 20:
            stop_all()
            need_stop = 1
    c1.callback = motor_stop_callback

    for l in range(30):
        m1.start(duty=25)
        m2.start(duty=25)
        m4.start(duty=25)
        while not need_stop:
            time.sleep(0.1)
        need_stop = 0
        time.sleep(1)

except KeyboardInterrupt:
    print("keyboard escape")
    stop_all()

try:
    print("Starting gearbox motor")
    for l in range(30):
        # m3.pwm_test()
        m3.start(duty=60, pulses=10)
        # import pdb; pdb.set_trace() 
        time.sleep(.1)
        m3.stop()
        time.sleep(1)
except KeyboardInterrupt:
    print("keyboard escape")
    m3.stop()


try:
    print("Starting stepper motor")
    for l in range(30):
        for k in range(30):
            m1.start(duty=25)
            m2.start(duty=25)
            m4.start(duty=25)
            time.sleep(1)
            stop_all()
            m1.spin(1, 5)
            m2.spin(1, 5)
            m4.spin(1, 5)
            time.sleep(1)
except KeyboardInterrupt:
    print("keyboard escape")
    stop_all()
    
try:
    print("Starting quarter rotations")
    for k in range(30):
        m1.spin(0.25,1,True)
        m2.spin(0.25,1,True)
        m4.spin(0.25,1,True)
        time.sleep(1)
        m1.spin(0.25,1,False)
        m2.spin(0.25,1,False)
        m4.spin(0.25,1,False)
        time.sleep(1)
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




