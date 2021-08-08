import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib





engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Phil !")
    elif 12 <= hour < 18:
        speak("Good Afternoon Phil !")
    else:
        speak("Good Evening Phil !")
    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # you can take max one second pause(in between words) while giving command
        audio = r.listen(source)
        

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    with open('/Users/awantika/PycharmProjects/Python_Projects/password.txt') as f:
        password = f.read()

    server.login('b20150@students.iitmandi.ac.in',password)
    server.sendmail('b20150@students.iitmandi.ac.in',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('http://www.stackoverflow.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        elif 'email to myself' in query:
            try:
                speak('What should I say')
                content = takeCommand()
                to = 'deoraawantika@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent.")

            except Exception as e:
                print(e)
                speak("Sorry Phil,the email could not be sent.")




            
            




            
        
        
        

    

        

