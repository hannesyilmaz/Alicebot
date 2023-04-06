import speech_recognition as sr
import pyttsx3

# obtain audio from the microphone



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
def speech_recog():
    speech_r = []
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        speech_r.append(r.recognize_google(audio))
        return speech_r
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def convertTuple():
    string_r = ' '.join(speech_recog())
    return string_r

print(convertTuple())

'''

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[36].id)
engine.say(convertTuple())
engine.runAndWait()
'''