import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import json 
from nltk_processing import *
from sorter import *
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
    awards = []
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    # def get_nominees(year, categories, cat_filters):
    
    return nominees


def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    
    
    f = open(year)
    data = json.load(f)
    
    nominees = get_nominees(year)
    categories = input("Please enter the hardcoded list of awards in the form of a comma separated list.")
    

    winners = []
    for cat in range(len(categories)):
        nom_votes = [0]*len(nominees[cat])

        for relevant_tweet_idx in cat_filters("processed_tweets_2.csv")[cat]:
            if gets_vote(data[relevant_tweet_idx]['text']):
                #figure out which category? maybe not
                #vote!
                for nom in range(len(nominees[cat])):
                    nom_ = [word for word in nominees[cat][nom].split() if not word in stop_words]
                    for n in nom_:
                        #first and last names / movie title individual words
                        if n in data[relevant_tweet_idx]['text'].lower():
                            nom_votes[nom] += 1
                            break

                
        # winners.append(nominees[cat][max_idx(nom_votes)])
       
        if nominees[cat] != []:
            winners.append(nominees[cat][max_idx(nom_votes)])
        else:
            winners.append(['?'])
    
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
    
    #categorizing tweets
        
    year = input("Please enter the path to the json file of tweets for the year of the year of the golden globe awards: ")

    x = sorter(year, get_awards(year))
    np.savetxt("processed_tweets_2.csv", x, fmt='%i', delimiter=',')
   
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    pre_ceremony()
    print("Hello, we're a group of two and neither of us has really done this before.")
    print("To use our functions, please see the readme for instructions.")
    print("What would you like to call?")
    print("get_hosts()")
    print("get_awards()")
    print("get_nominees)")
    print("get_winner()")
    print("get_presenters()")


    c = input("Please enter your choice.")
    if c == "get_hosts()":
        c = input("Please link the json file of tweets:")
        print(get_hosts(c))
    if c == "get_awards()":
        print("Sorry, we couldn't figure this one out enough to submit something we were proud of.")
    if c == "get_nominees()":
        c = input("Please link the json file of tweets:")
        print(get_nominees(c))
    if c == "get_winner()":
        c = input("Please link the json file of tweets:")
        print(get_winner(c))
    if c == "get_presenters()":
        c = input("Please link the json file of tweets:")
        print(get_presenters(c))
    




    

    



    return

if __name__ == '__main__':
    main()

def sorter(year, categories):
    #categorizing tweets
    f = open(year)
    data = json.load(f)
    ret = np.zeros(shape=(len(data),len(categories)), dtype=int)
   
    #assume we know nominees
    for tweet in range(len(data)):
        

        for cat in range(len(categories)):
            
            
            nominees = get_nominees(year)
            for n in nominees:
                nominees.append(n)
            
    
            ###
            



            for nom in nominees:
                nom_ = [word for word in nom.split() if not word in stop_words]
                for n in nom_:
                    #first and last names / movie title individual words
                    if n in data[tweet]['text'].lower():
                        ret[tweet][cat] = 1




    return ret





