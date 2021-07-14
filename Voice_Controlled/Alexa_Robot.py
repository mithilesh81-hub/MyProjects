from flask import Flask
import RPi.GPIO as GPIO
from flask_ask import Ask, statement, question,session
import time
import json
import requests
import unidecode


app = Flask(__name__)
ask = Ask(app,"/Car_Controller")

servoPin1 = 40
servoPin2 = 12
servoPin3 = 38
servoPin4 = 32


    

def jointDown():
 GPIO.setmode(GPIO.BOARD)         
 GPIO.setup(servoPin2, GPIO.OUT)   
 GPIO.output(servoPin2, GPIO.LOW)
 joint = GPIO.PWM(servoPin2, 50)
 joint.start(0)
 joint.ChangeDutyCycle(11.5)
 time.sleep(1)
 joint.stop()
 GPIO.cleanup() 

def jointUp():
 GPIO.setmode(GPIO.BOARD)         
 GPIO.setup(servoPin2, GPIO.OUT)   
 GPIO.output(servoPin2, GPIO.LOW)
 joint = GPIO.PWM(servoPin2, 50)
 joint.start(0)
 joint.ChangeDutyCycle(6)
 time.sleep(1)
 joint.stop()
 GPIO.cleanup()  



   
def teethOpen():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(servoPin4, GPIO.OUT)   
    GPIO.output(servoPin4, GPIO.LOW)
    teeth = GPIO.PWM(servoPin4, 100)  
    teeth.start(4)
    teeth.ChangeDutyCycle(4)
    time.sleep(1)
    teeth.stop()   
    GPIO.cleanup()   

def teethClose():
    print('teeth close')
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(servoPin4, GPIO.OUT)   
    GPIO.output(servoPin4, GPIO.LOW)
    teeth = GPIO.PWM(servoPin4, 100) 
    teeth.start(4)
    teeth.ChangeDutyCycle(17)
    time.sleep(1)
    teeth.stop()   
    GPIO.cleanup()

def Forward():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False)  
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, True)
    

    
def Forward_Fast(duration):
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False)  
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, True)
    time.sleep(duration)
    GPIO.cleanup()
    
    
def Backward():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, True) 
    GPIO.output(11, False)
    GPIO.output(15, True)
    GPIO.output(13, False)
    
def Backward_Fast(duration):
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, True) 
    GPIO.output(11, False)
    GPIO.output(15, True)
    GPIO.output(13, False)
    time.sleep(duration)
    GPIO.cleanup()
    
    
    

        
    

    
    
def Right():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False)  
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, False)
    
def Right_Fast(duration):    
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False)  
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, False)
    time.sleep(duration)
    GPIO.cleanup()
    
    
  
def Rightpivot():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(13, False)
    
def Rightpivot_Fast(duration):
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(13, False)
    time.sleep(duration)
    GPIO.cleanup()
    

       
   
def Left():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(15, False)
    GPIO.output(11, False)
    GPIO.output(13, True)
    
def Left_Fast(duration):
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(15, False)
    GPIO.output(11, False)
    GPIO.output(13, True)
    time.sleep(duration)
    GPIO.cleanup()

def Leftpivot():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, True) 
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(13, True)

def Leftpivot_Fast(duration):
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, True) 
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(13, True)
    time.sleep(duration)
    GPIO.cleanup()
    
def Stop_Motors():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(13, False)
    

    
    
   
    


@app.route('/Car_Controller',methods=['GET', 'POST'])
def Homepage():
    return"HomePage of Robot voice control communication server"
    
@ask.launch
def skill_1():
    print("skill_1")
    mzg1 = "ok"
    return question(mzg1)


    
@ask.intent("ForwardIntent")
def Controlling_the_robot_car_forward():
    forward = "The car has went forward"
    Forward()
    return question("ok")



@ask.intent("ForwardFastIntent")
def Controlling_the_robot_car_forward_Fast():
    forward_fast = "The car has went forward"
    Forward_Fast(0.2)
    return question("ok")

@ask.intent("BackwardIntent")
def Controlling_the_robot_car_backward():
    backward = "The car has went backward"
    Backward()
    return question("ok")

@ask.intent("BackwardFastIntent")
def Controlling_the_robot_car_backward_Fast():
    backward_fast = "The car has went backward"
    Backward_Fast(0.2)
    return question("ok")

@ask.intent("LeftIntent")
def Controlling_the_robot_car_left():
    left = "The car has went left"
    Left()
    return question("ok")

@ask.intent("LeftFastIntent")
def Controlling_the_robot_car_left_Fast():
    left_fast = "The car has went left"
    Left_Fast(0.2)
    return question("ok")

@ask.intent("RightIntent")
def Controlling_the_robot_car_right():
    right = "The car has went right"
    Right()
    return question("ok")

@ask.intent("RightFastIntent")
def Controlling_the_robot_car_right_Fast():
    right_fast = "The car has went right"
    Right_Fast(0.2)
    return question("ok")

@ask.intent("LeftPivotIntent")
def Controlling_the_robot_car_left_pivot():
    left_pivot = "The car has went left"
    Leftpivot()
    return question("ok")

@ask.intent("LeftPivotFastIntent")
def Controlling_the_robot_car_left_pivot_fast():
    left_pivot_fast = "The car has went left"
    Leftpivot_Fast(2)
    return question("ok")

@ask.intent("RightPivotIntent")
def Controlling_the_robot_car_right_pivot():
    right_pivot = "The car has went right"
    Rightpivot()
    return question("ok")

@ask.intent("RightPivotFastIntent")
def Controlling_the_robot_car_right_pivot_fast():
    right_pivot_fast = "The car has went right"
    Rightpivot_Fast(2)
    return question("ok")

@ask.intent("StopIntent")
def Controlling_the_robot_car_stop():
    stop = "The car has stopped"
    Stop_Motors()
    return question("ok")

@ask.intent("JointUpIntent")
def Controlling_the_robot_joint_up():
    jointup = "The arm has moved to up position"
    jointUp()
    return question("ok")

@ask.intent("JointDownIntent")
def Controlling_the_robot_joint_down():
    jointdown = "The arm has moved to down position"
    jointDown()
    return question("ok")

@ask.intent("TeethOpenIntent")
def Controlling_the_robot_teeth_open():
    teethopen = "The arm has opened the grip"
    teethOpen()
    return question("ok")

@ask.intent("TeethCloseIntent")
def Controlling_the_robot_teeth_close():
    teethclose = "The arm has closed the grip"
    teethClose()
    return question("ok")


@ask.intent("AMAZON.StopIntent")
def Amazon_Stop():
    stop = "The car has stopped"
    Stop_Motors()
    return question("ok")

if __name__ == '__main__':
    app.run(debug=True, host='localhost')


