import pigpio
import time
import RPi.GPIO as GPIO

class StepperMotor:
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    SPR = 200   # Steps per Revolution (360 / 1.8)

    RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

    delays = {1: 0.01, 2: 0.005, 3: 0.002, 4:0.001, 5:0.0004}

    def __init__(self, DIR_PIN, STEP_PIN, pi=None, rotation=CW, resolution="Full", mode=(14,15,18)):
        self.DIR_PIN = DIR_PIN
        self.STEP_PIN = STEP_PIN
        self.resolution = StepperMotor.RESOLUTION.get(resolution, (0,0,0)) # default to Full if entered wrong
        if resolution != "Full":
            print("Resolution is {}".format(resolution))
        self.mode = mode
        self.pi = pi
        self.setup()
        self.set_dir(rotation)

    def setup(self):
        if not self.pi:
            self.pi = pigpio.pi()

        self.pi.set_mode(self.DIR_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.STEP_PIN, pigpio.OUTPUT)
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution[i])

    def set_dir(self, rotation):
        self.pi.write(self.DIR_PIN, rotation)
    
    def start(self, duty=128, pulses=500, direction=None):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, duty)  # PWM 128 out of 256 on halfway
        self.pi.set_PWM_frequency(self.STEP_PIN, pulses)

    def stop(self):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, 0)
        self.pi.set_PWM_frequency(self.STEP_PIN, 0)

    def go(self, steps=200, step_delay=.001, rev=None):
        if rev:
            steps = (int) (rev * StepperMotor.SPR)
        step_delay = max(step_delay, 0.0004) # tested minimum delay of 0.0004

        for i in range(steps):
            self.pi.write(self.STEP_PIN, 1)
            time.sleep(step_delay)
            self.pi.write(self.STEP_PIN, 0)
            time.sleep(step_delay)



    def spin(self, rev, speed, is_cw=True):
        """ Simplified interface """
        self.set_dir(StepperMotor.CW if is_cw else StepperMotor.CCW)
        if type(speed) is not int or speed not in (1,2,3,4,5):
            print("Your speed {} is invalid".format(speed))
            speed = 2
        self.go(step_delay=StepperMotor.delays[speed], rev=rev)
            


    def exit(self):
        self.stop() # stop pwm
        self.pi.stop() # stop pi


class GearBoxMotor:
    
    def __init__(self, STEP_PIN, pi=None):
        self.STEP_PIN = STEP_PIN
        self.pi = pi
        self.setup()

    def setup(self):
        if not self.pi:
            self.pi = pigpio.pi()

        self.pi.set_mode(self.STEP_PIN, pigpio.OUTPUT)
    def start(self, duty=128, pulses=500, direction=None):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, duty)  # PWM 128 out of 256 on halfway
        self.pi.set_PWM_frequency(self.STEP_PIN, pulses)

    def stop(self):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, 0)
        self.pi.set_PWM_frequency(self.STEP_PIN, 0)

