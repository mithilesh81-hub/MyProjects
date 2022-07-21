import RPi.GPIO as GPIO
import time

OFFSE_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSE_DUTY
SERVO_MAX_DUTY = 12.5 + OFFSE_DUTY

servoPin = 8
inputvoltage = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputvoltage, GPIO.IN)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.output(servoPin, GPIO.LOW)

class Computer:


    Value = True
    def Turn_On(self):
        print('hello')
        x = GPIO.PWM(servoPin, 50)
        x.start(0)
        x.ChangeDutyCycle(2)
        time.sleep(1)
        x.ChangeDutyCycle(6)
        time.sleep(1)
        self.Value = False
        
    def Turn_Off(self):
        x = GPIO.PWM(servoPin, 50)
        x.start(0)
        x.ChangeDutyCycle(2)
        time.sleep(1)
        x.ChangeDutyCycle(6)
        time.sleep(1)
        self.Value = True    
    
x = Computer()
while True:
 if GPIO.input(inputvoltage):
   
   if x.Value == True:
     print('in if')   
     x.Turn_On()
     
     
 else:
  print(x.Value)
  if x.Value == False:
      print('else block')
      x.Turn_Off()
