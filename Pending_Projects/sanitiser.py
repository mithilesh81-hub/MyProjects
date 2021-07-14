#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time




OFFSE_DUTY = 0.5        
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    

servoPin = 3
servoPin2 = 5 
GPIO.setmode(GPIO.BOARD)         
GPIO.setup(servoPin, GPIO.OUT)   
GPIO.output(servoPin, GPIO.LOW)
GPIO.setup(servoPin2, GPIO.OUT)   
GPIO.output(servoPin2, GPIO.LOW)




def openbin():
  p = GPIO.PWM(servoPin, 50)
  x = GPIO.PWM(servoPin2, 50)     

  p.start(0)                     
  p.ChangeDutyCycle(12)
  x.start(0)                     
  x.ChangeDutyCycle(12)
  
  time.sleep(1)
  
    

openbin()


    

