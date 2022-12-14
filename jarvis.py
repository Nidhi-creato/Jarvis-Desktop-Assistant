import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour<18 :
        speak("Good Afternoon")   

    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you!")    

def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")   

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query      

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('1nt20cs114.nidhi@nmit.ac.in','harrypotter')
    server.sendmail('1nt20cs114.nidhi@nmit.ac.in',to,content)
    server.close()


if __name__ == "__main__":
      wishMe()
    #   while True:
      if 1:  
          query= takeCommand().lower()

          # logic for executing tasks based on query 
          if 'wikipedia' in query:
              speak("Serching Wikipedia...")
              query= query.replace("wikipedia","")
              results= wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)

          elif 'open youtube' in query:
            webbrowser.open("youtube.com")

          elif 'open google' in query:
            webbrowser.open("google.com")

          elif 'open stackoverflow.com' in query:
             webbrowser.open("stackoverflow.com") 

        #   elif 'play music' in query:   
        #      music_dir = ''
          
          elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

          elif 'open code' in query:
            code_path="C:\\Users\\NIDHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
            os.startfile(code_path)

          elif 'email to nidhi' in query:
            try:
                speak("What should I say?") 
                content= takeCommand()
                to= "nidhinarayan178@gmail.com"
                sendEmail(to,content) 
                speak("Email has been sent!")
            except Exception as e:
                print(e)   
                speak("Sorry, I am not able to send this email") 