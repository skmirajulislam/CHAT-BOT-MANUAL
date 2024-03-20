'''
 @Code developed by SK Mirajul Islam during Code Soft internship in 2022
 @this is an example of chat bot written in python language
 @this software only available for macOS, For windows need some changes in code
''' 

import datetime
import webbrowser
import random
import requests 
import requests
import subprocess

def open_website(website_name):
    supported_websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com'
    }
    try:
        if website_name in supported_websites:
            webbrowser.open(supported_websites[website_name])
            return f"Opening {website_name}..."
        else:
            return f"Sorry, I don't support opening {website_name} at the moment."
    except Exception as e:
        return f"Error opening {website_name}: {e}"

def open_software(software_name):
    supported_software = {
        'calc': 'open -a Calculator',
        'notepad': 'open -a TextEdit'
    }

    try:
        if software_name in supported_software:
            subprocess.run(supported_software[software_name], shell=True)
            return f"Opening {software_name}..."
        else:
            return f"Sorry, I don't support opening {software_name} as software at the moment."
    except Exception as e:
        return f"Error opening {software_name}: {e}"

def open_google_search(query):
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(google_search_url)
    return f"Searching for '{query}' on Google..."

def open_youtube_search(query):
    youtube_search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(youtube_search_url)
    return f"Searching for '{query}' on YouTube..."

def get_current_date_time():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def get_weather(city):
    api_key = '646824f2b7b86caffec1d0b16ea77f79'  
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(base_url)
        data = response.json()
        if 'main' in data and 'temp' in data['main'] and 'weather' in data and len(data['weather']) > 0:
            temperature = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            return f"The current temperature in {city} is {temperature}°C with {weather_desc}."
        else:
            print("Incomplete or unexpected data received:")
            print(data)
            return f"Error fetching weather information for {city}: Incomplete or unexpected data received"
    except requests.exceptions.RequestException as e:
        print(e)
        return f"Error fetching weather information for {city}: {e}"
    except Exception as e:
        print(e)
        return f"Error fetching weather information for {city}: {e}"


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!"
    ]
    return random.choice(jokes)

def set_reminder(reminder):
    return "Reminder set successfully!"

def rule_based_chatbot(user_input):

    if "hello" in user_input.lower():
        return "Hey there! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm doing well, thank you! How about you?"
    elif "i am fine" in user_input.lower():
        return "Great to hear!"
    elif "what is your name" in user_input.lower():
        return "I am your Personal Chatbot. You can call me Piku."
    elif "ok nice name" in user_input.lower():
        return "Thank you!"
    elif "who create you" in user_input.lower():
        return "I was created by you! Remember?"
    elif "can you help me" in user_input.lower():
        return "Of course! I'm here to assist you. Feel free to ask me anything!"
    elif "what is today's date" in user_input.lower():
        return f"Today's date is {get_current_date_time().split()[0]}."
    elif "what's the time now" in user_input.lower():
        return f"The current time is {get_current_date_time().split()[1]}."

    elif "open website" in user_input.lower():
        website_name = user_input.lower().replace("open website", "").strip()
        return open_website(website_name)
    elif "open software" in user_input.lower():
        software_name = user_input.lower().replace("open software", "").strip()
        return open_software(software_name)

    elif "search on google" in user_input.lower():
        query = user_input.lower().replace("search on google", "").strip()
        return open_google_search(query)
    elif "search on youtube" in user_input.lower():
        query = user_input.lower().replace("search on youtube", "").strip()
        return open_youtube_search(query)

    elif "tell me a joke" in user_input.lower():
        return tell_joke()

    elif "what is the weather in" in user_input.lower():
        city = user_input.lower().replace("what is the weather in", "").strip()
        return get_weather(city)

    elif "set a reminder" in user_input.lower():
        reminder = user_input.lower().replace("set a reminder", "").strip()
        return set_reminder(reminder)
    
    else:
        return "I'm sorry, I didn't understand that."

while True:
    user_input = input("You: ")
        
    if user_input.lower() == "exit":
        print("Goodbye! See you later.")
        break

    response = rule_based_chatbot(user_input)
    print("chatbot:", response)
