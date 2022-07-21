import RPi.GPIO as GPIO # importing files for program
import os
import struct
import time

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
    
class Event:

    def __init__(self, button_id, button_type, value, connecting_using_ds4drv):

        self.button_id = button_id
        self.button_type = button_type
        self.value = value
        self.connecting_using_ds4drv = connecting_using_ds4drv

    def circle_pressed(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 1

    def circle_released(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 0

    
    def x_pressed(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 1

    def x_released(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 0

    
    def triangle_pressed(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 1

    def triangle_released(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 0

    
    def square_pressed(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 1

    def square_released(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 0



class Actions:
   
    def __init__(self):
        return

    def on_x_press(self):
        print("on_x_press")
        jointDown()

    def on_x_release(self):
        print("on_x_release")

    def on_triangle_press(self):
        print("on_triangle_press")
        jointUp()

    def on_triangle_release(self):
        print("on_triangle_release")

    def on_circle_press(self):
        print("on_circle_press")
        teethClose()

    def on_circle_release(self):
        print("on_circle_release")

    def on_square_press(self):
        print("on_square_press")
        teethOpen()

    def on_square_release(self):
        print("on_square_release")

    
class Controller(Actions):

    def __init__(self, interface, connecting_using_ds4drv=True,event_definition=None, event_format=None):
                
        Actions.__init__(self)
        self.stop = False
        self.is_connected = False
        self.interface = interface
        self.connecting_using_ds4drv = connecting_using_ds4drv
        self.debug = False  
        self.black_listed_buttons = []  
        if self.connecting_using_ds4drv and event_definition is None:
            
            self.black_listed_buttons += [6, 7, 8, 11, 12, 13]
        self.event_definition = event_definition if event_definition else Event
        self.event_format = event_format if event_format else "LhBB"
        self.event_size = struct.calcsize(self.event_format)

    def listen(self, timeout=30, on_connect=None, on_disconnect=None):
        
        def on_disconnect_callback():
            self.is_connected = False
            if on_disconnect is not None:
                on_disconnect()

        def on_connect_callback():
            self.is_connected = True
            if on_connect is not None:
                on_connect()

        def wait_for_interface():
            print("Waiting for interface: {} to become available . . .".format(self.interface))
            for i in range(timeout):
                if os.path.exists(self.interface):
                    print("Successfully bound to: {}.".format(self.interface))
                    on_connect_callback()
                    return
                time.sleep(1)
            print("Timeout({} sec). Interface not available.".format(timeout))
            exit(1)

        def read_events():
            try:
                return _file.read(self.event_size)
            except IOError:
                print("Interface lost. Device disconnected?")
                on_disconnect_callback()
                exit(1)

        wait_for_interface()
        try:
            _file = open(self.interface, "rb")
            event = read_events()
            while not self.stop and event:
                (*tv_sec, value, button_type, button_id) = struct.unpack(self.event_format, event)
                if self.debug:
                    print("button_id: {} button_type: {} value: {}".format(button_id, button_type, value))
                if button_id not in self.black_listed_buttons:
                    self.__handle_event(button_id=button_id, button_type=button_type, value=value)
                event = read_events()
        except KeyboardInterrupt:
            print("\nExiting (Ctrl + C)")
            on_disconnect_callback()
            exit(1)

    def __handle_event(self, button_id, button_type, value):

        event = self.event_definition(button_id=button_id,
                                      button_type=button_type,
                                      value=value,
                                      connecting_using_ds4drv=self.connecting_using_ds4drv)

      
        
        if event.circle_pressed():
            self.on_circle_press()
        elif event.circle_released():
            self.on_circle_release()
        elif event.x_pressed():
            self.on_x_press()
        elif event.x_released():
            self.on_x_release()
        elif event.triangle_pressed():
            self.on_triangle_press()
        elif event.triangle_released():
            self.on_triangle_release()
        elif event.square_pressed():
            self.on_square_press()
        elif event.square_released():
            self.on_square_release()



        

            

controller = Controller(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen(timeout=60) 