import speech_recognition as sr
from datetime import datetime
import webbrowser
import pyautogui
import numpy as np 
import cv2
import pywhatkit
import pyttsx3
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=None)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        query = listen()
        
        if query:
            if "hello" in query or "hi" in query:
                speak("Hello! I hope your are doing well. How can I assist you?")
            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
                break
            elif "time" in query:
                current_time = datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
            elif "introduce yourself" in query or "introduction" in query:
                speak("I am a Voice Assistant created by Mohammad Umar Farooq as his Internship project")
            elif "date" in query:
                current_date = datetime.now().strftime("%Y-%m-%d")
                speak(f"Today is {current_date}")
            elif "search" in query:
                search_query = query.replace("search", "").strip()
                speak(f"Searching the web for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif "who is" in query or "what is" in query:
                person = query.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                speak(info)
            elif "youtube" in query:
                search_query = query.replace("youtube", "").strip()
                speak(f"Opening youtube")
                webbrowser.open(f"https://www.youtube.com/")
            elif "take a screenshot" in query:
                image = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(image), 
                     cv2.COLOR_RGB2BGR)
                cv2.imwrite("image1.png", image)
                speak("I took a screenshot for you.")
            elif "exit" in query  or "bye" in query or "see you" in query or "later" in query:
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("I'm sorry, I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
