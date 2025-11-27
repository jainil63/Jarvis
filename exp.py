import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("listning...")
    audio = r.listen(source, timeout=5)
    print("recognize...")

    try:
        print(r.recognize_google(audio))
    except Exception as e:
        print(e)
