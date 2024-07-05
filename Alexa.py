import speech_recognition as sam # type: ignore
import pyttsx3 # type: ignore
import pywhatkit # type: ignore
import datetime
import wikipedia # type: ignore
listener = sam.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sam.Microphone() as source:
            print("Hi Iam Listening...")
            voice= listener.listen(source)
            print(voice)
            command=listener.recognize_google(voice)
            command= command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')

                talk(command)
    except:
            pass
    return command
def run_alexa():
    command= take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
         time=datetime.datetime.now().strftime('%I:%M %p')
         talk('Current time is'+time)
    elif 'who the heck is ' in command:
         person=command.replace('who the heck is','')
         info= wikipedia.summary(person,1)
         print(info)
         talk(info)
while True:
            
            run_alexa()