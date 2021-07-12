import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as wb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("I am an AI assistant")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("current date is")
    speak(day)
    speak(month)
    speak(year)


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("now the time is")
    speak(Time)


def wishme():
    speak("Welcome back!")

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<=17:
        speak("Good afternoon")
    elif hour>17 and hour<=24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Jarvis at your service. How can I help you?")
    #date()
    #time()


#wishme()

def takeCommand():
    r = sr.Recognizer()
    my_mic_device = sr.Microphone(device_index=1)
    with my_mic_device as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    #my_string = r.recognize_google(audio)
    #print(my_string)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again....")

        return "None"

    return query

def sendmail():
    """server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login("maisie13brown","Jimin#0613")
    server.sendmail("maisie13brown",to,content)
    server.close()"""
    msg = MIMEMultipart()
    message = "This mail is sent by jarvis"
    # setup the parameters of the message
    password = "Jimin#0613"
    msg['From'] = "maisie13brown@gmail.com"
    msg['To'] = "rasikagirvikar14@gmail.com"
    msg['Subject'] = "Test"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\Users\DELL\Pictures\Screenshots\name.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == '__main__':
    wishme()
    takeCommand()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("searching...")
            fquery = query.replace("wikipedia","")
            result = wikipedia.summary(fquery, sentences = 3)
            speak(result)

        elif "send email" in query:
            try:
                sendmail()
                speak("successfully sent email")
            except Exception as e:
                speak(e)
                speak("unable to send the mail")

        elif "search in chrome" in query:
            speak("What should i search")
            """chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")"""

            url = takeCommand()
            wb.register('chrome', None, wb.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            wb.get('chrome').open_new(url +".com")

        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs = os.listdir("F:\music")
            os.startfile(os.path.join("F:\music", songs[0]))

        elif "remember" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("You told me to remember this "+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "read to do" in query:
            remember = open("data.txt","r")
            speak(remember.read())
            remember.close()

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken successfully")

        elif "usage" in query:
            cpu()

        elif "jokes" in query:
            jokes()

        elif "quit" in query:
            speak("Going offline. Thank you")
            quit()