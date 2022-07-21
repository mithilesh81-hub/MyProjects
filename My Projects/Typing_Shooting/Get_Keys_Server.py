from flask import Flask, request, render_template
from  Keyboard_Typer import initiate_key_class
import projecter_On as po
import RPi.GPIO as GPIO


    
app = Flask(__name__)

 
@app.route('/user/<task>',methods = ['POST', 'GET'])
def Welcome(task):
   
   try: 
    key1 = task.lower()
    print(key1)
    
    try:
        initiate_key = initiate_key_class()
        
        if key1 == 'ctrl' or key1 == 'left' or key1 == 'down' or key1 == 'tab' or key1 == 'alt' or key1 == 'enter' or key1 == 'shift' or key1 == 'projecter' or key1 == 'turnoffprojecter' or key1 == 'shoot' or key1 == 'unlock':
          print('In If')
          initiate_key.initiate_key(key1)
          

        else:
            print('In else')
            for i in key1:
             initiate_key.initiate_key(i)
    
    
    except Exception as e:
        print('Invalid Key')
        print(e)
    
    finally:
        return key1
   
   except Exception as e:
       print(e)
       return 'Invalid Key'
   finally:
       GPIO.cleanup()

if __name__ == '__main__':
    app.run(host='192.168.0.239')    