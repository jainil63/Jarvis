from utils import take_user_input, say_jarvis


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
    take_user_input()
    say_jarvis("I didnt understand that!")
    say_jarvis("Good bye, take care!")


if __name__ == "__main__":
    main()
