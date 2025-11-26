import pyttsx3

engine = pyttsx3.init(driverName="sapi5")
engine.runAndWait()


def take_user_input():
    x = input("User: ")
    print()
    return x


def say_jarvis(message):
    print(f"Jarvis: {message}")
    print()
