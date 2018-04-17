import pigpio
import time

class Motor:
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

    def __init__(self, DIR_PIN, STEP_PIN, pi, rotation=CW, resolution="Full", mode=(14,15,18)):
        self.DIR_PIN = DIR_PIN
        self.STEP_PIN = STEP_PIN
        self.resolution = Motor.RESOLUTION[resolution]
        self.mode = mode
        self.pi = pi
        self.set_dir(rotation)
        self.pi_setup()

    def pi_setup(self):
        if not self.pi:
            self.pi = pigpio.pi()

        self.pi.set_mode(self.DIR_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.STEP_PIN, pigpio.OUTPUT)
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution[i])

    def set_dir(self, rotation):
        self.pi.write(self.DIR_PIN, rotation)
    
    def pi_start(self, pwm=128, pulses=500, direction=None):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, pwm)  # PWM 128 out of 256 on halfway
        self.pi.set_PWM_frequency(self.STEP_PIN, pulses)

    def pi_stop(self):
        self.pi.set_PWM_dutycycle(self.STEP_PIN, 0)
        self.pi.set_PWM_frequency(self.STEP_PIN, 0)

    def pi_go(self, steps=200, step_delay=.005, rev=None):
        if rev:
            steps = rev * Motor.SPR
        step_delay = max(step_delay, 0.0004) # tested minimum delay of 0.0004

        for i in range(steps):
            self.pi.write(self.STEP_PIN, 1)
            time.sleep(step_delay)
            self.pi.write(self.STEP_PIN, 0)
            time.sleep(step_delay)



    def pi_spin(self, rev, speed, is_cw=True):
        """ Simplified interface """
        self.set_dir(Motor.CW if is_cw else Motor.CCW)
        if type(speed) is not int or speed not in (1,2,3,4,5):
            print("Your speed {} is invalid".format(speed))
            speed = 2
        self.pi_go(step_delay=Motor.delays[speed], rev=rev)
            


    def pi_exit(self):
        self.pi_stop() # stop pwm
        self.pi.stop() # stop pi
