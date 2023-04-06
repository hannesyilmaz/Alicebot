import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[36].id)
engine.say('Hello, my name is Alice and I am 22 years old')
engine.runAndWait()

#36 AZ
#17 AU
#32 US
#39 US
#28 GB