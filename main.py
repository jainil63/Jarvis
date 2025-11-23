from utils import take_user_input, say_jarvis
import os


def main():
    say_jarvis("Hello, How are you?")

    user_input = take_user_input()
    if user_input.lower() in ["im fine", "all right", "nice", "fine"]:
        say_jarvis("Oh, I feel happy by hearing that!")
    elif user_input.lower() in ["im not fine", "i feel bad", "im sick"]:
        say_jarvis("Oh, I feel bad by hearing that!")
    else:
        say_jarvis("Sorry, I didnt understand that!")

    say_jarvis("How can I help you?")
    user_input = take_user_input()
    if user_input.lower() in ["shutdown device", "shutdown pc"]:
        os.system("echo shutdown /s /t 0")
        return None
    elif user_input.lower() in ["restart", "restart pc"]:
        os.system("echo shutdown /r /t 0")
        return None
    elif user_input.lower() in ["bye", "good bye"]:
        say_jarvis("Good bye sir.")
        quit(0)
    else:
        say_jarvis("I didn't understand")

    say_jarvis("Good bye!")


if __name__ == "__main__":
    main()
