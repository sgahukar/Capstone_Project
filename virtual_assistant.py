import webbrowser
import os
import speech_recognition as sr
import datetime
import pyttsx3
import requests
import pywhatkit  # For sending WhatsApp messages
import time
from datetime import datetime
import random
import wikipedia
import cv2

# Initialize the speech engine
engine = pyttsx3.init('sapi5')

# Set properties (rate, volume, and voice)
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 2.0)  # Volume level
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Selects a female voice

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()
    print(f"Assistant: {text}")  # Optional: Print the spoken text

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak("Hello, Good Morning!")
    elif 12 <= hour < 17:
        speak("Hello, Good Afternoon!")
    else:
        speak("Hello, Good Evening!")
    
    speak("How can I assist you today?")

def take_user_input():
    """Takes voice input from the user and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't catch that. Please say it again.")
        return None


def open_google():
    """Opens Google and takes a voice search query"""
    speak("What do you want to search on Google?")
    search_query = take_user_input()
    if search_query:
        webbrowser.open(f"https://www.google.com/search?q={search_query.replace(' ', '+')}")
        speak(f"Searching Google for {search_query}")

def open_youtube():
    """Opens YouTube and takes a voice search query"""
    speak("What do you want to search on YouTube?")
    search_query = take_user_input()
    if search_query:
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}")
        speak(f"Searching YouTube for {search_query}")

def open_cmd():
    """Opens the Command Prompt"""
    os.system("start cmd")
    speak("Opening Command Prompt.")

def open_email():
    """Opens Gmail"""
    webbrowser.open("https://mail.google.com")
    speak("Opening Gmail.")

# OpenWeatherMap API Key (Replace with your own API key)
WEATHER_API_KEY = "7e1430cca305ccd67bb762d36f5ca8dd"

def open_whatsapp():
    """Opens WhatsApp Web"""
    webbrowser.open("https://web.whatsapp.com")
    speak("Opening WhatsApp Web.")

def get_weather():
    """Fetches and speaks the weather report"""
    speak("Please tell me your city name.")
    city = take_user_input()
    
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            speak(f"The current temperature in {city} is {temperature}°C, but it feels like {feels_like}°C.")
            speak(f"The weather is {weather_desc}.")
        else:
            speak("Sorry, I couldn't find the weather report for that location.")
    else:
        speak("I didn't catch the city name. Please try again.")

def open_weather_website():
    """Opens a weather website"""
    webbrowser.open("https://www.weather.com/")
    speak("Opening Weather.com for the latest weather updates.")

def open_news_website():
    """Opens a news website"""
    webbrowser.open("https://www.bbc.com/news")
    speak("Opening BBC News for the latest updates.")

def search_amazon():
    """Asks the user for a product and searches it on Amazon."""
    speak("What product do you want to search for on Amazon?")
    product = take_user_input().replace(" ", "+")  # Convert spaces to '+'
    url = f"https://www.amazon.in/s?k={product}"
    webbrowser.open(url)
    speak(f"Here are some listings for {product} on Amazon.")

def search_wikipedia():
    speak("What do you want to search on Wikipedia?")
    query = take_user_input()
    if query:
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia, {result}")
            print(f"According to Wikipedia: {result}")
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple results found. Please be more specific.")
            print(f"Multiple results found: {e.options[:5]}")
        except wikipedia.exceptions.PageError:
            speak("No results found on Wikipedia.")
            print("No results found on Wikipedia.")

def search_hotels():
    speak("Which city do you want to search for hotels in?")
    city = take_user_input()
    webbrowser.open(f"https://www.google.com/search?q=famous+hotels+in+{city.replace(' ', '+')}")
    speak(f"Here are some famous hotels in {city}.")

def search_swiggy():
    """Asks the user for food or restaurant preference and searches on Swiggy."""
    speak("What food item or restaurant do you want to search for on Swiggy?")
    food_query = take_user_input()

    if food_query:
        swiggy_url = f"https://www.swiggy.com/search?q={food_query.replace(' ', '%20')}"
        speak(f"Searching for {food_query} on Swiggy.")
        webbrowser.open(swiggy_url)

def get_weather(city="Nagpur"):
    """Fetches weather details for Nagpur"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        speak(f"The current temperature in {city} is {temp}°C with {weather_desc}.")
        return temp
    else:
        speak("Sorry, I couldn't fetch the weather details.")
        return None

