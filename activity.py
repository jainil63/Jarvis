from utils import take_user_input, say_jarvis, open_chrome
from showcamera import show_camera
import os
import webbrowser


def activity():
    while True:
        user_input = take_user_input().lower()

        if user_input in ["open vscode"]:
            os.system("code")

        elif user_input in ["open chrome"]:
            open_chrome()

        elif user_input in ["open youtube"]:
            webbrowser.open_new_tab("https://www.youtube.com")

        elif user_input in ["open camera"]:
            show_camera()

        elif user_input in ["shutdown device", "shutdown pc"]:
            os.system("shutdown /s /t 0")
            return None

        elif user_input in ["restart", "restart pc"]:
            os.system("shutdown /r /t 0")
            return None

        elif user_input in ["bye", "good bye"]:
            say_jarvis("Good bye sir.")
            quit(0)

        else:
            say_jarvis("Say again please!")
