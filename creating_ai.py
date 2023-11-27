import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import os
import speech_recognition as sr
engine =pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print (voices[1].id)
engine.setProperty("voice",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour >=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Your Assistant, Sir What can I do for you? ")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__=="__main__":
    wishme()
    while True:
    # if 1:
        query=takecommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            rewrite=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(rewrite)
            speak(rewrite)
        elif "who is" in query:
            speak("Searching Google...")
            query=query.replace("Wikipedia","")
            rewrite=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(rewrite)
            speak(rewrite)
        elif "tell me about" in query:
            speak("Searching Google...")
            query=query.replace("Wikipedia","")
            rewrite=wikipedia.summary(query,sentences=3)
            speak("According to Google")
            print(rewrite)
            speak(rewrite)

        elif "what can you do" in query:
            print("Many works like : I can tell you time, open youtube, search anything in google, open google, and many more  ")
            speak("Many works like : I can tell you time, open youtube, search anything in google, open google, and many more  ")
        
        elif "who invented you" in query:
            print("Definately You Invented me, Sir!")
            speak("Definately You Invented me, Sir!")

        elif "thank you"  in query: 
            print("Most welcome sir! Its my pleasure that i helped you, sir.")
            speak("Most welcome sir! Its my pleasure that i helped you, sir.")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")

        elif "play music" in query:
            webbrowser.open("https://youtu.be/uU7BSAVQI8M?si=sH7lTBzzHyqh7812")
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, The time is {strtime}")

        elif "can you tell me how you are invented" in query:
            print("No Sir, sorry that's the secret!")
            speak("No Sir, sorry that's the secret!")
        elif "i love u" in query:
            print("I Love You too, Sir.")
            speak("I Love You too, Sir.")

        elif "good bye" in query:
            print("Good Bye. Have a Nice Day sir!")
            speak("Good Bye. Have a Nice Day sir!")

            exit()