import time
import pigpio



class ContactSwitch:
    def __init__(self, pin, callback=None, bounce_ms=200):
        self.pin = pin 
        pi = pigpio.pi() 
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
        self.last_activation = time.time()


        def bounce_wrapper_callback(gpio, level, tick):
            
            print( time.time() - self.last_activation)
            if bounce_ms < time.time() - self.last_activation:
                print("i'm in")
                self.last_activation = time.time()
                if callback:
                    callback(gpio, level, tick)
            # print(gpio, level, tick)
        
        pi.callback(pin, pigpio.EITHER_EDGE, bounce_wrapper_callback)

        # while True:
            # time.sleep(0.2)
            # input_state = pi.read(pin)
            # if input_state == 1:
                # print('Button Pressed')
                # time.sleep(0.2)

c = ContactSwitch(20)
while True:
    time.sleep(0.2)
