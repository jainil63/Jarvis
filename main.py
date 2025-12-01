from utils import take_user_input, say_jarvis, wish
from activity import activity


def main():
    wish()

    say_jarvis("Im jarvis, how are you sir!")
    user_input = take_user_input().lower()

    if user_input in ["i am fine", "all right", "nice", "fine"]:
        say_jarvis("Oh, I feel happy by hearing that!")

    elif user_input in ["i am not fine", "i feel bad", "im sick"]:
        say_jarvis("Oh, I feel bad by hearing that!")

    else:
        say_jarvis("Sorry, I didnt understand that!")

    say_jarvis("How can I help you?")

    activity()


if __name__ == "__main__":
    main()
