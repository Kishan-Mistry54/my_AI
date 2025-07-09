import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2
from time import sleep
import pyautogui
import time
from pyautogui import click
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("I am Jarvis Sir. What can I help you sir")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
      #  print(e)
        print("say that again please....")
        return"none"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailid@gmail.com', 'your-password')
    server.sendmail('kishanmistry13542@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'song please' in query or 'play some song' in query or 'could you play some song' in query:
            speak('Which song should I play sir!...')
            song = takecommand()
            webbrowser.open(f'https://open.spotify.com/search/' + song)
            pyautogui.click(x=1055, y=617)
            speak('playing' + song)

        elif 'play' in query or 'can you play' in query or 'please play' in query:
            speak("okay sir...")
            query = query.replace("play", "")
            query = query.replace("could you play", "")
            query = query.replace("please play", "")
            webbrowser.open(f'https://open.spotify.com/serach/' + query)
            pyautogui.click(x=1055, y=617)
            print('Enjoy your song sir...')
            speak("Enjoy your song sir....")


        elif 'play music' in query:
            music_dir = 'put_your_directory'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\kisha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = "kishanmistry13542@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("sorry my friend .I am not able to send this email")

        elif 'open chrome' in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open command prompt' in  query:
            cmd = "%windir%\\system32\\cmd.exe"
            os.startfile('cmd')

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)  # Use the correct index for your webcam

            if not cap.isOpened():
                print('Error: Unable to open webcam')
            else:
                ret, frame = cap.read()

                if ret and frame.shape[0] > 0 and frame.shape[1] > 0:
                    cv2.imshow('Webcam', frame)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print('Error: Invalid webcam frame')

        elif 'search on google' in query or "search" in query:
            query = query.replace("jarvis","")
            query = query.replace("search on google","")
            query = query.replace("serach", "")
            speak("searching...")
            print('searching...')
            speak(query)
            speak("This is what I found on google")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif 'send message' in query or "message" in query:
            try:
                number = "+91"
                speak("enter the number I have to send message")
                number += takecommand()
                speak("okay,now what should i send?")
                msg = takecommand()
                minute = int(datetime.datetime.now().strftime("%M"))+1
                pywhatkit.sendwhatmsg(number,msg,time,minute,10)
            except Exception as e:
                print(e)
                speak("i can't send that")










