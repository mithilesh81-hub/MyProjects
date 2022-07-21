import RPi.GPIO as GPIO
import time
import requests as req



inputvoltage = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputvoltage, GPIO.IN)

url = 'http://192.168.0.228:5000/user/InitiateRock'


class InitiateRockAssistant:
    Value = True
    requests = 0
    
    def Turn_On(self):
        print('Turned On')
        self.Value = False
        resp = req.get(url)
        
        
    def Turn_Off(self):
        self.Value = True    
    
def check_voltage():
 
 while True:
 
  if GPIO.input(inputvoltage):
     
   if x.Value == True and x.requests == 0:
    try: 
     print('Voltage In')
     x.requests = x.requests + 1
     print(x.requests)
     x.Turn_On()
    except:
      print('Server Not Responding')   
     
  else:
   if x.Value == False:
      x.requests = x.requests - 1
      print(x.requests)
      x.Turn_Off()
      time.sleep(5)


if __name__ == '__main__':
    x = InitiateRockAssistant()
    check_voltage()


 