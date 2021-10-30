import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import json 

# pattern = 'NP: {<DT>?<JJ>*<NN>}'
# cp = nltk.RegexpParser(pattern)
stop_words = ['@', 'Golden', 'Globes', 'RT', 'GoldenGlobes']

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


def is_valid(proper_noun):
    words = proper_noun.split()
    for word in words:
        if word in stop_words:
            return False
    return True

def get_full_name(name, potential_hosts):
    for person in potential_hosts:
        if len(person.split()) == 2:
            if name in person:
                return person

    return name



## tests
txt = "Jennifer Lopez's dress is jaw Argo droppingly amazing #GoldenGlobes #redcarpet"
# print(preprocess(txt))


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
            print(potential_hosts[p_host] + ", " + get_full_name(potential_hosts[p_host], potential_hosts))
            potential_hosts[p_host] = get_full_name(potential_hosts[p_host], potential_hosts)


    hosts.append(max(set(potential_hosts), key = potential_hosts.count))
    
    for p_host in potential_hosts:
        if p_host == hosts[0]:
            potential_hosts.remove(p_host)
    
    hosts.append(max(set(potential_hosts), key = potential_hosts.count))


            
    return hosts
                    

                



print(get_hosts("/Users/joshlevitas/Desktop/School/CS_337/project 1 data/gg2013.json"))
