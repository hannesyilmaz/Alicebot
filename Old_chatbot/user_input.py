import nltk

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



def key_word():
    #it extracts the desired key word depending on its tag
    for item in use_input:
        if 'NNP' in item[1]:
            return item[0]

#print(key_word())

def find_sentence():
    #it finds all the instances of the 'Key word' in the text
    found_sentence = [item for item in sent_tokenization(raw_text) if key_word() in item]
    return found_sentence
    #return sentences as seperate elements with quotation marks

#find_sentence()

def input_sent():
    #input sentence
    sentence = input('enter word: ')
    return sentence

def input_word_seg():
    #tokenize the words of the input
    seg_words = nltk.word_tokenize(input_sent())
        #lower_letters = [word.lower() for word in seg_words]
    return seg_words



def input_pos_tag():
    #tag the tokenized words of the input
    input_pos = nltk.pos_tag(input_word_seg())
    return input_pos


use_input = input_pos_tag()
first_indices = [item[0] for item in use_input]
#print(first_indices)
second_indices = [item[1] for item in use_input]
    



def word_toke_tag():
    word_token = [nltk.word_tokenize(item) for item in find_sentence()]
    #returns sentences tagged in each of their own list in a 2d list
    #print(word_token)
    #zlist = []
    size_of_token = len(word_token)
    item = 0
    while item < size_of_token:
        xlist = [nltk.pos_tag(item) for item in word_token]
        item = item + 1
        return xlist

#print(word_toke_tag())

def find_the_sent():
    #returns the only list that contains the d
    for item in word_toke_tag():
        for index in item:
            if 'IN' in index:
                return item

#print(find_the_sent())

the_found_sent = find_the_sent()
first_indices_fts = [item[0] for item in the_found_sent]
#print(first_indices_fts)




def convertTuple():
    return_str = ' '.join(first_indices_fts)
    return return_str

print(convertTuple())

'''
def extract_word():
    for item in use_input:
        if 'NNP' in item[1]:
            return item[0]
        
def in_inquiry():
    if 'who' in first_indices:
        if 'IN' in second_indices:
            return True

    

def response_main():
    #response = []
    for item in word_toke_tag():
        if extract_word() in item:
            if in_inquiry() == True:
                return item

#print(response_main())
'''


'''
user_dict = {}
user_dict[first_indices] = first_indices

print(user_dict)
'''





















