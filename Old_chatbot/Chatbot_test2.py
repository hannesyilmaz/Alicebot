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



    def input_sent():
        sentence = input('enter word: ')
        return sentence

    def input_word_seg():
        seg_words = nltk.word_tokenize(input_sent())
        #lower_letters = [word.lower() for word in seg_words]
        return seg_words

    def input_pos_tag():
        input_pos = nltk.pos_tag(input_word_seg())
        return input_pos


    use_input = input_pos_tag()
    first_indices = [item[0] for item in use_input]
    second_indices = [item[1] for item in use_input]


    def key_word():
        #it extracts the desired key word depending on its tag
        for item in use_input:
            if 'NNP' in item[1]:
                return item[0]


    
    def find_sentence():
        found_sentence = [item for item in sent_tokenization(raw_text) if ' '.join(first_indices) in item]
        return found_sentence
    
    def key_word_sentence():
        found_sentence = [item for item in sent_tokenization(raw_text) if key_word() in item]
        return found_sentence
    
    #print(find_sentence())

    def word_toke_tag():
        #returns sentences tagged in each of their own list in a 2d list
        word_token = [nltk.word_tokenize(item) for item in find_sentence()]
        #print(word_token)
        #zlist = []
        size_of_token = len(word_token)
        item = 0
        while item < size_of_token:
            xlist = [nltk.pos_tag(item) for item in word_token]
            item = item + 1
            return xlist
    
    def key_word_toke_tag():
        #returns sentences tagged in each of their own list in a 2d list
        word_token = [nltk.word_tokenize(item) for item in key_word_sentence()]
        #print(word_token)
        #zlist = []
        size_of_token = len(word_token)
        item = 0
        while item < size_of_token:
            xlist = [nltk.pos_tag(item) for item in word_token]
            item = item + 1
            return xlist

    #print(word_toke_tag())

    def key_word_find_the_sent():
        #returns the only list that contains the matched tag
        for item in key_word_toke_tag():
            for index in item:
                if 'VBZ' in index:
                    return item
    
    #print(find_the_sent())



    #print(first_indices_fts)

    
    def in_name():
        if 'what' in first_indices:
            if 'name' in first_indices:
                return True
        elif 'name' in first_indices:
            if '?' in first_indices:
                return True
        elif 'who' in first_indices:
            if 'NNP' not in second_indices:
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


    def chr_name():
        if 'who' or 'Who' in first_indices:
            if 'NNP' in second_indices:
                return True
    

    value_matches_greet = {'hey': 'hello', 'hello': 'hi', 'hi': 'hey', 'Yo': 'Oy'}
    value_matches_subject = {'you': "I'm", 'your': 'my', 'his': 'his', 'her': 'her', 'their': 'their', 'he': 'he', 'she': 'she'}
    value_matches_aux = {'your': 'is', 'his': 'is', 'her': 'is', 'their': 'is', 'he': 'is', 'she': 'is'}


    
    def response_main():
        the_found_sent_ = key_word_find_the_sent()
        first_indices_fts = [item[0] for item in the_found_sent_]
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

                if chr_name() == True:
                    response.append(' '.join(first_indices_fts))
            
            
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
            
            if chr_name() == True:
                return first_indices_fts
            
            if item == 'exit':
                sys.exit()


    def convertTuple():
            return_string = ' '.join(response_main())
            return return_string
    
    print(convertTuple())

while True:
    main()