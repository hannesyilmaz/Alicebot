import nltk, itertools
import random

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
    seg_sent = nltk.sent_tokenize(input_sent())
    return seg_sent

def input_word_seg():
    seg_word = nltk.word_tokenize(input_sent())
    return seg_word

def input_pos_tag():
    input_pos = nltk.pos_tag(input_word_seg())
    return input_pos

def input_pos_local():
    input_pos_local_list = []
    for items in input_pos_tag():
        input_pos_local_list.append(items)
    return input_pos_local_list

def pos_local_words_return():
        input_match = [item for item in input_pos_local()]
        if input_match[0][1] == 'WP' and input_match[1][1] == 'VBZ' and input_match[2][0] == 'your' and input_match[3][0] == 'name' and input_match[4][1] == '.':
                return 'ask_name_fps'
        elif input_match[2][0] == 'her' and input_match[3][0] == 'name':
                return 'ask_name_tpsf'
        elif input_match[2][0] == 'his'and input_match[3][0] == 'name':
                return 'ask_name_tpsm'
        elif input_match[2][0] == 'their'and input_match[3][0] == 'name':
                return 'ask_name_tpp'
        elif input_match[2][0] == 'your' and input_match[3][0] == 'age':
                return 'ask_age_fps'
        elif input_match[2][0] == 'her' and input_match[3][0] == 'age':
                return 'ask_age_tpsf'
        elif input_match[2][0] == 'his' and input_match[3][0] == 'age':
                return 'ask_age_tpsm'
        elif input_match[2][0] == 'their' and input_match[3][0] == 'ages':
                return 'ask_age_tpp'
        else:
                print('not true')


personal_values = pos_local_words_return()

def pos_local():
    pos_list = []
    for items in pos_tag_text():
        pos_list.append(items)
    return pos_list


def response_main():
        response =[]
        if personal_values == 'ask_name_fps':
                response.append('My'), response.append('name'), response.append('is'), response.append(random.choice([item for item in pos_local() if item[1] == 'NNP'])[0])
                return response
        elif personal_values == 'ask_name_tpsf':
                response.append('Her'), response.append('name'), response.append('is'), response.append(random.choice([item for item in pos_local() if item[1] == 'NNP'])[0])
                return response
        elif personal_values == 'ask_name_tpsm':
                response.append('His'), response.append('name'), response.append('is'), response.append(random.choice([item for item in pos_local() if item[1] == 'NNP'])[0])
                return response
        elif personal_values == 'ask_name_tpp':
                response.append('Their'), response.append('names'), response.append('are'), response.append(random.choice([item for item in pos_local() if item[1] == 'NNP'])[0]), response.append('and'), response.append(random.choice([item for item in pos_local() if item[1] == 'NNP'])[0])
                return response
        elif personal_values == 'ask_age_fps':
                response.append('My'), response.append('age'), response.append('is'), response.append(random.choice([item for item in pos_local() if item[1] == 'CD'])[0])
                return response
        elif personal_values == 'ask_age_tpsf':
                response.append('Her'), response.append('age'), response.append('is'), response.append(random.choice([item for item in pos_local() if item[1] == 'CD'])[0])
                return response
        elif personal_values == 'ask_age_tpsm':
                response.append('His'), response.append('age'), response.append('is'), response.append(random.choice([item for item in pos_local() if item[1] == 'CD'])[0])
                return response
        elif personal_values == 'ask_age_tpp':
                response.append('Their'), response.append('ages'), response.append('are'), response.append(random.choice([item for item in pos_local() if item[1] == 'CD'])[0]), response.append('and'), response.append(random.choice([item for item in pos_local() if item[1] == 'CD'])[0])
                return response
        return response


def convertTuple():
        return_string = ' '.join(response_main())
        return return_string

print(convertTuple())
