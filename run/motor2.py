import time
import RPi.GPIO as GPIO

class Motor2:
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

    def __init__(self, DIR_PIN, STEP_PIN, rotation=CW, resolution="Full", mode=(14,15,18)):

        self.DIR_PIN = DIR_PIN
        self.STEP_PIN = STEP_PIN
        self.resolution = resolution
        self.mode = mode
        self.gpio_setup()
        self.set_dir(rotation)


    def gpio_setup(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR_PIN, GPIO.OUT)
        GPIO.setup(self.STEP_PIN, GPIO.OUT)
        GPIO.setup(self.mode, GPIO.OUT)
        GPIO.output(self.mode, Motor2.RESOLUTION[self.resolution])


    def set_dir(self, rotation):
        GPIO.output(self.DIR_PIN, rotation)
    

    def go(self, steps=200, step_delay=.001, rev=None):
        if rev:
            steps = (int) (rev * Motor2.SPR)
        step_delay = max(step_delay, 0.0006) # tested minimum delay of 0.0006
        # step_delay = 0.0208/32

        for x in range(steps):
            GPIO.output(self.STEP_PIN, GPIO.HIGH)
            time.sleep(step_delay)
            GPIO.output(self.STEP_PIN, GPIO.LOW)
            time.sleep(step_delay)
            print("go", x)


    def spin(self, rev, speed, is_cw=True):
        """ Simplified interface """
        self.set_dir(Motor2.CW if is_cw else Motor2.CCW)
        if type(speed) is not int or speed not in (1,2,3,4,5):
            print("Your speed {} is invalid".format(speed))
            speed = 2
        self.go(step_delay=Motor2.delays[speed], rev=rev)
            


    def exit(self):
        GPIO.cleanup()
