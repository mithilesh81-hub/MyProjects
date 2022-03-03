from datetime import datetime
import pyttsx3
import speech_recognition as sr
import Whatsapp_Automation as wh
import Sms_Automation as sms
import LothianBus_Automation as bus

r = sr.Recognizer()
now = datetime.now()

current_time = str(now.strftime("%H:%M:%S").replace(':', '')[:-2])

engine = pyttsx3.init()
volume = engine.getProperty('volume')


class VoiceAssistantTest:
    while True:
        wakeword = ''
        print("Say Rock. I will help you")
        try:
            with sr.Microphone() as source:
                wakewordaudio = r.record(source, duration=6)
                wakeword = str(r.recognize_google(wakewordaudio)).lower()
                print(wakeword)
                print(wakeword.find('rock'))


        except Exception as e:
            print(e)
            pass

        if wakeword.find('rock') > -1 or wakeword.find('raq') > -1 or wakeword.find('raaq') > -1 \
                or wakeword.find('raaq') > -1 \
                or wakeword.find('iraq') > -1 or wakeword.find('hierarch') > -1 \
                or wakeword.find('mark') > -1 or wakeword.find('work') > -1 or wakeword.find('haydock') > -1 \
                or wakeword.find('ock') > -1 or wakeword.find('lock') > -1 or wakeword.find('drug') > -1:
            print('How Can I Help You')
            engine.setProperty('volume', 2.0)
            engine.say('How Can I Help You')
            engine.runAndWait()
            Task = ''
            try:
                with sr.Microphone() as source:
                    TaskAudio = r.record(source, duration=5)
                    Task = str(r.recognize_google(TaskAudio)).lower()
                    print(Task)
            except Exception as e:
                print(e)
                pass

            if Task.find('whatsapp') > -1 or Task.find('messages') > -1:
                wh.callfunction()

            elif Task.find('sms') > -1 or Task.find('text messages') > -1:
                sms.callfunction()

            elif Task.find('bus') > -1:
                bus.callfunction(Task)
