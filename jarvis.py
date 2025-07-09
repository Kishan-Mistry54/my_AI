import sys
import cv2
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import  datetime
import os
import cv2
import random
from requests import  get
import webbrowser
import wikipedia
import pywhatkit
import time
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please....")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning ")

    elif hour>=12 and hour<18:
        speak("good afternoon ")

    else:
        speak("good evening ")
    speak("i'm jarvis sir. please tell me what can i do for you.")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your mailid','your password')
    server.sendmail('your mailid',to,content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=83263a48521a48a797182dbc3926e513'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
    #speak()
    #takecommand()
    wish()

    while True:

        query = takecommand().lower()

        if "open notepad" in query:
            path = "your_software_path"
            os.startfile(path)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'your_software_path'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(en,neutral)
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rund1132.exe powerprof.dll,SetSuspendstate 0,1,0")

        elif "open cmd" in query or "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "your_music_directory_path"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir ,song))
                else:
                    os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'search on google' in query or "search" in query or "open google" in query:
            query = query.replace("jarvis", "")
            query = query.replace("search on google", "")
            query = query.replace("serach", "")
            speak("searching...")
            print('searching...')
            speak(query)
            speak("This is what I found on google")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query or "search on youtube" in query:
            speak("this is what i found for your search!")
            query = query.replace("youtube","")
            query = query.replace("search on youtube","")
            query = query.replace("jarvis","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("done, sir")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+91your_mobile_no.","this is testing message",12,12)

        elif "email to kishan" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "your_email_id"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "close the window" in query:
            pyautogui.keyDown("alt")

        


        speak("thanks for using me sir, have a good day.")
        sys.exit()

        speak("sir, do you have any other work")

        


