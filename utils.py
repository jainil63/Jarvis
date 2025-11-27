import pyttsx3
import time

engine = pyttsx3.init(driverName="sapi5")
engine.runAndWait()


def send_audio(message):
    if engine.isBusy():
        engine.runAndWait()

    engine.say(message)
    time.sleep(3)


def take_user_input():
    x = input("User: ")
    print()
    return x


def say_jarvis(message):
    print("Jarvis: ")
    send_audio(message)
    print(message)
    print()
