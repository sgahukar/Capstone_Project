import nltk
import datetime
import pyttsx3
import speech_recognition as sr
from nltk.chat.util import Chat, reflections

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get time-based greeting
def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Define chatbot patterns and responses
pairs = [
    (r"(hi|hello|hey)", [f"{get_greeting()} Hello! How can I assist you today?"]),
    (r"(what services do you offer\?|hotel services)", 
     ["We offer room service, spa, gym, free WiFi, and airport pickup."]),
    (r"(what are the check-in and check-out times\?|check in time|check out time)", 
     ["Check-in is from 2 PM, and check-out is until 12 PM."]),
    (r"(do you have a restaurant\?|dining options)", 
     ["Yes, we have a multi-cuisine restaurant and a 24/7 café."]),
    (r"(can i get extra towels\?|room service)", 
     ["Yes, you can request extra towels by calling reception or using the hotel app."]),
    (r"(do you offer airport pickup\?|airport transfer)", 
     ["Yes, we provide airport pickup and drop services. Please book in advance."]),
    (r"(do you have a swimming pool\?|pool availability)", 
     ["Yes, we have an outdoor swimming pool open from 7 AM to 10 PM."]),
    (r"(how do i connect to wifi\?|wifi access)", 
     ["You can connect to our free WiFi by selecting 'Hotel_Guest_WiFi' and using your room number as the password."]),
    (r"(goodbye|bye)", ["Goodbye! Have a great stay."]),
    (r"(.*)", ["I'm not sure about that. Please contact the front desk for assistance."])
]

# Initialize chatbot
hotel_assistant = Chat(pairs, reflections)

# Function for speech recognition (User speaks)
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You: {user_input}")  # Display what the user said
        return user_input.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Could you repeat that?")
        return listen()
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# Start conversation
greeting = get_greeting()
speak(f"{greeting} Hello! How can I help you?")

while True:
    user_input = listen()
    if user_input in ["exit", "quit", "bye"]:
        speak("Thank you! Have a great day!")
        break
    response = hotel_assistant.respond(user_input)
    speak(response)
