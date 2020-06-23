import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import random
import sys


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
print(voices[0      ].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning mehul")
    elif hour>=12 and hour<17:
        speak("good afternoon mehul sir!")
    else:
        speak("good evening babe")
    speak("i am jarvis your virtual assistant pease tell me how may i help you!")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold =1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        speak("can you please say that again...")
        return "none"
    return query

if __name__ == '__main__':
    wishMe()
    while (1):
        query=takeCommand().lower()
        try:
            if 'wikipedia ' in query:
                speak("searching wikipedia")
                query=query.replace("wikipedia", "")
                results=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/watch?v=Lp9Ftuq2sVI")

            elif 'open stackoverflow' in query:
                webbrowser.open("https://stackoverflow.com/")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com/")

            elif 'open geeksforgeeks' in query:
                webbrowser.open("https://www.geeksforgeeks.org/")
            elif 'open gmail'  in query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            elif  'open google maps' in query:
                webbrowser.open("https://www.google.com/maps")
            elif 'open hackerrank' in query:
                webbrowser.open("https://www.hackerrank.com/domains/python?filters%5Bdifficulty%5D%5B%5D=easy&filters%5Bsubdomains%5D%5B%5D=py-introduction")
            elif 'open hackerearth' in query:
                webbrowser.open("https://www.google.com/search?q=hackerearth&rlz=1C1CHBF_enIN881IN881&oq=hackere&aqs=chrome.0.69i59j69i57j0l3j69i60l3.3086j0j7&sourceid=chrome&ie=UTF-8")
            elif 'open my portfolio' in query:
                webbrowser.open("https://mehulshakya.github.io/mehul_portfolio/")
            #speak('mehul is a very naughty as well as good boy')
            elif 'open hackerrank' in query:
                webbrowser.open(
                    "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

            elif 'play music' in query:
                music_dir="D:\\songs and ringtones"
                songs=os.listdir(music_dir)
                n = random.randint(0, 284)
                #print(songs)
                os.startfile(os.path.join(music_dir,songs[n]))


            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
                print(strTime)
                speak(f"Sir,the time is{strTime}")
        except Exception as s:
            speak('unable to listen say it again')

        try:
            if 'about yourself'  in query:
                speak('my name is jarvis i am designed by Mr. Mehul Shakya and he has provided me with a speed capacity of 1 Terahertz (THz) and a memory capacity of 1 Zettabyte.')
            elif 'i love you'  in query:
                speak("pleasure to hear this but i don't believe in these type of shitty things")
            elif 'about me' in query:
                speak('you are the most prettiest person i have ever met you can ask me anything i am always here for you ')
            elif 'certifications ' in query:
                dir = "E:\work"
                serials = os.listdir(dir)
                #n = random.randint(0, 284)
                # print(songs)
                os.startfile(os.path.join(dir,serials[0]))
            elif 'exit' in query:
                speak('thank you')
                sys.exit()

        except Exception as m:
            speak('not hearable say it again please')

