import RPi.GPIO as GPIO
import time
import projecter_On as po
from nerf_gun_movement import Shooting

servoPin_D = 5
servoPin_E = 3
servoPin_C = 7
servoPin_1 = 8
servoPin_ENTER = 10
button_press_SHIFT = 11
servoPin_ALT = 12
servoPin_TAB = 13
button_press_V = 15
button_press_CTRL = 16
button_press_LEFT = 18
button_press_DOWN= 19


class initiate_key_class:
 
 def initiate_key(self,key):
    
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(servoPin_D, GPIO.OUT)
    GPIO.output(servoPin_D, GPIO.LOW)

    GPIO.setup(servoPin_E, GPIO.OUT)
    GPIO.output(servoPin_E, GPIO.LOW)

    GPIO.setup(servoPin_C, GPIO.OUT)
    GPIO.output(servoPin_C, GPIO.LOW)

    GPIO.setup(servoPin_1, GPIO.OUT)
    GPIO.output(servoPin_1, GPIO.LOW)

    GPIO.setup(servoPin_TAB, GPIO.OUT)
    GPIO.output(servoPin_TAB, GPIO.LOW)


    GPIO.setup(servoPin_ALT, GPIO.OUT)
    GPIO.output(servoPin_ALT, GPIO.LOW)

    GPIO.setup(servoPin_ENTER, GPIO.OUT)
    GPIO.output(servoPin_ENTER, GPIO.LOW)


    GPIO.setup(button_press_SHIFT, GPIO.OUT)
    GPIO.output(button_press_SHIFT, GPIO.LOW)
                                    
    GPIO.setup(button_press_V, GPIO.OUT)
    GPIO.output(button_press_V, GPIO.LOW)

    GPIO.setup(button_press_CTRL, GPIO.OUT)
    GPIO.output(button_press_CTRL, GPIO.LOW)

    GPIO.setup(button_press_LEFT, GPIO.OUT)
    GPIO.output(button_press_LEFT, GPIO.LOW)

    GPIO.setup(button_press_DOWN, GPIO.OUT)
    GPIO.output(button_press_DOWN, GPIO.LOW)
    if key == 'd':
      button_press_d()
    
    if key == 'e':
      button_press_e()
    
    elif key == 'c':
      button_press_c()
    
    elif key == '1':
      button_press_1()
    
    elif key == 'tab':
      button_press_tab()
    
    elif key == 'alt':
      button_press_alt()
    
    elif key == 'enter':
      button_press_enter()
    
    elif key == 'shift':
      button_press_shift()
    
    elif key == 'v':
      button_press_v()
    
    
    elif key == 'ctrl':
      button_press_ctrl()
    
    elif key == 'left':
      button_press_left()
    
    elif key == 'down':
      button_press_down()
    
    elif key == 'projecter':
      print('in projecter')  
      projecter()
    
    elif key == 'turnoffprojecter':
      print('In turn off projecter')
      turnoffprojecter()
    
    elif key == 'shoot':
      print('In Shoot Key')
      shooting = Shooting()
      shooting.setup()
      shooting.shoot_laptop()
      
    elif key == 'unlock':
      print('In unlock')
      password()
     

def button_press_d():
        y = GPIO.PWM(servoPin_D, 50)
        y.start(0)
        y.ChangeDutyCycle(9)
        time.sleep(0.40)
        y.ChangeDutyCycle(2)
        time.sleep(0.5)

       
def button_press_e():
        y = GPIO.PWM(servoPin_E, 50)
        y.start(0)
        y.ChangeDutyCycle(2.5)
        time.sleep(0.4)
        y.ChangeDutyCycle(8)
        time.sleep(0.5)


def button_press_c():
        y = GPIO.PWM(servoPin_C, 50)
        y.start(0)
        y.ChangeDutyCycle(10.8)
        time.sleep(0.45)
        y.ChangeDutyCycle(5)
        time.sleep(0.5)

def button_press_1():
        y = GPIO.PWM(servoPin_1, 50)
        y.start(0)

        y.ChangeDutyCycle(2)
        time.sleep(0.5)
        y.ChangeDutyCycle(9)
        time.sleep(1)
        
def button_press_tab():
        y = GPIO.PWM(servoPin_TAB, 50)
        y.start(0)

        y.ChangeDutyCycle(9)
        time.sleep(0.5)
        y.ChangeDutyCycle(2)
        time.sleep(0.5)

def button_press_alt():
        y = GPIO.PWM(servoPin_ALT, 50)
        y.start(0)
        y.ChangeDutyCycle(8.7)
        time.sleep(0.5)
        y.ChangeDutyCycle(3)
        time.sleep(1)


def button_press_enter():
        y = GPIO.PWM(servoPin_ENTER, 50)
        y.start(0)
        y.ChangeDutyCycle(3)
        time.sleep(0.5)
        y.ChangeDutyCycle(9)
        time.sleep(0.5)
        
def button_press_shift():
        y = GPIO.PWM(button_press_SHIFT, 50)
        y.start(0)
        y.ChangeDutyCycle(10.8)
        time.sleep(0.5)
        y.ChangeDutyCycle(6)
        time.sleep(0.5)
        
def button_press_v():
        y = GPIO.PWM(button_press_V, 50)
        y.start(0)
        y.ChangeDutyCycle(6)
        time.sleep(0.4)
        y.ChangeDutyCycle(12)
        time.sleep(1)

def button_press_ctrl():
        y = GPIO.PWM(button_press_CTRL, 50)
        y.start(0)
        y.ChangeDutyCycle(6)
        time.sleep(0.5)
        y.ChangeDutyCycle(12)
        time.sleep(0.5)        
        
def button_press_left():
        y = GPIO.PWM(button_press_LEFT, 50)
        y.start(0)
        y.ChangeDutyCycle(6)
        time.sleep(0.5)
        y.ChangeDutyCycle(12)
        time.sleep(0.5)                 

def button_press_down():
        y = GPIO.PWM(button_press_DOWN, 50)
        y.start(0)
        y.ChangeDutyCycle(2)
        time.sleep(1)
        y.ChangeDutyCycle(7)
        time.sleep(0.5)
        
def projecter():
    po.setup_projecter()
#     for i in range(7):
#        button_press_tab()
#     button_press_enter()
    
def turnoffprojecter():
    button_press_off_on()

def shoot_Key():
    shoot = shoot_script.Shoot()
    shoot.button_press_Shoot()
    GPIO.cleanup()
    
def password():

    button_press_ctrl()
    time.sleep(2)
    button_press_d()
    button_press_e()
    button_press_c()
    button_press_1()
    button_press_v()
    button_press_enter()
    GPIO.cleanup()

if __name__=='__main__':
    
    button_press_d()
    button_press_e()
    button_press_c()
    button_press_v()
    button_press_1()
    button_press_tab()
    button_press_alt()
    button_press_enter()
    button_press_shift()
    button_press_ctrl()
    button_press_left()
    button_press_down()
    GPIO.cleanup()
