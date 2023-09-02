"""
Created on Sat Sep  2 15:33:06 2023

@author: mohamed
"""

import speech_recognition as sr
import pyttsx3
import os

"""
    Function to take voice an input from microphone and 
    transform it as a list of words.
"""
def take_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 2.88
        said = recognizer.listen(source)
        print('I am listening . . . ')
        lst =   recognizer.recognize_google(said, language='en')
    return lst


"""
    Function to take words from the terminal and save it
    in a list to remove those words from our voice.

"""
def take_words():
    print("Hi user, enter all words you want to remove from the voice.")
    print("If you've finished, enter -1.")
    lst = []
    while True:
        word = input()
        if word != '-1':
            lst.append(word)
        else:
            break
    return lst


"""
    Function to output the final list of words.
"""
def speak(result):
    speaker = pyttsx3.init()
    speaker.say(result)
    speaker.runAndWait()
    
    
"""
    Function to iterate over each word in the voice input and 
    check if it’s in the insult list: it put specific-fixed 
    thing in place of it.
"""
def processor(voice, words):
    voice_words = voice.split()
    for word in words:
        voice_words = [w if w != word else "                " for w in voice_words]
    result = " ".join(voice_words)
    return result


"""
    Put all things together
"""
def main():
    voice = take_voice().lower()
    words = take_words()
    result = processor(voice, words)
    speak(result)
    
main()