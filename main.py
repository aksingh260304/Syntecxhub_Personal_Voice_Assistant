import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import datetime
import os


engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)

            command = command.lower()

            print("You:", command)

            return command

        except:
            return ""


def execute_command(command):

    if "hello" in command:
        speak("Hello Ankit, how can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching {query}")
        pywhatkit.search(query)

    elif "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "exit" in command:
        speak("Goodbye")
        return False

    else:
        speak("Sorry, I did not understand that command.")

    return True


speak("Personal Voice Assistant Started")

running = True

while running:
    command = listen()

    if command:
        running = execute_command(command)