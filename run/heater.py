import pigpio
import time

class Heater:
    def __init__(self, pin):
        self.pi = pigpio.pi()
        self.pin = pin
        self.pi.set_mode(self.pin, pigpio.OUTPUT)
        self.pi.write(self.pin, 0)
        self.stop()

    def start(self, duty=125, pulses=11):
        self.pi.set_PWM_dutycycle(self.pin, duty) # 255 is always on, 0 is never on
        self.pi.set_PWM_frequency(self.pin, pulses)

    def stop(self):
        self.pi.set_PWM_dutycycle(self.pin, 0)
        self.pi.set_PWM_frequency(self.pin, 0)
