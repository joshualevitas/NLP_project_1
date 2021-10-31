import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import words, names
import json 
import numpy as np

from sorter import *

# pattern = 'NP: {<DT>?<JJ>*<NN>}'
# cp = nltk.RegexpParser(pattern)
stop_words = ['@', 'Golden', 'Globes', 'RT', 'GoldenGlobes', '#', '*', '.']
stop_words_noms = ['@', 'golden', 'globes', 'rt', 'Golden', 'Globes', '#', '*', '.', 'Nshowbiz', 'Actor', 'best', 'Best', 'act','Act', 'drama', 'Drama', 'and', 'picture', 'Picture', 'globo', 'musical', 'Musical']
vowels = ['a','e','i','o','u','y']

def spacer(word):
    #https://www.codegrepper.com/code-examples/python/how+to+add+space+before+capital+letter+in+python
    new_word = ''
    for i, letter in enumerate(word):
        if i and letter.isupper():
            new_word += ' '

        new_word += letter
    
    return new_word

def space_free(word):
    #returns 1 if there are no spaces, 0 if there are
    for i, letter in enumerate(word):
        if letter == ' ':
            return 0
    return 1


def get_full_phrases(processed_tweet):
    phrases = []
    tmp = []
    l = len(processed_tweet)
    c = 0
    while c < l:
        if processed_tweet[c][1] == 'NNP' and not processed_tweet[c][0].isupper():
            tmp.append(processed_tweet[c][0])
            c += 1
        else:
            if tmp != []:
                phrases.append(tmp)
                tmp = []
            c += 1
   

    return phrases

def already_there(word, arr):
    for elt in arr:
        if word in elt:
            return True 

def top_five(array_2d, cat):
    # input = [['abc', 1], ['efg', 4] ... ]

    tmp = array_2d
    out = []
    c = 0
    while c < 5:
        
        max = 0
        to_append = ''
        for elt in range(len(tmp)):
            if tmp[elt][1] > max and is_valid_2(tmp[elt][0][0]) and not already_there(tmp[elt][0][0], out) and voweled(tmp[elt][0][0]):
                if cat_typer(categories[cat]):
                    
                    if tmp[elt][0][0] not in names.words() or len(tmp[elt][0]) == 1:
                        max = tmp[elt][1]
                        to_append = tmp[elt][0]
                        idx = elt
                else: 
                    if tmp[elt][0][0] in names.words():
                   
               
                        max = tmp[elt][1]
                        to_append = tmp[elt][0]
                        idx = elt

        out.append(to_append)
        tmp.pop(idx)
        c += 1
    
    return out




def preprocess(sent):
    ##only works if names are capitalized
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    names = []
    movies = []

    for word in range(len(sent)-1):
        if sent[word][1] == 'NNP':
            if sent[word+1][1] == 'NNP':
                names.append(sent[word][0] + " " + sent[word+1][0])
            else:
                #figure out how to remove duplicate^
                movies.append(sent[word][0])



    return names, movies




def is_valid(proper_nouns):
    for pn in proper_nouns:
        if pn in stop_words: return False
        
    return True

def is_valid_noms(proper_nouns):
    for pn in proper_nouns:
        if pn in stop_words_noms: return False
        # if pn not in words.words(): return False
    return True

def is_valid_2(words):
    for word in words:
        for w in stop_words_noms:
            if w in word:
                return False
    return True

def voweled(word):
    for i, letter in enumerate(word):
        if letter in vowels:
            return 1
    return 0


def get_full_name(name, potential_hosts):
    for person in potential_hosts:
        if len(person.split()) == 2:
            if name in person:
                return person

    return name






