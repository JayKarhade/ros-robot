import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

in1 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, False)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    print 'Temp: {0:0.1f} C Humidity: {1:0.1f}%'.format(temperature, humidity)
    if (temperature >=32):
        GPIO.output(in1, True)
        #time.sleep(0.5)
    else:	
        GPIO.output(in1, False)
        #time.sleep(0.5)

GPIO.cleanup()
