import nltk


def input_sent():
    sentence = input("Enter your sentence: ")
    return sentence

def input_sent_seg():
    seg_sents = nltk.sent_tokenize(input_sent())
    lower_words = [word.lower() for word in seg_sents]
    return lower_words

def input_word_seg():
    seg_words = nltk.word_tokenize(input_sent())
    return seg_words

def input_pos_tag():
    input_pos = nltk.pos_tag(input_word_seg())
    return input_pos

def input_pos_local():
    input_pos_local_list = []
    for items in input_pos_tag():
        input_pos_local_list.append(items)
    return input_pos_local_list

use_input = input_pos_local()
first_indices = [item[0] for item in use_input]

'''
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
        if 'how' in first_indices:
                if 'old' in first_indices:
                        return True
'''
#print(in_name())

value_matches_subject = {'you': 'I', 'your': 'my', 'his': 'his', 'her': 'her', 'their': 'their'}
value_matches_aux = {'you': 'are', 'I': 'am', 'he': 'is', 'she': 'is', 'it': 'is'}



#print(value_matches_subject.keys())

def test_dict():
        key1 = []
        for item in first_indices:
                if item in value_matches_subject.keys():
                        key1.append(item)
        key1_str = ' '.join(key1)
        return value_matches_subject.get(key1_str)

print(test_dict())

#print(value_matches_subject.values())
'''
def value_dict_subject():
    for key, value in value_matches_subject.items():
            if key in first_indices:
                    return value
'''