def get_hosts(file):
    f = open(file)
    data = json.load(f)
    hosts = []
    
    potential_hosts = []
    # potential_host_counts = []
    
    for tweet in range(len(data)):
        if 'host' in data[tweet]['text']:
            tweet_tokenized = nltk.word_tokenize(data[tweet]['text'])
            tweet_tokenized = nltk.pos_tag(tweet_tokenized)
            
            
            for word in range(len(tweet_tokenized)-1):
                if tweet_tokenized[word][1] == 'NNP' and is_valid(tweet_tokenized[word][0]):
                    if tweet_tokenized[word + 1][1] == 'NNP' and is_valid(tweet_tokenized[word + 1][0]):
                        potential_hosts.append(tweet_tokenized[word][0] + " " + tweet_tokenized[word+1][0])

                    else: potential_hosts.append(tweet_tokenized[word][0])

    ###
    for p_host in range(len(potential_hosts)):
        if len(potential_hosts[p_host].split()) == 1:
            # print(potential_hosts[p_host] + ", " + get_full_name(potential_hosts[p_host], potential_hosts))
            potential_hosts[p_host] = get_full_name(potential_hosts[p_host], potential_hosts)


    hosts.append(max(set(potential_hosts), key = potential_hosts.count))
    
    for p_host in potential_hosts:
        if p_host == hosts[0]:
            potential_hosts.remove(p_host)
    
    hosts.append(max(set(potential_hosts), key = potential_hosts.count))


            
    return hosts
                    


def already_found(name, twoD_Arr):
    #returns index of person or -1 if not found
    for pair in range(len(twoD_Arr)):
        if name == twoD_Arr[pair][0]:
            return pair
    
    return -1



def sort_noms(nominees):
    sorted_noms = []
    used_words = []
    
    for nom in nominees:        
        seen = False
        for uw in used_words:
            if uw in nom:
                seen = True
        if not seen:
            sorted_noms.append(nom)
            for w in nom:
                used_words.append(w)

    return sorted_noms
            


            
            


def get_nominees(year, categories, cat_filters):
    f = open(year)
    data = json.load(f)
    nominees = []
   
    for cat in range(len(categories)):
        potential_noms = []
        idxs_ = np.random.choice(len(cat_filters[cat]), size=100, replace=False)
        for relevant_tweet_idx in cat_filters[cat][idxs_]:
            tweet_tokenized = spacer(data[relevant_tweet_idx]['text'])
            # tweet_tokenized = nltk.word_tokenize(data[relevant_tweet_idx]['text'])
            tweet_tokenized = nltk.word_tokenize(tweet_tokenized)
            tweet_tokenized = nltk.pos_tag(tweet_tokenized)
            
            phrases = get_full_phrases(tweet_tokenized)
        
            for phrase in phrases:
                if is_valid_noms(phrase):
                    idx = already_found(phrase, potential_noms)
                    if idx != -1:
                        potential_noms[idx][1] += 1
                    else:
                      
                        potential_noms.append([phrase, 1])
                        
        tmp = []      
        tmp.append(top_five(potential_noms, cat))
        
        
        while isinstance(tmp[0][0], list):
            tmp = tmp[0]
        
        apnd = []
        for n in tmp:
             apnd.append(" ".join(n))
        
        

        nominees.append(apnd)
        
        
    
        
                        
    return nominees
            







# print(get_hosts("/Users/joshlevitas/Desktop/School/CS_337/project 1 data/gg2013.json"))
print(get_nominees("/Users/joshlevitas/Desktop/School/CS_337/project 1 data/gg2013.json", categories, cat_filters("/Users/joshlevitas/Desktop/processed_tweets_2.csv")))

#THERE ARE ALWAYS 5 Nominees
# print(already_there("Django",['Django', 'Unchained']))
# print(top_five([[['Hb'], 1], [['Dbn'], 1], [['Lk'], 1], [['Justice'], 1], [['Mike', 'Hamad', 'Heck'], 1], [['Donnie', 'Wahlberg'], 2], [['Miglior', 'Regista'], 1], [['Argo', 'Miglior', 'Film'], 1], [['Hahahahahahahah'], 1], [['Glória', 'Pires'], 2], [['Huffington', 'Post'], 7], [['Becb'], 1], [['Jacques-', 'Cartier'], 1], [['Justiceto', 'Film'], 1], [['Food', 'Dood'], 1], [['”', '/they'], 1], [['Lincoln'], 100], [["L'ultra"], 1], [['Ultimo'], 1]],0))