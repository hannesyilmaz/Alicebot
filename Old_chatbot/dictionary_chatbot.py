import nltk
import random
from random import randint

raw_text = nltk.corpus.gutenberg.raw('carroll-alice.txt')

def sentence_segmentation(raw_text):
    segmented_sentences = nltk.sent_tokenize(raw_text)
    return segmented_sentences

def word_tokenization(raw_text):
    segmented_words = nltk.word_tokenize(raw_text)
    return segmented_words

def pos_tag_text():
    post = nltk.pos_tag(word_tokenization(raw_text))
    return post

def input_sent():
    sentence = input("Enter your sentence: ")
    return sentence

def input_sent_seg():
    seg_sents = nltk.sent_tokenize(input_sent())
    lower_words = [word.lower() for word in seg_sents]
    return lower_words

def input_word_seg():
    seg_words = nltk.word_tokenize(input_sent())
    lower_letters = [word.lower() for word in seg_words]
    return lower_letters

def input_pos_tag():
    input_pos = nltk.pos_tag(input_word_seg())
    return input_pos

def input_pos_local():
    input_pos_local_list = []
    for items in input_pos_tag():
        input_pos_local_list.append(items)
    return input_pos_local_list

def pos_local():
    pos_list = []
    for items in pos_tag_text():
        pos_list.append(items)
    return pos_list

#print(input_pos_local())


use_input = input_pos_local()
first_indices = [item[0] for item in use_input]

#print(first_indices)

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
        elif 'how' in first_indices:
                if 'old' in first_indices:
                        return True




value_matches_subject = {'you': "I'm", 'your': 'my', 'his': 'his', 'her': 'her', 'their': 'their'}
value_matches_aux = {'your': 'is', 'his': 'is', 'her': 'is', 'their': 'is'}

'''
def value_dict_subject():
    for key, value in value_matches_subject.items():
            if key in first_indices:
                    return value
'''

def response_main():
        response =[]
        subject_key = []
        aux_key = []
        for item in first_indices:
                if item in value_matches_subject.keys():
                        subject_key.append(item)
                        sub_key_str = ' '.join(subject_key)
                        response.append(value_matches_subject.get(sub_key_str))
        
        if in_name() == True:
                response.append('name')
        
        if in_age() == True:
                if 'you' not in first_indices:
                        response.append('age')
                else:
                        response.append('')
        
        
        for item in first_indices:
                if item in value_matches_aux.keys():
                        aux_key.append(item)
                        aux_key_str = ' '.join(aux_key)
                        response.append(value_matches_aux.get(aux_key_str))

        if in_name() == True:
                response.append(random.choice([item for item in pos_local() if item[1] == 'NNP'])[0])
                return response
        
        if in_age() == True:
                response.append(str(random.randint(0,99)))
                return response


#def response_back_main():
        #response_back = []



#print(response_main())


def convertTuple():
        return_string = ' '.join(response_main())
        return return_string

print(convertTuple())




#print(value_dict_subject())