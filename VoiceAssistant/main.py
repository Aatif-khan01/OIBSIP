import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import sys
import requests

print("VoiceAssistant 1.1! Created by Aatif Muneeb Khan.")

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for noise
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble with the service.")
            speak("Sorry, I'm having trouble with the service.")
            return None

def respond_to_command(command):
    if command:
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {now}")
        elif "date" in command:
            from datetime import datetime
            today = datetime.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "search" in command:
            query = command.replace("search", "").strip()
            speak(f"Searching for {query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)
        elif "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            sys.exit()
        else:
            speak("Sorry, I did not understand that command.")
    else:
        speak("I could not hear your command clearly.")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    try:
        speak("Hello! How can I help you today?")
        while True:
            command = listen_command()
            if command:
                respond_to_command(command)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully...")
        sys.exit()

if __name__ == "__main__":
    print("Voice Assistant is starting...")
    main()
