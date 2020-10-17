import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!, sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!, sir")
    else:
        speak("Good Evening!, sir")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold = 200
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pratikkumar9097186@gmail.com','Kumar852#')
    server.sendmail('pratikkumar753@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print("Computer: Searching Wikipedia...")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening Youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening Google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        elif 'play cartoon' in query:
            webbrowser.open("https://www.youtube.com/watch?v=1fYvUTlmvDs")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'E:\\My Music'
            songs =os.listdir(music_dir)
            print(songs[0])
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play random music' in query:
            music_dir = 'E:\\My Music'
            songs =os.listdir(music_dir)
            random_number=random.randint(0,100)
            print(songs[random_number])
            os.startfile(os.path.join(music_dir,songs[random_number]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir The Time is",strTime)
            speak(f"Sir, The Time is{strTime} ")

        elif 'open code' in query:
            codepath="C:\\Users\\Pratik Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening Visual Studio Code")
            os.startfile(codepath)

        elif 'open chrome' in query:
            chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening Google Chome")
            os.startfile(chromepath)

        elif 'open cal' in query:
            calpath="C:\\Windows\\System32\\calc.exe"
            speak("opening Calculator")
            os.startfile(calpath)
        elif 'open word' in query:
            wordpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("opening MicroSoft Word")
            os.startfile(wordpath)
        elif 'open control' in query:
            controlpath="C:\\Windows\\System32\\control.exe"
            os.startfile(controlpath)
        elif 'open pic' in query:
            picpath="D:\\Images & Videos\\picachu.jpg"
            os.startfile(picpath)
        elif 'open code block' in query:
            blockpath="C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(picpath)
        elif 'open pycharm' in query:
            pypath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
            os.startfile(pypath)

            elif 'email to me' in query:
            try:
                speak("What Should I Send!")
                content = takeCommand()
                to = "pratikkumar753@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, The Email not send")

        elif 'exit' in query:
            print("Computer: Quitting sir,Thank you for your time.")
            speak("Quitting sir,Thank you for your time.")
            print(exit())

        elif 'introduce yourself' in query:
            temp1="hii I am jarvis. I am a Assistant. Which is Develop By, Prateek Kumar"
            speak(temp1)


        elif 'hello' in query:
            temp3="hello,Sir How may I help you"
            print(temp3)
            speak(temp3)

                    
         elif 'quit' or 'exit' in query:
             speak("Thank you sir")
              print(exit())
        
    
