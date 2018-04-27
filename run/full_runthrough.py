from motor import StepperMotor
from motor import GearBoxMotor
from heater import Heater
from contact_switch import ContactSwitch

import pigpio
import time

# pi = pigpio.pi()
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

try:
    rotate_base_motor.spin(1.625/2, 3, 0) # 90 deg clockwise
    time.sleep(1)
    rotate_base_motor.set_power(True)
    linear_push.spin(0.8,2,1)# push skewer forward
    time.sleep(5)
    linear_push.spin(0.8,2,0) # pull skewer back
    rotate_base_motor.set_power(False)
    time.sleep(1)

    rotate_base_motor.spin(1.625, 3, 1) # 180 deg counter-clockwise
    time.sleep(1)
    linear_push.spin(0.8,4,1) # push skewer forward
    time.sleep(5)
    linear_push.spin(0.8,4,0) # pull skewer back
    time.sleep(1)

    rotate_base_motor.spin(1.625/2, 3, 0) # 90 deg clockwise
    time.sleep(1)
    rotate_base_motor.set_power(True)
    cracker_motor.spin(42, 5, 1)
    cracker_motor.spin(42, 5, 0)
    time.sleep(1)
    chocolate_motor.spin(42, 5, 1)
    chocolate_motor.spin(42, 5, 0)
    rotate_base_motor.set_power(False)
    time.sleep(1)
    linear_push.spin(0.8,4,1) # push skewer forward
    time.sleep(1)
    cracker_motor.spin(42, 5, 1)
    time.sleep(1)
    cracker_motor.spin(42, 5, 0)
    print("GOGOGOG")
    time.sleep(10)

except KeyboardInterrupt:
    stop_all()


# linear_push.exit()
# cracker_motor.exit()
# mm_rotate_motor.exit()
# chocolate_motor.exit()
# rotate_base_motor.exit()
# pigpio.pi().stop()




