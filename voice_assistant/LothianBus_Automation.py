import json
from datetime import datetime
import pyttsx3
import requests
import speech_recognition as sr

r = sr.Recognizer()
now = datetime.now()

current_time = str(now.strftime("%H:%M:%S").replace(':', '')[:-2])

engine = pyttsx3.init()
volume = engine.getProperty('volume')

Saughton_Rose_Gardens = '6200201280'
Balgreen_Primary_School = '6200248760'

bus = ''
busvalueconverted = 0

x = requests.get('https://tfeapp.com/api/website/stop_times.php?stop_id=' + Balgreen_Primary_School)
y = (json.loads(x.text))
ints = []

def callfunction(Task):
    for s in Task.split():
        if s.isdigit():
            ints.append(s)
            print(s)
    bus = getbusvalue()

    for i in range(3):
        print(bus)
        servicename = y["services"][i]['service_name']
        if servicename == bus:
            busvalueconverted = i
            ReadBusTimes(busvalueconverted)

def ReadBusTimes(busvalue):
    Noofdeptime = 0
    for i in y["services"][busvalue]["departures"]:
        Noofdeptime = Noofdeptime + 1

    engine.say('you have a bus')
    engine.runAndWait()

    for t in range(Noofdeptime):
        departure_time = str(y["services"][busvalue]["departures"][t]['departure_time'])

        Departure_time = str(departure_time.replace(':', ''))

        if str(Departure_time)[:2] == str(current_time)[:2]:
            DiffTimeInMin = str(int(Departure_time) - int(current_time))

        else:
            DiffTimeInMin = str(int(Departure_time) - int(current_time) - 40)

        if int(DiffTimeInMin) < 60:
            print('In: ' + DiffTimeInMin)
            engine.setProperty('volume', 2.0)
            engine.say(DiffTimeInMin + 'Minutes')
            engine.runAndWait()
        else:
            print('At: ' + str(Departure_time))
            engine.setProperty('volume', 2.0)
            engine.say('At' + str(Departure_time))
            engine.runAndWait()


def getbusvalue():
    if len(ints) == 1:
        bus = ints[0]
        print(bus)
        print('In If')
        return bus

    elif len(ints) == 0:
        engine.setProperty('volume', 2.0)
        engine.say('What Bus Details Would You Like')
        engine.runAndWait()

        with sr.Microphone() as source:
            audio = r.record(source, duration=4)
        try:
            bus = str(r.recognize_google(audio))
            return bus
        except Exception as e:
            bus = '2'
        return bus