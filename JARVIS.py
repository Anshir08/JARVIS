import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print("Initializing Jarvis")

MASTER = "Anshir Chaudhary"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Speak function will pronounce the string which is passed to it
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
    with sr.Microphone() as source:
        print("Listening...")
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
    server = smtplib.SMTP('smtp.gmail.com',535)
    server.ehlo()
    server.starttls()
    server.login("chaudharyanshirsingh2050@gmail.com",'9045441245')
   # server.sendmail("chaudharyanshirsingh2050@gmail.com",'9045441245')
    server.sendmail("vishnu2018.121@gmail.com",to,content)
    server.close()
#Main program starts here...
speak("Initializing Jarvis...")
WishMe()
speak("I am jarvis how may i help you")
#query = takeCommand()

#Logic for executiing tasks as per the query
def main(query = takeCommand()):

    if 'wikipedia' in query.lower():
                  speak('Searching Wikipedia...')
                  query = query.replace("wikipedia","")
                  results = wikipedia.summary(query, sentences =2)
                  print(results)
                  speak(results)
    elif 'youtube' in query.lower():
                 #url = "youtube.com"
                # chrome_path = "https:\\www.google.com"
                 webbrowser.open("youtube.com")
    elif 'open portal' in query.lower():
                 #url = "aktu.ac.in"
                 #chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application'
                 webbrowser.open('aktu.ac.in')
    elif 'play music' in query.lower():
                 songs = os.listdir("E:\\songs")
                 print(songs)
                 os.startfile(os.path.join("E:\\songs",songs[0]))
    elif 'the time' in query.lower():
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strtime)
                speak(f"{MASTER} the time is {strtime}")
    elif 'open code' in query.lower():
                codepath = "C:\\Users\\user\\PycharmProjects\\Jarvis\\main.py"
                os.startfile(codepath)
    elif 'email to harry' in query.lower():
                try:
                    speak("What should I send")
                    content = takeCommand()
                    to = "vishnu2018.121@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent successfully")
                except Exception as e:
                    print(e)
main()