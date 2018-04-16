import pigpio
import time

class Motor:
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    SPR = 48   # Steps per Revolution (360 / 7.5)

    RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

    def __init__(self, DIR_PIN, STEP_PIN, pi, rotation=Motor.CW, resolution="Full", mode=(14,15,18)):
        self.DIR_PIN = DIR_PIN
        self.STEP_PIN = STEP_PIN
        self.resolution = Motor.RESOLUTION[resolution]
        self.mode = mode
        self.pi = pi
        self.set_rotation(rotation)

    def set_rotation(self, rotation):
        self.rotation = rotation

    def pi_setup(self):
        if not self.pi:
            self.pi = pigpio.pi()

        self.pi.set_mode(self.DIR_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.STEP_PIN, pigpio.OUTPUT)
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution[i])
    
    def pi_start(self, pwm=128, pulses=500, direction=None):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, pwm)  # PWM 128 out of 256 on halfway
        self.pi.set_PWM_frequency(self.STEP_PIN, pulses)

    def pi_stop(self):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, 0)
        self.pi.set_PWM_frequency(self.STEP_PIN, 0)

    def pi_go(self, steps=200, step_delay=.005, rotations=None):
        if rotations:
            steps = rotations * Motor.SPR

        for i in steps:
            self.pi.write(STEP_PIN, 1)
            time.sleep(stepdelay)
            self.pi.write(STEP_PIN, 0)
            time.sleep(stepdelay)

    def pi_exit(self):
        self.pi_stop() # stop pwm
        self.pi.stop() # stop pi
