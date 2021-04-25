import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import pyjokes
import randfacts
import wikipedia
import weathercom
import requests
import json
import psutil
import pyautogui
from oyt import *
from wiki import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Night")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said :{query}\n ")

    except Exception as e:
        print("I am sorry  , please repeat again....")
        return "None"
    return query


def weatherReport(city):
    weatherdetails = weathercom.getCityWeatherDetails(city)
    temp = json.loads(weatherdetails)["vt1observation"]["temperature"]
    humidity = json.loads(weatherdetails)["vt1observation"]["humidity"]
    phrase = json.loads(weatherdetails)["vt1observation"]["phrase"]
    return temp, humidity, phrase


if __name__ == '__main__':
    wish()
    speak("I am your Personal Assistant, How are you sir?")
    while True:
        text = takeCommand().lower()
        if "what about you " in text:
            speak("I am good sir , What can I do for you?")

        elif "date" in text:
            curDate = datetime.datetime.now().strftime("%d:%B:%Y")
            curDay = datetime.datetime.now().strftime("%A")
            speak(f"Today's date is {curDate} and day is {curDay}")
        
        elif "time" in text:
            curTime = datetime.datetime.now().strftime("%H:%M:%S %p")
            speak(f"The current time is {curTime}")

        elif "open" and "code" in text:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open" and "lt" in text:
            codePath = "C:\\Program Files\\LTC\\LTspiceXVII\\XVIIx64.exe"
            os.startfile(codePath)

        elif "open google" in text:
            speak("opening google in your browser")
            webbrowser.open(url="https://google.com")

        elif "open youtube" in text:
            speak("opening youtube in your browser")
            webbrowser.open(url="https://youtube.com")

        elif "open" and "chapter" in text:
            speak("opening ISTE in your browser")
            webbrowser.open(url="https://istevit.in")

        elif "joke" in text:
            J = pyjokes.get_joke("en", "neutral")
            print(J)
            speak(J)
            # takeCommand()

        elif "facts" in text:
            F = randfacts.getFact()
            print(F)
            speak(F)

        elif "according to wikipedia" in text:
            speak("searching in wikipedia.....")
            word = text.replace("wikipedia", "")
            results = wikipedia.summary(word, sentences=2)
            speak("according to wikipedia....")
            print(results)
            speak(results)

        elif "play online" in text:
            speak("Sure sir, what do you want me to play ?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                print("Recognizing....")
                title = r.recognize_google(audio, language="en-in")
            print("Playing {} in youtube".format(title))
            speak("Playing {} in youtube".format(title))
            bot = music()
            bot.play(title)

        elif "information" in text:
            speak("Please name the topic sir ?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                print("Recognizing....")
                topic = r.recognize_google(audio, language="en-in")
            print("Searching {} in wikipedia online".format(topic))
            speak("Searching {} in wikipedia online".format(topic))
            assit = info()
            assit.get_info(topic)

        elif "weather" in text:
            print("Sure sir ,please tell me the city")
            speak("Sure sir ,please tell me the city")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                print("Recognizing....")
                city = r.recognize_google(audio, language="en-in")
                temp, humidity, phrase = weatherReport(city)
                print("Currently in " + city + " the temperature is " + str(
                    temp) + " degrees celcius , with humidity of " + str(
                    humidity) + " percent and the sky is " + phrase)
                speak("Today's Weather Report : Currently in " + city + " the temperature is " + str(
                    temp) + " degrees celcius , with humidity of " + str(humidity) + " percent and sky is " + phrase)

        elif "news" in text:
            api_address = "https://newsapi.org/v2/top-headlines?country=in&apiKey=00edecf191db4a378638247a08dba133"

            response = requests.get(api_address)
            news_json = json.loads(response.text)

            speak("how many headlines should i tell ?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                print("Recognizing....")
                count = r.recognize_google(audio, language="en-in")
                count = int(count)

            # count = 3
            print("Here are today's top {} headlines".format(count))
            speak("Here are today's top {} headlines".format(count))

            for news in news_json['articles']:
                if count > 0:
                    T = str(news['title'])  # title of each headline stored in T as string
                    print(T)
                    speak(T)
                    count -= 1

        elif "cpu usage" in text:
            usage = str(psutil.cpu_percent())
            speak('CPU is at' + usage)

            battery = psutil.sensors_battery()
            speak('Battery is at')
            speak(battery.percent)

        elif "take screenshot" in text:
            img = pyautogui.screenshot()
            speak("Done sir")
            img.save('E:\\Captures')

        elif "take notes" in text:
            file = open('notes.txt', 'w')
            speak('Should i include date and time ?')
            ans = takeCommand()
            speak("What should i write sir")
            notes = takeCommand()
            if "yes" or "sure" in ans:
                curTime = datetime.datetime.now().strftime("%H:%M:%S %p")
                curDate = datetime.datetime.now().strftime("%d:%B:%Y")
                file.write(curTime)
                file.write(curDate)
                file.write(':-\n')
                file.write(notes)
                speak("Done taking notes sir.")
            else:
                file.write(notes)
                speak("Done taking notes sir.")

        elif "show notes" in text:
            speak("Opening notes sir")
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif "go offline" in text:
            speak("Going offline sir, bye")
            quit()