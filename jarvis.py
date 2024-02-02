#Project jarvis
import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
from gtts import gTTS
import os
import time
import subprocess
import pyautogui
import serial
import keyboard
import time
#arduino orders 1 (lights up an led for 2 seconds )
#you can change the orders from the arduino ide  
def arduino_orders1():
    # arduino_serial = serial.Serial('COM10', 9600)
    # time.sleep(2)
    arduino_serial.write('1'.encode())
    time.sleep(2)
    ''' arduino_serial.close() #in case you want to close the serial after using the arduino just once
     but in this case you should add the 2 lines i commented ! just to initialize the Arduino once again ...'''

        

#Text To Speech
def speak(audio):
    tts = gTTS(text=audio, lang='en-au')
    tts.save("output.mp3")
    os.system("start output.mp3")

#This feature is optional , to let jarvis greet you !
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning yacine")
    elif hour>=12 and hour<18:
        speak("good afternoon yacine") 
    else:
        speak("good night yacine")  

# convret audio to text
 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising....") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
        return text

    #error handling (common way)
    except Exception: 
        print("Network connection error") 
        return "none"
    return text


#for main function                               
if __name__ == "__main__":
    wish()
    arduino_serial = serial.Serial('COM10', 9600)
    time.sleep(2)
    while True:
        query = takecom().lower()
        #Searching in wikipedia summary
        if "what do you know about" in query or "wikipedia" in query or "search" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            query.replace("what do you know about","")
            query.replace("search","")
            results = wikipedia.summary(query)
            print(results)
            speak(results)
        #arduino orders    
        elif 'open light' in query or "light" in query or "turn the light" in query:
            speak("okay")
            arduino_orders1()
            time.sleep(2)
        #openning youtube
        elif 'open youtube' in query or "open video online" in query or "nassim" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        #openning GitHub    
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        #openning Facebook
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")     
        #openning Instagram 
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    
        #openning google    
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
        #openning a wesite called Phoenix    
        elif 'open phoenix' in query:
            webbrowser.open("https://phoenix-esgee.site/")
            speak("opening phoenix website")
        #openning G-mail to check the inbox 
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
        #openning Notion     
        elif 'open notion' in query:
            webbrowser.open("https://www.notion.so/") 
            speak("opening Notion !")  
        #openning Amazon     
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        #openning ChatGpt    
        elif 'open' and 'gpt' in query or 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")
            speak("opening chatgpt")
        #Listening to Music from the folder in the path    
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = 'D:\SnapTube Audio'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(musics)))
            
        #Open a video from the specified path (watching a movie ...)
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0]))  
        #Ending the programm (break)    
        elif 'good bye' in query:
            speak("good bye")
            exit()
        #Shutting down the pc     
        elif "shut down" in query or  "close pc" in query:
            speak("shutting down")
            os.system('shutdown -s')
        #Asking Jarvis how is he ...     
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            speak("how about you ?")
            ans_take_from_user_how_are_you = takecom().lower()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        #Credits         
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Yacine Laribi Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        #Introduction of Jarvis ...    
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        #Greeting    
        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Yacine Laribi ! How May i Help you.."
            print(hel)
            speak(hel)
        #Name    
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis but they used to call me dababa"  
            print(na_me)
            speak(na_me)
        #feelings    
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 
        #i case the query is not detected !    
        elif query == 'none':
            continue 
        #Exiting     
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'Okay , i am exiting now'
            speak(ex_exit)
            exit()
        #Googling something       
        elif 'google' in query :
            query=query.replace('google','')
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'okay searching about'+query
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
        #Closing windows in the browser using (ctrl+w)    
        elif 'close' and 'window' in query:
            speak('okay')
            pyautogui.hotkey('ctrl', 'w')
        #changing Window (tabilation)
        elif 'change' and 'window' in query:
            speak('okay')
            pyautogui.hotkey('alt', 'tab')
        #If you are on a text editor or something !    
        elif 'write' in query:
            query=query.replace('write','')
            query.split()
            speak('writing'+query)
            pyautogui.hotkey(*query)
        #In case it doesn't understand you it searches in google 
        #in reality we are going to add an LLM here for the response  
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand you but i will search in the  internet to give you an answer !'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)       

'''Basically the code is not really optimized cuz the are thousands of if else statements here
but if you assure running it on a good cpu , you will get a wonderful results , and with the perfect 
arduino commands you can recreate jarvis ironman's house perfectly '''            