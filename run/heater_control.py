import Adafruit_MAX31855.MAX31855 as MAX31855
import time
CLK = 14
CS  = 15
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)


print 'Press Ctrl-C to quit.'
while True:
	temp = sensor.readTempC()
	internal = sensor.readInternalC()
	print('Thermocouple Temperature: {0:0.3F} *C'.format(temp))
	print ('Internal Temperature: {0:0.3F}*C'.format(internal))
	time.sleep(1.0)
