from motor import StepperMotor
from motor import GearBoxMotor
from heater import Heater
from contact_switch import ContactSwitch

import pigpio
import time

linear_push = StepperMotor(13,06, ENABLE_PIN=17) # green and orange wires
mm_rotate_motor = GearBoxMotor(23) # blue single wire
cracker_motor = StepperMotor(26,19, ENABLE_PIN=27) # gray and blue wires
chocolate_motor = StepperMotor(16,12, ENABLE_PIN=3) # red and gray wire
rotate_base_motor = StepperMotor(5,11, ENABLE_PIN=2) # purple and green

h1 = Heater(7) # bright yellow wire with some green

c1 = ContactSwitch(20)

def stop_all():
    linear_push.stop()
    cracker_motor.stop()
    mm_rotate_motor.stop()
    chocolate_motor.stop()
    rotate_base_motor.stop()
    h1.stop()
    pigpio.stop()

def test_linear(motor=chocolate_motor):
    motor.spin(42,5,1)
    motor.spin(42,5,0)

def test_marshmallow():
    linear_push.spin(0.8,2,1)
    linear_push.spin(0.8,2,0)
    time.sleep(2)
    linear_push.spin(0.8,2,1)
    mm_rotate_motor.start(duty=60, pulses=10)
    time.sleep(10)
    mm_rotate_motor.stop()
    linear_push.spin(0.8,2,0)
def quick_spin():
    mm_rotate_motor.start(duty=200, pulses=10)
    time.sleep(0.1)
    mm_rotate_motor.stop()




# try:
    # print("Starting heater PWM")
    # h1.start()
    # while(1):
        # time.sleep(1)
# 
# except KeyboardInterrupt:
    # print("keyboard escape")
    # stop_all()
 


# try:
    # print("Starting all motors\nLooping and waiting for contact switch")
    # need_stop =  0
    # def motor_stop_callback(gpio, level, tick):
        # global need_stop
        # if gpio == 20:
            # stop_all()
            # need_stop = 1
    # c1.callback = motor_stop_callback
# 
    # for l in range(30):
        # linear_push.start(duty=25)
        # cracker_motor.start(duty=25)
        # chocolate_motor.start(duty=25)
        # rotate_base_motor.start(duty=25)
        # while not need_stop:
            # time.sleep(0.1)
        # need_stop = 0
        # time.sleep(1)
# 
# except KeyboardInterrupt:
    # print("keyboard escape")
    # stop_all()

# try:
    # print("Starting gearbox motor")
    # for l in range(30):
        # mm_rotate_motor.start(duty=60, pulses=10)
        # import pdb; pdb.set_trace() 
        # time.sleep(.1)
        # mm_rotate_motor.stop()
        # time.sleep(1)
# except KeyboardInterrupt:
    # print("keyboard escape")
    # mm_rotate_motor.stop()
# 
# 
# try:
    # print("Starting stepper motor")
    # for l in range(30):
        # for k in range(30):
            # linear_push.start(duty=25)
            # cracker_motor.start(duty=25)
            # chocolate_motor.start(duty=25)
            # time.sleep(1)
            # stop_all()
            # linear_push.spin(1, 5)
            # cracker_motor.spin(1, 5)
            # chocolate_motor.spin(1, 5)
            # time.sleep(1)
# except KeyboardInterrupt:
    # print("keyboard escape")
    # stop_all()
    # 
# try:
    # print("Starting quarter rotations")
    # for k in range(30):
        # linear_push.spin(0.25,1,True)
        # cracker_motor.spin(0.25,1,True)
        # chocolate_motor.spin(0.25,1,True)
        # time.sleep(1)
        # linear_push.spin(0.25,1,False)
        # cracker_motor.spin(0.25,1,False)
        # chocolate_motor.spin(0.25,1,False)
        # time.sleep(1)
        # print("cycle", k)
# except KeyboardInterrupt:
    # print("keyboard escape")
    # stop_all()
# chocolate_motor.spin(10,1,False)

# i = 0
# while True:
    # time.sleep(0.01)
    # linear_push.pi_start(pulses=500)
    # cracker_motor.pi_start()
    # if i%1000 == 0:
        # linear_push.set_dir(Motor.CW)
    # elif i%1000 == 500:
        # linear_push.set_dir(Motor.CCW)
    # i += 1

# linear_push.exit()
# cracker_motor.exit()
# mm_rotate_motor.exit()
# chocolate_motor.exit()
# rotate_base_motor.exit()
# pigpio.pi().stop()




