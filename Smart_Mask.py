#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

servoPin1 = 11
servoPin2 = 40
trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # calculate timeout according to the maximum measuring distance

OFFSE_DUTY = 0.5        
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    

GPIO.setmode(GPIO.BOARD)         
GPIO.setup(servoPin1, GPIO.OUT)   
GPIO.output(servoPin1, GPIO.LOW)
GPIO.setup(servoPin2, GPIO.OUT)   
GPIO.output(servoPin2, GPIO.LOW)
GPIO.setup(trigPin, GPIO.OUT)   # set trigPin to OUTPUT mode
GPIO.setup(echoPin, GPIO.IN)    # set echoPin to INPUT mode






def maskdown():
  p = GPIO.PWM(servoPin1, 50)
  p2 = GPIO.PWM(servoPin2, 50) 
  
  p.start(0)
  p2.start(0)
  
  p.ChangeDutyCycle(7)
  p2.ChangeDutyCycle(8)
  
  time.sleep(0.5)
  

def maskup():
  p = GPIO.PWM(servoPin1, 50)
  p2 = GPIO.PWM(servoPin2, 50) 
  
  p.start(0)
  p2.start(0)
  
  p.ChangeDutyCycle(5)
  p2.ChangeDutyCycle(10)
  
  time.sleep(0.5)




def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     # get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      # make trigPin output 10us HIGH level 
    time.sleep(0.00001)     # 10us
    GPIO.output(trigPin,GPIO.LOW) # make trigPin output LOW level 
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # calculate distance with sound speed 340m/s 
    return distance
    



def loop():
    while(True):
        distance = getSonar() # get distance
        print ("The distance is : %.2f cm"%(distance))
        if distance<60: 
          print("maskup")
          maskup()
        else:
          print('maskdown')
          maskdown()
        time.sleep(1)
        
        
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        GPIO.cleanup()         # release GPIO resource


    
    

    

