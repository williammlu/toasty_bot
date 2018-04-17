from motor import Motor
import pigpio
import time

pi = pigpio.pi()
m2 = Motor(26,19, pi)
m1 = Motor(13,06, pi)

for k in range(30):
    m1.spin(0.25,4,True)
    time.sleep(1)
    m1.spin(0.25,4,False)
    time.sleep(1)
    m2.spin(0.25,4,True)
    time.sleep(1)
    m2.spin(0.25,4,False)
    time.sleep(1)
    print("cycle", k)

m2.pi_stop()




