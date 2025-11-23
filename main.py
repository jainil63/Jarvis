def say_user():
    input("User: ")

def say_jarvis(message):
    print(f"Jarvis: {message}")  

def main(): 
    say_jarvis("Hello\n")
    say_jarvis("I'm currently busy! can we talk later?\n")
    say_user()
    print()
    say_jarvis("Bye, Thank you!")

if __name__ == "__main__":
    main()
