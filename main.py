def say_user():
    input("User: ")
    print()
    
def say_jarvis(message):
    print(f"Jarvis: {message}")  
    print()

def main(): 
    say_jarvis("Hello")
    say_jarvis("I'm currently busy! can we talk later?")
    say_user()
    say_jarvis("Bye, Thank you!")

if __name__ == "__main__":
    main()
