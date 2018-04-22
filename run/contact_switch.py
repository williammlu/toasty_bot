import time
import pigpio



class ContactSwitch:
    def __init__(self, pin, callback=None, bounce_ms=0.1):
        self.pin = pin 
        pi = pigpio.pi() 
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
        self.last_activation = time.time()


        def bounce_wrapper_callback(gpio, level, tick):
            if bounce_ms < time.time() - self.last_activation:
                self.last_activation = time.time()
                print("calling callback") 
                if callback:
                    callback(gpio, level, tick)
        
        pi.callback(pin, pigpio.EITHER_EDGE, bounce_wrapper_callback)

c = ContactSwitch(20)
while True:
    time.sleep(0.2)
