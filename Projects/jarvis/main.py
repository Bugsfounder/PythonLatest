# export GROQ_API_KEY="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"
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import client_graqC
from gtts import gTTS
import pygame
import os

# recognizer = sr.Recognizer()
engine = pyttsx3.init()
api = "8b24e1ef076f4eeb82db4e8e6d2940c4"

engine.setProperty("rate", 150)  # Speed of speech (words per minute, default is 200))
engine.setProperty("volume", 1)  # volume level (0.0 to 1.0)
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[3].id)


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # pygame.mixer.music.unload()
    # os.remove("temp.mp3")


def fetch_headlines(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        titles = [article["title"] for article in data["articles"]]
        return titles
    else:
        print(f"Failed to fetch headlines. Status code: {response.status_code}")
        return []


def processCommand(c):
    print("Command: ", c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        newsLst = fetch_headlines(api)
        if len(newsLst):
            for news in newsLst:
                print(news)
                speak(news)
    else:
        # Let OpenAi Handle The request
        output = client_graqC.ai(c)
        print(output)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    # Listen for the wake work "Jarvis"
    while True:
        print("recognizing...")
        # recognize speech using Sphinx
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Sphinx error; {e}")
