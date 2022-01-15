import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess, sys


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
   hour = int(datetime.datetime.now().hour)
   print(hour)

   if hour>=0 and hour<12:
       speak("Good Morning" + MASTER)

   elif hour>+12 and hour<18:
       speak("Good Afternoon" +MASTER)

   else:
       speak("Good Evening" + MASTER)


#This command will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    audio = None
    with sr.Microphone() as source:
        print("Listening...")
        while not audio:
            audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("chaudharyanshirsingh2050@gmail.com",'9105399385')
   # server.sendmail("chaudharyanshirsingh2050@gmail.com",'9045441245')
    server.sendmail("chaudharyanshir@gmail.com",to,content)
    server.close()
#Main program starts here...
while True:
    query = takeCommand()
    try:
        if 'wake up' in query.lower():
            WishMe()
            speak("I am Jarvis how may i help you")
            break
    except:pass


#Logic for executiing tasks as per the query
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
p = None
while True:
    try:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'portal' in query:
            webbrowser.get(chrome_path).open("aktu.ac.in")

        elif 'music' in query:
            songs = os.listdir("C:\\Users\\Anshir\\Music")
            print(songs)
            os.startfile(os.path.join("C:\\Users\\Anshir\\Music",songs[0]))
            # os.startfile(songs[0])

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"{MASTER} the time is {strtime}")

        elif 'synopsis' in query:
            codepath = "C:\\Users\\Anshir\\Desktop\\Final Year Project\\Project_Synopsis.pdf"
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak("What should I send")
                content = takeCommand()
                to = "chaudharyanshir@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)

        elif 'mouse' in query:
            if p is None:
                p = subprocess.Popen([sys.executable, 'AIVirtualMouseProject.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
            else:
                p.kill()
        
        elif 'covid' in query:
            import Covid
            speak(Covid.message)

        elif 'exit' in query:
            break

    except Exception as e:
        print(e)
        
