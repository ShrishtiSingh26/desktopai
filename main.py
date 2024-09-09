import pyttsx3
import speech_recognition as sr
import win32com.client
import webbrowser
import wikipedia
import os
import datetime
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Ziri . Please tell me how may I help you")
def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

if __name__=="__main__":
   wishMe()
   while True:

       query = takeCommand()
       sites=[["youtube","https.//youtube.com"]]
       for site in sites:
           if f"Open {site[0]}".lower() in query.lower:
               speak("Opening Youtube")
               webbrowser.open(site[1])
       #if 'wikipedia' in query:
         #  query = query.replace("wikipedia", "")
          # results = wikipedia.summary(query, sentences=2)
          # speak("According to Wikipedia")
         #  print(results)
          # speak(results)

       #elif 'time' in query:
          # strtime=datetime.datetime.now().strftime("%H:%M:%S")
          # speak(f"the time is {strtime}")
