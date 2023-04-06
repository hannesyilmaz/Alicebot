import nltk
import random
import datetime
import os
import sys
from random import randint
import speech_recognition as sr
import pyttsx3
import re


def main():

    raw_text = nltk.corpus.gutenberg.raw('carroll-alice.txt')

    def sent_tokenization(raw_text):
        segmented_sentences = nltk.sent_tokenize(raw_text)
        return segmented_sentences

    def word_tokenization(raw_text):
        segmented_words = nltk.word_tokenize(raw_text)
        return segmented_words

    def pos_tag_text():
        post = nltk.pos_tag(word_tokenization(raw_text))
        return post


    
    def speech_recog():
        speech_r = []
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ask me something!")
            audio = r.listen(source)
            try:
                speech_r.append(r.recognize_google(audio))
                return speech_r
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        

    def convertTuple1():
        string_r = ' '.join(speech_recog())
        return string_r
    

    def input_word_seg():
        seg_words = nltk.word_tokenize(convertTuple1())
        #lower_letters = [word.lower() for word in seg_words]
        return seg_words

    def input_pos_tag():
        input_pos = nltk.pos_tag(input_word_seg())
        return input_pos


    use_input = input_pos_tag()
    first_indices = [item[0] for item in use_input]



    
    def find_sentence():
        found_sentence = [item for item in sent_tokenization(raw_text) if ' '.join(first_indices) in item]
        return found_sentence
    

    def word_toke_tag():
        word_token = [nltk.word_tokenize(item) for item in find_sentence()]
        #print(word_token)
        #zlist = []
        size_of_token = len(word_token)
        item = 0
        while item < size_of_token:
            xlist = [nltk.pos_tag(item) for item in word_token]
            item = item + 1
            return xlist

    
    
    def in_name():
        if 'what' in first_indices:
            if 'name' in first_indices:
                return True
        elif 'name' in first_indices:
            if '?' in first_indices:
                return True
        elif 'who' in first_indices:
            if '?' in first_indices:
                return True



    def in_age():
        if 'what' in first_indices:
            if 'age' in first_indices:
                return True
        elif 'age' in first_indices:
            if '?' in first_indices:
                return True
        elif 'how' or 'How' in first_indices:
            if 'old' in first_indices:
                return True


    
    value_matches_greet = {'hey': 'hello', 'hello': 'hi', 'hi': 'hey', 'Yo': 'Oy'}
    value_matches_subject = {'you': "I'm", 'your': 'my', 'his': 'his', 'her': 'her', 'their': 'their', 'he': 'he', 'she': 'she'}
    value_matches_aux = {'your': 'is', 'his': 'is', 'her': 'is', 'their': 'is', 'he': 'is', 'she': 'is'}


    
    def response_main():
        response =[]
        subject_key = []
        aux_key = []
        greeting_key = []
        for item in first_indices:
            if item in value_matches_subject.keys():
                subject_key.append(item)
                sub_key_str = ' '.join(subject_key)
                response.append(value_matches_subject.get(sub_key_str))
        
                if in_name() == True:
                    if 'you' not in first_indices:
                        if 'he' not in first_indices:
                            if 'she' not in first_indices:
                                response.append('name')
                    else:
                        response.append('')
            
                if in_age() == True:
                    if 'you' not in first_indices:
                        if 'he' not in first_indices:
                            if 'she' not in first_indices:
                                response.append('age')
                    else:
                        response.append('')
            
            
                for item in first_indices:
                    if item in value_matches_aux.keys():
                        aux_key.append(item)
                        aux_key_str = ' '.join(aux_key)
                        response.append(value_matches_aux.get(aux_key_str))

                if in_name() == True:
                        response.append(random.choice([item for item in pos_tag_text() if item[1] == 'NNP'])[0])
                        return response
            
                if in_age() == True:
                        response.append(str(random.randint(0,99)))
                        return response

            if item in value_matches_greet.keys():
                greeting_key.append(item)
                greeting_key_str = ' '.join(greeting_key)
                response.append(value_matches_greet.get(greeting_key_str))
                return response
            
            if item == 'exit':
                sys.exit()


    def convertTuple():
            return_string = ' '.join(response_main())
            return return_string
    



    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[36].id)
    engine.say(convertTuple())
    engine.runAndWait()

while True:
    main()