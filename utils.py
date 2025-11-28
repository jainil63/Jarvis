import pyttsx3
import time
import speech_recognition as sr
import datetime

engine = pyttsx3.init(driverName="sapi5")
engine.runAndWait()
r = sr.Recognizer()


def take_voice_command():
    with sr.Microphone() as source:
        print("listning...")
        audio = r.listen(source, timeout=5)
        print("recognize...")
        command = r.recognize_google(audio)
        try:
            print(command)
        except Exception as e:
            print(e)
    return command


def send_audio(message):
    if engine.isBusy():
        engine.runAndWait()

    engine.say(message)
    time.sleep(3)


def take_user_input():
    print("User:")
    x = take_voice_command()
    print()
    return x


def say_jarvis(message):
    print("Jarvis: ")
    send_audio(message)
    print(message)
    print()


def wish():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 11:
        say_jarvis("Good morning sir")
    elif 11 <= current_hour < 17:
        say_jarvis("Good afternoon sir")
    else:
        say_jarvis("good evening sir")
