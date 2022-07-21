import RPi.GPIO as GPIO
import time


servoPin= 37


GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.output(servoPin, GPIO.LOW)



def leftwing():
    p = GPIO.PWM(servoPin,50)
    p.start(0)
    p.ChangeDutyCycle(6)
    time.sleep(1)


leftwing()