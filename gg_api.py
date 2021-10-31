import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import json 
from nltk_processing import *
'''Version 0.35'''

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    f = open(year)
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

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    




    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    return

if __name__ == '__main__':
    main()
