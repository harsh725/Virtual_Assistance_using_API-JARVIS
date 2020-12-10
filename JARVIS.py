import speech_recognition as sr
import webbrowser as wb
import pyttsx3,time, re
import requests
gender="Sir"
def my_command():
	# Converts the audio in string & returns
    r=sr.Recognizer()
    with sr.Microphone(device_index=0,chunk_size=2048,sample_rate=48000) as source:

        print('Listening....')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    try:
        command=r.recognize_google(audio).lower()
        sayit('You said: "'+command+'"\n')
    except sr.UnknownValueError:
        print('Your Last command couldn\'t be heard.')
        command=my_command()
    return command


def link(url,query):
    r=sr.Recognizer()

    try:
        wb.get().open_new(url+query)
    except sr.UnknownValueError:
        sayit('Sorry your voice is not audible')
    except sr.RequestError as e:
        sayit('I recomend you to connect to a stable network'+e)


def sayit(text):
	#Takes a string as an argument & speaks
    x=pyttsx3.init('sapi5')
    x.setProperty('rate',140)
    # voices = x.getProperty('voices')
    # x.setProperty('voice', voices[2].id)
    x.say(text)
    if 'master' not in text and 'the end' not in text:print(text)
    x.runAndWait()

def jarvis(command):
    if 'who are you' in command:
        sayit("Hello, I am 'JARIVIS' a virtual assistant designed and developed by my master Harsh Dhiman")
    elif 'bixbi' in command or 'siri' in command or 'google assistant' in command or 'alexa' in command:
        sayit("Yeahh they all are good but 'In the end' it doesn't even matter")
        link('https://music.youtube.com/watch?v=eVTXPUF4Oz4&list=RDAMVMeVTXPUF4Oz4','')
    elif 'time' in command:
        sayit('I can tell you the current Date & Time.')
        audio=my_command()

        x=time.ctime().replace("  "," ")
        if 'time' not in audio:sayit("Date:"+x[:9]+' '+x[-4:])
        if 'date' not in audio:sayit('Time:'+x[9:-4])
    elif 'weather' in command:
        url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        sayit('Sure! I can tell you the weather just tell me the city or state name')
        location=my_command()
        s=requests.get(url+location).json()
        sayit("Weather at "+location+" is "+s['weather'][0]['description'])


    elif 'what are you doing' in command:
        sayit('Just doing my thing!')

    elif 'search' in command:
        reg_ex = re.search('search (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.google.com/maps/place/' + domain
            wb.open(url)
            print('Done!')
        else:
            pass
 
    elif 'music' in command or 'song' in command:
        url='https://music.youtube.com/search?q='
        sayit('So what would you like to here?')
        song=my_command()
        link(url,song)
        
    elif 'youtube' in command:
        url ="www.youtube.com/results?search_query="
        print("Yes ofcourse i will suggest you Youtube Videos\n")
        sayit("just tell me what u need")
        audio=my_command()
        link(url,audio)
        
    elif 'google' in command or 'search' in command:
        url='https://www.google.com/search?q='
        sayit("What you want to search?")
        audio=my_command()
        link(url,audio)

    elif 'joke' in command:
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"}
        )
        if res.status_code == requests.codes.ok:
            sayit(str(res.json()['joke']))
        else:
            sayit('oops!I ran out of jokes')

    elif 'exit' in command or 'quit' in command:
        sayit('Thank you!!\nHave a great day ahead')
        exit()
    else:
        # sayit("\nI am not desinged to do that, You help yourself for now ")
        sayit("I don't know!!")
    sayit('What else you want me to do?')


gender="Maam"
sayit("Hello "+gender+".\nWhat can i do for you?\n\n")
while 1:
	jarvis(my_command())

