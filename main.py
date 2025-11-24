from utils import take_user_input, say_jarvis
from showcamera import show_camera
import os


def main():
    say_jarvis("Hello, How are you?")

    user_input = take_user_input().lower()

    if user_input in ["im fine", "all right", "nice", "fine"]:
        say_jarvis("Oh, I feel happy by hearing that!")

    elif user_input in ["im not fine", "i feel bad", "im sick"]:
        say_jarvis("Oh, I feel bad by hearing that!")

    else:
        say_jarvis("Sorry, I didnt understand that!")

    while True:
        say_jarvis("How can I help you?")

        user_input = take_user_input().lower()

        if user_input in ["shutdown device", "shutdown pc"]:
            os.system("echo shutdown /s /t 0")
            return None

        elif user_input in ["restart", "restart pc"]:
            os.system("echo shutdown /r /t 0")
            return None

        elif user_input in ["open vscode"]:
            os.system("code")

        elif user_input in ["open chrome"]:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif user_input in ["open camera"]:
            show_camera()

        elif user_input in ["bye", "good bye"]:
            say_jarvis("Good bye sir.")
            quit(0)

        else:
            say_jarvis("I didn't understand")


if __name__ == "__main__":
    main()
