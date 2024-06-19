import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import pyaudio
# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current time
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# Function to get the current date
def get_date():
    today = datetime.today().strftime('%Y-%m-%d')
    return today

# Function to perform a web search
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Here are the search results for {query}"

# Function to listen for commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return ""

# Main function to handle commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = get_time()
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = get_date()
        speak(f"Today's date is {current_date}")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        response = search_web(query)
        speak(response)
    else:
        speak("I am sorry, I don't understand that command.")

# Run the assistant
if __name__ == "__main__":
    speak("Voice assistant initialized. How can I help you?")
    while True:
        command = listen_command()
        if command:
            handle_command(command)
