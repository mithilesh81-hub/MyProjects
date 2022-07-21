import RPi.GPIO as GPIO  # importing files for program
import time
from flask import Flask
from flask_ask import Ask,statement,question,session
import json
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

def Give_Hand_Wash():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    GPIO.output(15, True)
    GPIO.output(13,False)
    GPIO.output(11,False)
    GPIO.output(7,True)
    time.sleep(2)
    Rewind_Hand_Wash()
    Stop_Motors()
    
def Rewind_Hand_Wash():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    GPIO.output(15, False)
    GPIO.output(13,True)
    GPIO.output(11,True)
    GPIO.output(7,False)
    time.sleep(0.5)
    Stop_Motors()


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


@app.route('/')
def homepage():
  print('Good')
  return "Hello This is HomePage For Automatic Handwash"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like some handwash?'
    return question(welcome_message)

@ask.intent("YesIntent")
def run_function():
    Ok_msg = "Ok"
    Give_Hand_Wash()
    return statement(Ok_msg)

@ask.intent("NoIntent")
def no_Intent():
    Ok_msg = "Ok"
    return statement(Ok_msg)

if __name__ == "__main__":
    app.run(debug=True)
