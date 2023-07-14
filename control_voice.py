from datetime import date
from functools import partial
import speech_recognition as speech 
import os 

import pyttsx3

engine = pyttsx3.init()
# voice = engine.getProperty("voices")
# print(voice)
# engine.setProperty("voices", voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak_corotuine(function):
    
    def speak_er(argument):
        while True:
            getting = (yield);

            if getting == argument:
                function(argument) # send the command to works ..
                # speak(" Sorry Sir! I have not Train to Advance")
            else: continue
    return speak_er


def matching(argument):
    if argument == "hello":
        speak(" Hello My name is Jarvis")
    elif  argument == "What is My Name".lower():
        speak(" My name is Smallchat")
    elif argument == "who is developed you".lower():
        speak(" Md Shahid Ali ")
    elif argument == "What do you".lower():
        speak(" I can Help you to Better for The Searching ! and Finding the Result .")
    elif argument == " What is your project Name".strip().lower():
        speak(" Project Name is ! SmallChat")
    elif argument == "What is the time".strip().lower():
        speak(date.today().weekday())        

    else: 
        speak(" Thanking you sir.")
        exit()





def take_command():
    while True:
        command = speech.Recognizer()
        with speech.Microphone() as source:
            print(" Listing ....")
            command.pause_thresold = 1
            # audio = command.listen(source)
            audio = input("Enter The Command")
            try:
                print(" Recognization ....")
                query = command.recognize_google(audio, language='en-in')
                print(f" you Said : {query}")
                users = speak_corotuine(matching)(query)
                users.__next__()
                users.send(query)
                users.close()
            except Exception as Error:
                print(" try Again ...")
                return "None"    







# lists = []
# for i in input().split('\n'):
#     lists.append(i.strip())

# for i in  lists:
#     matching(i)
#     # print(i)

# print(lists)


if __name__ == "__main__":
    speak(" System Loading , Please Wait ....")
    speak(" System Loaded Sucessfully ! Hello Sir")
    # take_command()
    audio = input("Enter The Command:- ")
    print(os.getcwd()+"\\Apple\\")
    speaks = speak_corotuine(matching)
    starts = speaks(audio)
    starts.__next__()
    starts.send(audio)
    starts.close()
    
    

