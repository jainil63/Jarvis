from utils import take_user_input, say_jarvis

def main(): 
    say_jarvis("Hello")
    say_jarvis("I'm currently busy! can we talk later?")

    user_input = take_user_input()
    if user_input == "yes":
        say_jarvis("Bye, Thank you!")
    else:
        say_jarvis("Nope, It's final, I have to go.")

if __name__ == "__main__":
    main()
