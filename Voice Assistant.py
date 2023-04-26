"""
    Created on Wed Apr 26 00:32:17 2023
    @author: Mohamed Hassan
    @IDE: Spyder
"""

import pyttsx3 
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes

"""
    Function to take a speech from a user, transform it into a text
    using Google's speech recognition service, and return the 
    recognized text or an error message depending on the outcome.
"""
def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.88
        said = r.listen(source)
        try:
            print("I'm listening ...")
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry, I don't understand you.")
            return "I'm waiting ..."
        except sr.RequestError:
            print("Sorry, the service is down :(")
            return "I'm waiting ..."
        except:
            return "I'm waiting ..."


"""
    Function to recieve a text message as input, convert it to 
    speech using the pyttsx3 library and speak the message at loud.
"""
def speaking(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()



"""
    Loop to print all voices on your devices, then take the id of 
    the specific voice that you want and set it to use it all time.
"""
engine = pyttsx3.init()
#for voice in engine.getProperty('voices'):
#    print(voice)
voiceId = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voiceId)


"""
    Function to return the weekday.
"""
def queryDay():
    day = datetime.date.today()
    weekday = day.weekday()
    days = {
        0: "Monday", 
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday", 
        4: "Friday", 
        5: "Saterday", 
        6: "Sunday"}
    try:
        speaking(f'Today is {days[weekday]}')
    except:
        pass



"""
    Function to return the time.
    I specified it a format to return only the hours and the minutes.
"""
def queryTime():
    time = datetime.datetime.now().strftime("%I:%M")
    speaking(f"It's {time[0:2]} o'clock and time[3:5] minutes")



"""
    Function to greet the user at the startup.
"""
def greeting():
    speaking('''Hey, what's up.
             My name is Zira and I am your personal assistant.
             How can I help you? ''')


"""
    The main function.
"""
def main():
    greeting()
    whileKey = True
    while(whileKey):
        command = transform().lower()
        if 'youtube' in command:
            speaking("Starting Youtube now ...")
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'webbrowser' in command:
            speaking("Starting the webbrowser now ...")
            webbrowser.open("https://www.google.com")
            continue
        elif 'facebook' in command:
            speaking("Starting Facebook now ...")
            webbrowser.open("https://www.facebook.com")
            continue
        elif 'linkedin' in command:
            speaking("Starting Linkedin now ...")
            webbrowser.open("https://www.linkedin.com")
            continue
        elif 'day' in command:
            queryDay()
            continue
        elif 'time' in command:
            queryTime()
            continue
        elif 'stop' in command:
            speaking("Ok, I'll stop in few seconds")
            break
        elif 'shutdown' in command:
            speaking("Ok, I'll shutdown in few seconds")
            break

main()    
        
        
        
        
        
        
        
        
        