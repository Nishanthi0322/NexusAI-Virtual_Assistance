import pyttsx3
import speech_recognition as sr
import webbrowser

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        
        # Define a list of websites and their URLs
        sites = [
            ["youtube", "http://www.youtube.com"],
            ["wikipedia", "http://www.wikipedia.com"],
            ["google", "http://www.google.com"],
            ["whatsapp", "http://www.whatsapp.com"],
            ["chatgpt", "http://www.chatgpt.com"]
        ]

        # Iterate over the list and check if the command is to open a website
        for site in sites:
            if f"open {site[0]}" in query.lower():  # Check for the phrase "open site_name"
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])  # Open the website using its URL
                break  # Exit the loop after opening the site

        print(f"User said: {query}")
        return query

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that. Please say it again.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service. Check your internet connection.")
        return None

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Nexus A.I.")

    while True:
        print("Listening....")
        text = takeCommand()
        if text:
            say(text)
        
        # Add a condition to break the loop if the user says "exit" or "stop"
        if text and "exit" in text.lower():
            print("Exiting program.")
            say("Goodbye!")
            break
