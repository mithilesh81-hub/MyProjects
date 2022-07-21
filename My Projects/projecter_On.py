import RPi.GPIO as GPIO
import time

OFFSE_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSE_DUTY
SERVO_MAX_DUTY = 12.5 + OFFSE_DUTY

servoPin_On_Source = 5
servoPin_Right = 7
servoPin_Ok = 11



GPIO.setmode(GPIO.BOARD)

GPIO.setup(servoPin_On_Source, GPIO.OUT)
GPIO.output(servoPin_On_Source, GPIO.LOW)

GPIO.setup(servoPin_Right, GPIO.OUT)
GPIO.output(servoPin_Right, GPIO.LOW)

GPIO.setup(servoPin_Ok, GPIO.OUT)
GPIO.output(servoPin_Ok, GPIO.LOW)


def button_press_off_on():
        y = GPIO.PWM(servoPin_On_Source, 50)
        y.start(0)
        y.ChangeDutyCycle(2.6)
        time.sleep(3)
        y.ChangeDutyCycle(3)
        time.sleep(1)

def button_press_source():
        y = GPIO.PWM(servoPin_On_Source, 50)
        y.start(0)
        y.ChangeDutyCycle(3.7)
        time.sleep(3)
        y.ChangeDutyCycle(3)
        time.sleep(1)
    
def right_button():
        y = GPIO.PWM(servoPin_Right, 50)
        y.start(0)
        y.ChangeDutyCycle(2.5)
        time.sleep(0.25)
        y.ChangeDutyCycle(4)
        time.sleep(1)

def Ok_button():
        y = GPIO.PWM(servoPin_Ok, 50)
        y.start(0)
        y.ChangeDutyCycle(11.5)
        time.sleep(1)
        y.ChangeDutyCycle(11)
        time.sleep(1)


def setup_projecter():
    button_press_off_on()
    time.sleep(7)
    button_press_source()
    for i in range(2):
        right_button()
    Ok_button()
    
if __name__== '__main__':
    setup_projecter()
    button_press_off_on()
