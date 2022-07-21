import RPi.GPIO as GPIO  # importing files for program
import time
import os
import struct

GPIO.setmode(GPIO.BOARD)  # setup of GPIO pins
GPIO.setup(7, GPIO.OUT)  # setup of motors
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering


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
    GPIO.cleanup()



class Event:

    def __init__(self, button_id, button_type, value, connecting_using_ds4drv):

        self.button_id = button_id
        self.button_type = button_type
        self.value = value
        self.connecting_using_ds4drv = connecting_using_ds4drv

    # L joystick group #


    def L3_event(self):  # L3 has the same mapping on ds4drv as it does when connecting  to bluetooth directly
        return self.button_type == 2 and self.button_id in [1, 0]

    def L3_y_at_rest(self):
        return self.button_id in [1] and self.value == 0

    def L3_x_at_rest(self):
        return self.button_id in [0] and self.value == 0

    def L3_up(self):
        return self.button_id == 1 and self.value < 0

    def L3_down(self):
        return self.button_id == 1 and self.value > 0

    def L3_left(self):
        return self.button_id == 0 and self.value < 0

    def L3_right(self):
        return self.button_id == 0 and self.value > 0

    def L3_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 11 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def L3_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 11 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv

    # R joystick group #
    def R3_event(self):
        if not self.connecting_using_ds4drv:
            return self.button_type == 2 and self.button_id in [4, 3]
        return self.button_type == 2 and self.button_id in [5, 2]

    def R3_y_at_rest(self):
        if not self.connecting_using_ds4drv:
            return self.button_id in [4] and self.value == 0
        return self.button_id in [2] and self.value == 0

    def R3_x_at_rest(self):
        if not self.connecting_using_ds4drv:
            return self.button_id in [3] and self.value == 0
        return self.button_id in [5] and self.value == 0

    def R3_up(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 4 and self.value < 0
        return self.button_id == 5 and self.value < 0

    def R3_down(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 4 and self.value > 0
        return self.button_id == 5 and self.value > 0

    def R3_left(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 3 and self.value < 0
        return self.button_id == 2 and self.value < 0

    def R3_right(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 3 and self.value > 0
        return self.button_id == 2 and self.value > 0

    def R3_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 12 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def R3_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 12 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv

    # Square / Triangle / Circle / X Button group #
    def circle_pressed(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 1

    def circle_released(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 0

    def x_pressed(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 1

    def x_released(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 0

    def triangle_pressed(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 1

    def triangle_released(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 0

    def square_pressed(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 1

    def square_released(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 0

    def options_pressed(self):
        return self.button_id == 9 and self.button_type == 1 and self.value == 1

    def options_released(self):
        return self.button_id == 9 and self.button_type == 1 and self.value == 0

    def share_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 8 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def share_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 8 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv

    # N1 group #
    def L1_pressed(self):
        return self.button_id == 4 and self.button_type == 1 and self.value == 1

    def L1_released(self):
        return self.button_id == 4 and self.button_type == 1 and self.value == 0

    def R1_pressed(self):
        return self.button_id == 5 and self.button_type == 1 and self.value == 1

    def R1_released(self):
        return self.button_id == 5 and self.button_type == 1 and self.value == 0

    # N2 group #
    def L2_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 2 and self.button_type == 2 and (32767 >= self.value >= -32766)
        return self.button_id == 3 and self.button_type == 2 and (32767 >= self.value >= -32766)

    def L2_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 2 and self.button_type == 2 and self.value == -32767
        return self.button_id == 3 and self.button_type == 2 and self.value == -32767

    def R2_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 5 and self.button_type == 2 and (32767 >= self.value >= -32766)
        return self.button_id == 4 and self.button_type == 2 and (32767 >= self.value >= -32766)

    def R2_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 5 and self.button_type == 2 and self.value == -32767
        return self.button_id == 4 and self.button_type == 2 and self.value == -32767

    # up / down arrows #
    def up_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 7 and self.button_type == 2 and self.value == -32767
        return self.button_id == 10 and self.button_type == 2 and self.value == -32767

    def down_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 7 and self.button_type == 2 and self.value == 32767
        return self.button_id == 10 and self.button_type == 2 and self.value == 32767

    def up_down_arrow_released(self):
        # arrow buttons on release are not distinguishable and if you think about it,
        # they are following same principle as the joystick buttons which only have 1
        # state at rest which is shared between left/ right / up /down inputs
        if not self.connecting_using_ds4drv:
            return self.button_id == 7 and self.button_type == 2 and self.value == 0
        return self.button_id == 10 and self.button_type == 2 and self.value == 0

    # left / right arrows #
    def left_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 6 and self.button_type == 2 and self.value == -32767
        return self.button_id == 9 and self.button_type == 2 and self.value == -32767

    def right_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 6 and self.button_type == 2 and self.value == 32767
        return self.button_id == 9 and self.button_type == 2 and self.value == 32767

    def left_right_arrow_released(self):
        # arrow buttons on release are not distinguishable and if you think about it,
        # they are following same principle as the joystick buttons which only have 1
        # state at rest which is shared between left/ right / up /down inputs
        if not self.connecting_using_ds4drv:
            return self.button_id == 6 and self.button_type == 2 and self.value == 0
        return self.button_id == 9 and self.button_type == 2 and self.value == 0

    def playstation_button_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 10 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def playstation_button_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 10 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv



class Actions:

    def __init__(self):
        return

    def on_L1_press(self):
        print("on_L1_press")

    def on_L1_release(self):
        print("on_L1_release")

    def on_L2_press(self, value):
        print("on_L2_press: {}".format(value))

    def on_L2_release(self):
        print("on_L2_release")

    def on_R1_press(self):
        print("on_R1_press")

    def on_R1_release(self):
        print("on_R1_release")

    def on_R2_press(self, value):
        print("on_R2_press: {}".format(value))

    def on_R2_release(self):
        print("on_R2_release")

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
        if event.L1_pressed():
            self.on_L1_press()

        elif event.L1_released():
            self.on_L1_release()

        elif event.L2_pressed():
            self.on_L2_press(value)

        elif event.L2_released():
            self.on_L2_release()

        elif event.R1_pressed():
            self.on_R1_press()

        elif event.R1_released():
            self.on_R1_release()

        elif event.R2_pressed():
            self.on_R2_press(value)

        elif event.R2_released():
            self.on_R2_release()


controller = Controller(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen(timeout=60)


