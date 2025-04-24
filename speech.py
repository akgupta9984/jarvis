import webbrowser
import speech_recognition as sr
import os
from o_retrieve import search_internet  # Import the new search function

def say(text):
    os.system(f"say {text}") 
    return

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from the service.")
            return None

if __name__ == '__main__':
    print('python')
    say("hello i am jarvis ai")
    while True: 
        print('listening')
        query = take_command()
        sites = [["youtube","https://www.youtube.com"],["hotstar","https://www.hotstar.com"]]
        
        # Check for search command
        if "search for" in query.lower():
            search_query = query.lower().replace("search for", "").strip()
            results = search_internet(search_query)  # Call the search function
            say(results)  # Speak out the results
            continue
        
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir...")
                webbrowser.open(site[1])