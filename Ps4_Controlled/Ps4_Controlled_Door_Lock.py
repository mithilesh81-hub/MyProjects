import RPi.GPIO as GPIO  # importing files for program
import time
import os
import struct

OFFSE_DUTY = 0.5        
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    

servoPin = 40
GPIO.setmode(GPIO.BOARD)         
GPIO.setup(servoPin, GPIO.OUT)   
GPIO.output(servoPin, GPIO.LOW)

def opendoorlock():
  p = GPIO.PWM(servoPin, 50)     
  p.start(0)                     
  p.ChangeDutyCycle(2)
  time.sleep(1)
    

def closedoorlock():
  p = GPIO.PWM(servoPin, 50)     
  p.start(0)                     
  p.ChangeDutyCycle(11)
  time.sleep(1)
 
 
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

    def square_pressed(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 1

    def square_released(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 0



class Actions:

    def __init__(self):
        return

    def on_circle_press(self):
        print("on_circle_press")
        opendoorlock()  

    def on_circle_release(self):
        print("on_circle_release")
    
    def on_square_press(self):
        print("on_square_press")
        closedoorlock()

    def on_square_release(self):
        print("on_square_release")


class Controller(Actions):

    def __init__(
            self, interface, connecting_using_ds4drv=True,
            event_definition=None, event_format=None
    ):
        """
        Initiate controller instance that is capable of listening to all events on specified input interface
        :param interface: STRING aka /dev/input/js0 or any other PS4 Duelshock controller interface.
                          You can see all available interfaces with a command "ls -la /dev/input/"
        :param connecting_using_ds4drv: BOOLEAN. If you are connecting your controller using ds4drv, then leave it set
                                                 to True. Otherwise if you are connecting directly via directly via
                                                 bluetooth/bluetoothctl, set it to False otherwise the controller
                                                 button mapping will be off.
        """
        Actions.__init__(self)
        self.stop = False
        self.is_connected = False
        self.interface = interface
        self.connecting_using_ds4drv = connecting_using_ds4drv
        self.debug = False  # If you want to see raw event stream, set this to True.
        self.black_listed_buttons = []  # set a list of blocked buttons if you dont want to process their events
        if self.connecting_using_ds4drv and event_definition is None:
            # when device is connected via ds4drv its sending hundreds of events for those button IDs
            # thus they are blacklisted by default. Feel free to adjust this list to your linking when sub-classing
            self.black_listed_buttons += [6, 7, 8, 11, 12, 13]
        self.event_definition = event_definition if event_definition else Event
        self.event_format = event_format if event_format else "LhBB"
        self.event_size = struct.calcsize(self.event_format)

    def listen(self, timeout=30, on_connect=None, on_disconnect=None):
        """
        Start listening for events on a given self.interface
        :param timeout: INT, seconds. How long you want to wait for the self.interface.
                        This allows you to start listening and connect your controller after the fact.
                        If self.interface does not become available in N seconds, the script will exit with exit code 1.
        :param on_connect: function object, allows to register a call back when connection is established
        :param on_disconnect: function object, allows to register a call back when connection is lost
        :return: None
        """

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

        elif event.square_pressed():
            self.on_square_press()
        elif event.square_released():
            self.on_square_release()



controller = Controller(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen(timeout=60)


 