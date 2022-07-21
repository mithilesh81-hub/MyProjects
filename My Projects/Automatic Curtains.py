#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO  # importing files for program
import time
import json
import unidecode


servoPin = 3
servoPin2 = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.output(servoPin, GPIO.LOW)
GPIO.setup(servoPin2, GPIO.OUT)
GPIO.output(servoPin2, GPIO.LOW)


def Open_Curtain():
    
    p = GPIO.PWM(servoPin, 50)
    p.start(0)

    p.ChangeDutyCycle(8)
    time.sleep(2)
    p.ChangeDutyCycle(2)
    time.sleep(1)

    
 

def Close_Curtain():
    x = GPIO.PWM(servoPin2, 50)
    x.start(0)
    
    x.ChangeDutyCycle(2)
    time.sleep(2)
    x.ChangeDutyCycle(6)
    time.sleep(1)
    
    

Close_Curtain()





