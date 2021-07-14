from flask import Flask,request,render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)  # setup of GPIO pins

GPIO.setup(7, GPIO.OUT)  # setup of motors
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


servoPin1 = 40
servoPin2 = 12
servoPin3 = 38
servoPin4 = 32


    
def clockwise():
 print("Clockwise")   
 GPIO.setmode(GPIO.BOARD)         
 GPIO.setup(servoPin1, GPIO.OUT)   
 GPIO.output(servoPin1, GPIO.LOW)
 base = GPIO.PWM(servoPin1, 50)
 base.start(0)
 base.ChangeDutyCycle(2)
 time.sleep(0.75)
 base.stop()
 GPIO.cleanup()
 
def Mid():
 GPIO.setmode(GPIO.BOARD)         
 GPIO.setup(servoPin1, GPIO.OUT)   
 GPIO.output(servoPin1, GPIO.LOW)
 base = GPIO.PWM(servoPin1, 50)
 base.start(0)
 base.ChangeDutyCycle(7)
 time.sleep(0.75)
 base.stop()
 GPIO.cleanup() 


def anticlockwise():
 GPIO.setmode(GPIO.BOARD)         
 GPIO.setup(servoPin1, GPIO.OUT)   
 GPIO.output(servoPin1, GPIO.LOW)
 base = GPIO.PWM(servoPin1, 50)
 base.start(0)
 base.ChangeDutyCycle(12)
 time.sleep(0.75)
 base.stop()
 GPIO.cleanup()


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


def neckDown():
   GPIO.setmode(GPIO.BOARD)         
   GPIO.setup(servoPin3, GPIO.OUT)   
   GPIO.output(servoPin3, GPIO.LOW)
   neck = GPIO.PWM(servoPin3, 50)
   neck.start(0)
   x = 7
   while x > 4:
    neck.ChangeDutyCycle(x)
    time.sleep(0.0025)
    x = x-0.025
   neck.stop()
   GPIO.cleanup()
 
   

def neckUp():
   GPIO.setmode(GPIO.BOARD)         
   GPIO.setup(servoPin3, GPIO.OUT)   
   GPIO.output(servoPin3, GPIO.LOW)
   neck = GPIO.PWM(servoPin3, 50)
   neck.start(0)
   x = 4
   while x < 9:
    neck.ChangeDutyCycle(x)
    time.sleep(0.0025)
    x = x+0.025
   neck.stop()
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
    

def forward():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False)  
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, True)
    
def backward():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, True) 
    GPIO.output(11, False)
    GPIO.output(15, True)
    GPIO.output(13, False)    
    
   
def left():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(15, False)
    GPIO.output(11, False)
    GPIO.output(13, True)

    
    
def right():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False)  
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, False)
   
def leftpivot():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, True) 
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(13, True)
    
def rightpivot():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(7, GPIO.OUT)    
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.output(7, False) 
    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(13, False)
    
    
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
    




@app.route('/')
def Welcome():
 return render_template('Robot_Control.html')

@app.route('/Robot_Arm', methods=['GET', 'POST'])
def Robot_Arm():
 
 Stop=request.form.get("destroy")
 print(Stop)
 if Stop == "Stop":
  Stop_Motors()
 
 
 Turn_Clockwise=request.form.get("clockwise")
 print(Turn_Clockwise)
 if Turn_Clockwise == "Turn_Clockwise":
  clockwise()
  
 Turn_Mid=request.form.get("mid")
 print(Turn_Mid)
 if Turn_Mid == "Turn_Mid":
  Mid() 
    
 
 AntiClockwise=request.form.get("anticlockwise")
 print(AntiClockwise)
 if AntiClockwise == "Turn_Anticlockwise":
   anticlockwise()   


 joint_down=request.form.get("joint_down")
 print(joint_down)
 if joint_down == "Joint_Down":
   jointDown()   

 
 joint_up=request.form.get("joint_up")
 print(joint_up)
 if joint_up == "Joint_Up":
   jointUp()   

 up_neck=request.form.get("up_neck")
 print(up_neck)
 if up_neck == "Neck_Up":
   neckUp()
   
 down_neck=request.form.get("down_neck")
 print(down_neck)
 if down_neck == "Neck_Down":
   neckDown()
   
 open_teeth=request.form.get("open_teeth")
 print(open_teeth)
 if open_teeth == "Open_Grip":
   teethOpen()
   
 close_teeth=request.form.get("close_teeth")
 print(close_teeth)
 if close_teeth == "Close_Grip":
   teethClose()

   
   
 return render_template('Robot_Arm.html')

@app.route('/Car_Control', methods=['GET', 'POST'])
def Car_Control():
    
 print("In Car Control")  
 selected_forward=request.form.get('forward')
 print(selected_forward)
 if (selected_forward == '1'):
     forward()
 
     
    
 selected_backward=request.form.get('backward')
 print(selected_backward)
 if (selected_backward == '2'):
     backward()
 
   
  
 selected_left=request.form.get('left')
 print(selected_left)
 if  (selected_left == '4'):
      left()
 
  
 selected_right=request.form.get('right')
 print(selected_right)
 if (selected_right == '3'):
     right()
 
  
 selected_Stop_Motors=request.form.get('Stop_Motors')  
 if (selected_Stop_Motors == '5'):
     Stop_Motors()
     
 selected_rightpivot=request.form.get('rightpivot')
 print(selected_rightpivot) 

 if (selected_rightpivot == '6'):
     rightpivot()
     
 selected_leftpivot=request.form.get('leftpivot')
 print(selected_leftpivot) 

 if (selected_leftpivot == '7'):
     leftpivot()
     
      
 
   
 return render_template('Robot_Control.html')
 




if __name__ == '__main__':
    app.run(debug=True, host='localhost')