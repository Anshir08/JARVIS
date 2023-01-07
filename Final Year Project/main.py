import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess, sys
import time
import requests
from bs4 import BeautifulSoup
import pyautogui


MASTER = "Sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
   

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish you as per the current time
def WishMe():
        
        hour = datetime.now().hour  

        if hour>=0 and hour<12:
            speak("Good Morning" + MASTER)

        elif hour>+12 and hour<18:
            speak("Good Afternoon" +MASTER)

        else:
            speak("Good Evening" + MASTER)
 
def ctime():
    try:
        tim = datetime.now().strftime("%I:%M %p") 
        print(tim)
        Im,p = tim.split(' ')
        I,M = map(int,Im.split(':'))
        time = ''.join(map(str,[I,M,p]))
        speak("Time is "+time)
    except Exception as e:
        print(e)

def weather():
    try:
        search = "temperature in mathura"
        url = "https://www.google.com/search?q=" + search
        r = requests.get(url).text
        data = BeautifulSoup(r, "html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        # clouds = data.find_all("div", class_="wob_dcp")
        speak(f"The Temperature Outside is {temperature}, with scattered clouds.")
    except Exception as e:
        print(e)

#This command will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    query = None
    while 1:  
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            print("Listening...")
            audio = r.listen(source)

        try: 
            query = r.recognize_google(audio)
            print("Recognizing...")
            print(f"user said: {query}\n")
            break

        except Exception as e:
            print("Say that again please\n")


    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("chaudharyanshirsingh2050@gmail.com",'lzznllvszwqwvchq')
   # server.sendmail("chaudharyanshirsingh2050@gmail.com",'9045441245')                                                                                                                                                 
    server.sendmail("chaudharyanshirsingh2050@gmail.com",to,content)
    server.close()

#Main program starts here...
g = None
while True:
    query = takeCommand()
    try:
        if 'wake up' in query.lower():
            g = subprocess.Popen([sys.executable, 'jarvis_gui_main.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
            time.sleep(1)
            speak("Initializing...")
            time.sleep(1)
            WishMe()
            speak("I am Jarvis how may i help you")
            break
    except:pass


#Logic for executing tasks as per the query
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

p = None
while True:
    try:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Results...')
            
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 1)
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak('I am fine Sir! What about you?')

        elif 'alarm' in query:
            speak('Alarm has been set successfully')

        elif 'youtube' in query:
            speak('Opening Youtube...')
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'portal' in query:
            speak('opening aktu portal')
            webbrowser.get(chrome_path).open("aktu.ac.in")

        elif 'music' in query or 'songs' in query:
            songs = os.listdir("D:\\Users\\Anshir\\Music\\")
            print(songs)
            os.startfile(os.path.join("D:\\Users\\Anshir\\Music\\",songs[0]))
            time.sleep(20)
            # os.startfile(songs[0])

        elif 'time' in query:
            ctime()

        elif 'project' in query:
            codepath = "D://Users//Anshir//Desktop//Some Folder//Final_Year_Project_Report.pdf"
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak("What should I send, Sir")
                content = takeCommand()
                to = "chaudharyanshir@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully, Sir")
            except Exception as e:
                print(e)

        elif 'mouse' in query:
            if p is None:
                p = subprocess.Popen([sys.executable, 'AIVirtualMouseProject.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
            else:
                p.kill()
                
        elif 'message' in query:
            speak("What should I send?")
            content = takeCommand()
            pyautogui.write(content)
            pyautogui.press('enter')
            
        elif 'covid' in query:
            import Covid
            speak(Covid.message)
        
        elif 'weather' in query:
            weather()

        elif 'are you there' in query:
            speak('At your service, always Sir')

        elif 'exit' in query:
            g.kill()
            break

    except Exception as e:
        pass
        
