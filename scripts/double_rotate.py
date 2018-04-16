from time import sleep
import pigpio

DIR1 = 20     # Direction GPIO Pin
STEP1 = 21    # Step GPIO Pin
DIR2 = 26     # Direction GPIO Pin
STEP2 = 19    # Step GPIO Pin

CCW = 0
CW = 1


RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR1, pigpio.OUTPUT)
pi.set_mode(STEP1, pigpio.OUTPUT)

pi.set_mode(DIR2, pigpio.OUTPUT)
pi.set_mode(STEP2, pigpio.OUTPUT)
# Set up input switch

MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Half'][i])

# Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP1, 128)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP1, 500)  # 500 pulses per second

pi.set_PWM_dutycycle(STEP2, 128)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP2, 500)  # 500 pulses per second

try:
    pi.write(DIR1, CW)  # Set direction
    pi.write(DIR2, CCW)  # Set direction
    while True:
        sleep(.1)

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP1, 0)  # PWM off
    pi.set_PWM_dutycycle(STEP2, 0)  # PWM off
    pi.stop()
