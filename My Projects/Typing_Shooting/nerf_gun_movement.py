import time
import RPi.GPIO as GPIO


servoPin_x = 40
servoPin_y = 38
servoPin_shoot = 37



class Shooting:
    
    def setup(self):
        
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(servoPin_x, GPIO.OUT)
        GPIO.output(servoPin_x, GPIO.LOW)

        GPIO.setup(servoPin_y, GPIO.OUT)
        GPIO.output(servoPin_y, GPIO.LOW)


        GPIO.setup(servoPin_shoot, GPIO.OUT)
        GPIO.output(servoPin_shoot, GPIO.LOW)





    def y_change(self,change):
                y = GPIO.PWM(servoPin_y, 50)

                y.start(0)
                y.ChangeDutyCycle(change)
                time.sleep(1)
                
    def x_change(self,change):
                x = GPIO.PWM(servoPin_x, 50)
                x.start(0)
                x.ChangeDutyCycle(change)
                time.sleep(1)

    def shoot(self):
                s = GPIO.PWM(servoPin_shoot, 50)

                s.start(0)
                s.ChangeDutyCycle(4)
                time.sleep(1)
                s.ChangeDutyCycle(6)
                time.sleep(1)

                  
    def reset(self):
            self.x_change(2)
            self.y_change(7)
                
    def gotomirrorandshoot(self):
        self.x_change(4)
        self.y_change(10)
        self.shoot()
        self.reset()
        GPIO.cleanup()

    def gotomomphotoandshoot(self):
        self.x_change(4.18)
        self.y_change(9)
        self.shoot()
        self.reset()
        GPIO.cleanup()

    def gotoUmbccellaandshoot(self):
        self.x_change(4.7)
        self.y_change(10)
        self.shoot()
        self.reset()
        GPIO.cleanup()
        
    def shoot_laptop(self):
        self.x_change(3.5)
        self.y_change(9.5)
        self.shoot()
        self.reset()
        GPIO.cleanup()


if __name__ == "__main__":
    shooting = Shooting()
    shooting.setup()
    shooting.shoot_laptop()







