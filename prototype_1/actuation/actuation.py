#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO     #MS1 and MS2 HIGH
import time

DIR1 = 20  # Direction GPIO Pin        #left side(Stepper motor 1 and motor 3)
STEP1 = 7  # Step GPIO Pin             #right side(Stepper motor 2 and motor 4)
DIR2 = 21  # Direction GPIO Pin
STEP2 = 11  # Step GPIO Pin
DIR3 = 23  # Direction GPIO Pin
STEP3 = 13  # Step GPIO Pin
DIR4 = 24  # Direction GPIO Pin
STEP4 = 15  # Step GPIO Pin

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 10


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

delay = 0.0001
step_count = SPR
int i = 0
def backward():
	while i<400:#Backward
	    GPIO.output(DIR1, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP1, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP1, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR2, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP2, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP2, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR3, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP3, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP3, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR4, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP4, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP4, GPIO.LOW)
        	time.sleep(delay)
        i = i+1

def forward():
	while i<400:#Forward
	    GPIO.output(DIR1, CW)
	    for x in range(step_count):
	        GPIO.output(STEP1, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP1, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR2, CW)
	    for x in range(step_count):
	        GPIO.output(STEP2, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP2, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR3, CW)
	    for x in range(step_count):
	        GPIO.output(STEP3, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP3, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR4, CW)
	    for x in range(step_count):
	        GPIO.output(STEP4, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP4, GPIO.LOW)
	        time.sleep(delay)
	    i =i+1

def right():
	while i<400:#Right
	    GPIO.output(DIR1, CW)
	    for x in range(step_count):
	        GPIO.output(STEP1, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP1, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR2, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP2, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP2, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR3, CW)
	    for x in range(step_count):
	        GPIO.output(STEP3, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP3, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR4, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP4, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP4, GPIO.LOW)
        	time.sleep(delay)
        i = i+1

def left():
	while i<400:#Left
	    GPIO.output(DIR1, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP1, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP1, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR2, CW)
	    for x in range(step_count):
	        GPIO.output(STEP2, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP2, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR3, CCW)
	    for x in range(step_count):
	        GPIO.output(STEP3, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP3, GPIO.LOW)
	        time.sleep(delay)
	
	    GPIO.output(DIR4, CW)
	    for x in range(step_count):
	        GPIO.output(STEP4, GPIO.HIGH)
	        time.sleep(delay)
	        GPIO.output(STEP4, GPIO.LOW)
        	time.sleep(delay)
        i = i+1

def CommandCallback(commandMessage):
    command = commandMessage.data
    print(command)
    if command == "\"move_forward\"":
        print('Moving forward')
        forward()
        i=0
    elif command == "\"move_backward\"":
        print('Moving backward')
        backward()
        i=0
    elif command == "\"move_left\"":
    	print('Moving left')
    	left()
    	i=0
    elif command == "\"move_right\"":
        print('moving right')
        right()        
        i=0
        
def listener():
	rospy.init_node('Actuator',anonymous=True)
	rospy.Subscriber('movement_cmd', String, CommandCallback)
	rospy.spin()
print('Shutting down : Stopping motors')

GPIO.cleanup()

if __name__ == '__main__':
	listener()