def suggest_places():
    """Suggests places to visit in Nagpur based on weather"""
    city = "Nagpur"
    temp = get_weather(city)

    if temp is not None:
        if temp < 25:
            places = [
                ("Ambazari Lake & Garden", "https://www.holidify.com/places/nagpur/ambazari-lake-and-garden-sightseeing-3202.html"),
                ("Ramtek & Khindsi Lake", "https://www.holidify.com/places/nagpur/ramtek-sightseeing-3203.html"),
                ("Pench National Park", "https://en.wikipedia.org/wiki/Pench_National_Park")
            ]
            speak("The weather is pleasant. Here are some scenic and outdoor locations to visit.")
        elif temp >= 25 and temp < 35:
            places = [
                ("Waki Woods", "https://www.holidify.com/collections/picnic-spots-near-nagpur"),
                ("Futala Lake", "https://www.holidify.com/places/nagpur/futala-lake-sightseeing-3196.html"),
                ("Krazy Castle Aqua Park", "https://www.tripadvisor.in/Attraction_Review-g662323-d6031562-Reviews-Krazy_Castle_Aqua_Park-Nagpur_Nagpur_District_Maharashtra.html")
            ]
            speak("The weather is warm. You can visit these places in the evening.")
        else:
            places = [
                ("Wet N Joy Water Park", "https://www.expedia.com/Things-To-Do-In-Nagpur.d2512.Travel-Guide-Activities"),
                ("Empress Mall", "https://www.tripadvisor.in/Attraction_Review-g662323-d4408254-Reviews-Empress_Mall-Nagpur_Nagpur_District_Maharashtra.html"),
                ("Raman Science Centre", "https://www.tripadvisor.in/Attraction_Review-g662323-d4408251-Reviews-Raman_Science_Centre-Nagpur_Nagpur_District_Maharashtra.html")
            ]
            speak("It's hot outside. Consider visiting indoor places or water parks.")

        for place, url in places:
            speak(f"You can visit {place}. Opening details now.")
            webbrowser.open(url)

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!"
]

def tell_joke():
    """Tells a random joke"""
    speak("If you're bored, let me tell you a joke!")
    joke = random.choice(jokes)
    speak(joke)

def open_calculator():
    """Opens the calculator"""
    speak("Opening the calculator for you.")
    import subprocess
    subprocess.Popen("calc.exe")


def open_camera():
    """Opens the webcam and displays the video feed."""
    cap = cv2.VideoCapture(0)  # Open default camera (0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        cv2.imshow("Camera Feed", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    greet_user()

    while True:
        #speak("Please tell me a command.")
        command = take_user_input()

        if command:
            if "open google" in command or "google" in command:
                open_google()
            elif "open youtube" in command or "youtube" in command:
                open_youtube()
            elif "open cmd" in command or "open command prompt" in command:
                open_cmd()
            elif "open email" in command or "open gmail" in command or "gmail" in command:
                open_email()
            elif "open whatsapp" in command or "whatsapp" in command:
                open_whatsapp()
            elif "weather" in command:
                get_weather()
            elif "open weather website" in command:
                open_weather_website()
            elif "open news website" in command:
                open_news_website()
            elif "shopping" in command or "amazon" in command or "open amazon" in command:
                search_amazon()
            elif "wikipedia" in command or "search wikipedia" in command:
                search_wikipedia()
            elif "hotels" in command or "best hotels" in command:
                search_hotels()
            elif "order food" in command or "search food" in command or "swiggy" in command:
                search_swiggy()
            elif "places to visit" in command or "best places according to weather" in command:   
                suggest_places()
            elif "bored" in command or "i am getting bore" in command or "the day is boring" in command:
                tell_joke()
            elif "open calculator" in command:
                open_calculator()
            elif "open camera" in command or "start camera" in command:
                speak("Opening camera.")
                open_camera()
            elif "exit" in command or "thank you" in command or "bye" in command or "thanks" in command:
                speak("You're welcome! Have a great day!")
                break
            else:
                speak("Sorry, I didn't understand. Please try again.")

def process_command(command):
    if command:
        if "open google" in command or "google" in command:
            open_google()
            return "Opening Google"
        elif "open youtube" in command or "youtube" in command:
            open_youtube()
            return "Opening YouTube"
        elif "open cmd" in command or "open command prompt" in command:
            open_cmd()
            return "Opening Command Prompt"
        elif "open email" in command or "open gmail" in command or "gmail" in command:
            open_email()
            return "Opening Gmail"
        elif "open whatsapp" in command or "whatsapp" in command:
            open_whatsapp()
            return "Opening WhatsApp"
        elif "weather" in command:
            get_weather()
            return "Fetching weather"
        elif "open weather website" in command:
            open_weather_website()
            return "Opening weather site"
        elif "open news website" in command:
            open_news_website()
            return "Opening news site"
        elif "shopping" in command or "amazon" in command or "open amazon" in command:
            search_amazon()
            return "Searching on Amazon"
        elif "wikipedia" in command or "search wikipedia" in command:
            search_wikipedia()
            return "Searching Wikipedia"
        elif "hotels" in command or "best hotels" in command:
            search_hotels()
            return "Searching hotels"
        elif "order food" in command or "search food" in command or "swiggy" in command:
            search_swiggy()
            return "Ordering food"
        elif "places to visit" in command or "best places according to weather" in command:   
            suggest_places()
            return "Showing places based on weather"
        elif "bored" in command or "i am getting bore" in command or "the day is boring" in command:
            tell_joke()
            return "Told you a joke"
        elif "open calculator" in command:
            open_calculator()
            return "Opening calculator"
        elif "open camera" in command or "start camera" in command:
            open_camera()
            return "Opening camera"
        elif "exit" in command or "thank you" in command or "bye" in command or "thanks" in command:
            return "You're welcome! Have a great day!"
        else:
            return "Sorry, I didn't understand. Please try again."


# assistant_api.py

from flask import Flask, request, jsonify
from virtual_assistant import speak, take_command, wish_me, process_command

app = Flask(__name__)

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query = data.get("query")
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    print(f"User said: {query}")
    response = process_command(query)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
