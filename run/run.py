# from motor2 import Motor2
from motor import StepperMotor
from motor import GearBoxMotor
import pigpio
import time

# pi = pigpio.pi()
m1 = StepperMotor(13,06) # white wires
m2 = StepperMotor(26,19) # gray and blue wires
m3 = GearBoxMotor(23) # blue single wire


try:
    print("Starting gearbox motor")
    for l in range(30):
        m3.start(pwm=200)
        time.sleep(5)
        m3.stop()
        time.sleep(1)
except KeyboardInterrupt:
    print("keyboard escape")
    m3.stop()


try:
    print("Starting stepper motor")
    for l in range(30):
        for k in range(30):
            m1.start()
            time.sleep(1)
            m1.stop()
            m1.go()
            time.sleep(1)
except KeyboardInterrupt:
    print("keyboard escape")
    m1.stop()
    
try:
    print("Starting quarter rotations")
    for k in range(30):
        m1.spin(0.25,1,True)
        time.sleep(1)
        m1.spin(0.25,1,False)
        time.sleep(1)
        # m2.spin(1 ,2,True)
        # time.sleep(1)
        # m2.spin(1,2,False)
        # time.sleep(1)
        print("cycle", k)
except KeyboardInterrupt:
    print("keyboard escape")
    m1.stop()

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


# m1.exit()



