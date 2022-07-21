#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

servoPin1 = 7
servoPin2 = 13



OFFSE_DUTY = 0.5        
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    

GPIO.setmode(GPIO.BOARD)         
GPIO.setup(servoPin1, GPIO.OUT)   
GPIO.output(servoPin1, GPIO.LOW)
GPIO.setup(servoPin2, GPIO.OUT)   
GPIO.output(servoPin2, GPIO.LOW)






def Fan_Switch_ON():
  p = GPIO.PWM(servoPin1, 50)
  
  p.start(0)
  p.ChangeDutyCycle(2)
  time.sleep(1)
  
def Fan_Switch_OFF():
  p = GPIO.PWM(servoPin1, 50)
  
  p.start(0)
  p.ChangeDutyCycle(7)
  time.sleep(1)  
  

def Light_Switch_ON():
  p = GPIO.PWM(servoPin2, 50)
  
  p.start(0)
  p.ChangeDutyCycle(2)
  time.sleep(1)  

def Light_Switch_OFF():
  p = GPIO.PWM(servoPin2, 50)
  
  p.start(0)
  p.ChangeDutyCycle(6)
  time.sleep(1)
  

 
Light_Switch_ON()


    
    

    


