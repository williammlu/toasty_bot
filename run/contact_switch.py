import time
import pigpio



class ContactSwitch:
    def __init__(self, pin, callback=None, bounce_ms=0.1):
        self.pin = pin 
        pi = pigpio.pi() 
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
        self.last_activation = time.time()
        self.callback = callback


        def bounce_wrapper_callback(gpio, level, tick):
            if bounce_ms < time.time() - self.last_activation:
                self.last_activation = time.time()
                print("calling callback") 
                if self.callback:
                    self.callback(gpio, level, tick)
        
        pi.callback(pin, pigpio.RISING_EDGE, bounce_wrapper_callback)
    
    def is_pressed(self):
        pi = pigpio.pi()
        return pi.read(pin)

# c = ContactSwitch(20)
# while True:
    # time.sleep(0.2)
