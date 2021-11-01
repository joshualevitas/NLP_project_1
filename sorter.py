
from nltk.featstruct import _retract_bindings
import numpy as np
import json
import pandas as pd
import re
from bs4 import BeautifulSoup
import nltk

from gg_apifake import get_nominees

filepath = "/Users/joshlevitas/Desktop/School/CS_337/project 1 data/gg2013.json" #2013

winner_data = {"hosts": ["amy poehler", "tina fey"], "award_data": {"best screenplay - motion picture": {"nominees": ["zero dark thirty", "lincoln", "silver linings playbook", "argo"], "presenters": ["robert pattinson", "amanda seyfried"], "winner": "django unchained"}, "best director - motion picture": {"nominees": ["kathryn bigelow", "ang lee", "steven spielberg", "quentin tarantino"], "presenters": ["halle berry"], "winner": "ben affleck"}, "best performance by an actress in a television series - comedy or musical": {"nominees": ["zooey deschanel", "tina fey", "julia louis-dreyfus", "amy poehler"], "presenters": ["aziz ansari", "jason bateman"], "winner": "lena dunham"}, "best foreign language film": {"nominees": ["the intouchables", "kon tiki", "a royal affair", "rust and bone"], "presenters": ["arnold schwarzenegger", "sylvester stallone"], "winner": "amour"}, "best performance by an actor in a supporting role in a motion picture": {"nominees": ["alan arkin", "leonardo dicaprio", "philip seymour hoffman", "tommy lee jones"], "presenters": ["bradley cooper", "kate hudson"], "winner": "christoph waltz"}, "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": {"nominees": ["hayden panettiere", "archie panjabi", "sarah paulson", "sofia vergara"], "presenters": ["dennis quaid", "kerry washington"], "winner": "maggie smith"}, "best motion picture - comedy or musical": {"nominees": ["the best exotic marigold hotel", "moonrise kingdom", "salmon fishing in the yemen", "silver linings playbook"], "presenters": ["dustin hoffman"], "winner": "les miserables"}, "best performance by an actress in a motion picture - comedy or musical": {"nominees": ["emily blunt", "judi dench", "maggie smith", "meryl streep"], "presenters": ["will ferrell", "kristen wiig"], "winner": "jennifer lawrence"}, "best mini-series or motion picture made for television": {"nominees": ["the girl", "hatfields & mccoys", "the hour", "political animals"], "presenters": ["don cheadle", "eva longoria"], "winner": "game change"}, "best original score - motion picture": {"nominees": ["argo", "anna karenina", "cloud atlas", "lincoln"], "presenters": ["jennifer lopez", "jason statham"], "winner": "life of pi"}, "best performance by an actress in a television series - drama": {"nominees": ["connie britton", "glenn close", "michelle dockery", "julianna margulies"], "presenters": ["nathan fillion", "lea michele"], "winner": "claire danes"}, "best performance by an actress in a motion picture - drama": {"nominees": ["marion cotillard", "sally field", "helen mirren", "naomi watts", "rachel weisz"], "presenters": ["george clooney"], "winner": "jessica chastain"}, "cecil b. demille award": {"nominees": [], "presenters": ["robert downey, jr."], "winner": "jodie foster"}, "best performance by an actor in a motion picture - comedy or musical": {"nominees": ["jack black", "bradley cooper", "ewan mcgregor", "bill murray"], "presenters": ["jennifer garner"], "winner": "hugh jackman"}, "best motion picture - drama": {"nominees": ["django unchained", "life of pi", "lincoln", "zero dark thirty"], "presenters": ["julia roberts"], "winner": "argo"}, "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": {"nominees": ["max greenfield", "danny huston", "mandy patinkin", "eric stonestreet"], "presenters": ["kristen bell", "john krasinski"], "winner": "ed harris"}, "best performance by an actress in a supporting role in a motion picture": {"nominees": ["amy adams", "sally field", "helen hunt", "nicole kidman"], "presenters": ["megan fox", "jonah hill"], "winner": "anne hathaway"}, "best television series - drama": {"nominees": ["boardwalk empire", "breaking bad", "downton abbey (masterpiece)", "the newsroom"], "presenters": ["salma hayek", "paul rudd"], "winner": "homeland"}, "best performance by an actor in a mini-series or motion picture made for television": {"nominees": ["benedict cumberbatch", "woody harrelson", "toby jones", "clive owen"], "presenters": ["jessica alba", "kiefer sutherland"], "winner": "kevin costner"}, "best performance by an actress in a mini-series or motion picture made for television": {"nominees": ["nicole kidman", "jessica lange", "sienna miller", "sigourney weaver"], "presenters": ["don cheadle", "eva longoria"], "winner": "julianne moore"}, "best animated feature film": {"nominees": ["frankenweenie", "hotel transylvania", "rise of the guardians", "wreck-it ralph"], "presenters": ["sacha baron cohen"], "winner": "brave"}, "best original song - motion picture": {"nominees": ["act of valor", "stand up guys", "the hunger games", "les miserables"], "presenters": ["jennifer lopez", "jason statham"], "winner": "skyfall"}, "best performance by an actor in a motion picture - drama": {"nominees": ["richard gere", "john hawkes", "joaquin phoenix", "denzel washington"], "presenters": ["george clooney"], "winner": "daniel day-lewis"}, "best television series - comedy or musical": {"nominees": ["the big bang theory", "episodes", "modern family", "smash"], "presenters": ["jimmy fallon", "jay leno"], "winner": "girls"}, "best performance by an actor in a television series - drama": {"nominees": ["steve buscemi", "bryan cranston", "jeff daniels", "jon hamm"], "presenters": ["salma hayek", "paul rudd"], "winner": "damian lewis"}, "best performance by an actor in a television series - comedy or musical": {"nominees": ["alec baldwin", "louis c.k.", "matt leblanc", "jim parsons"], "presenters": ["lucy liu", "debra messing"], "winner": "don cheadle"}}}
categories = ["best screenplay - motion picture","best director - motion picture", "best performance by an actress in a television series - comedy or musical", "best foreign language film", "best performance by an actor in a supporting role in a motion picture", "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television", "best motion picture - comedy or musical", "best performance by an actress in a motion picture - comedy or musical", "best mini-series or motion picture made for television", "best original score - motion picture","best performance by an actress in a television series - drama", "best performance by an actress in a motion picture - drama","cecil b. demille award", "best performance by an actor in a motion picture - comedy or musical", "best motion picture - drama","best performance by an actor in a supporting role in a series, mini-series or motion picture made for television", "best performance by an actress in a supporting role in a motion picture", "best television series - drama", "best performance by an actor in a mini-series or motion picture made for television", "best performance by an actress in a mini-series or motion picture made for television","best animated feature film","best original song - motion picture","best performance by an actor in a motion picture - drama", "best television series - comedy or musical","best performance by an actor in a television series - drama","best performance by an actor in a television series - comedy or musical"]
sorting_categories = ["screenplay","director", "actress television series - comedy or musical", "foreign", "supporting actor", "actress supporting", "comedy musical", "best actress comedy or musical", "mini series television", " original score","actress in a television series - drama", "actress in a motion picture","cecil b. demille award", "actor comedy or musical", "best drama","actor in a supporting role in a series, mini-series television", "best performance by an actress in a supporting role in a motion picture", "best television series - drama", "best performance by an actor in a mini-series or motion picture made for television", "best performance by an actress in a mini-series or motion picture made for television","best animated feature film","best original song - motion picture","best performance by an actor in a motion picture - drama", "best television series - comedy or musical","best performance by an actor in a television series - drama","best performance by an actor in a television series - comedy or musical"]


stop_words = ['to', '-', 'the', 'in', 'not', 'too', 'best']
win_words = ["won", "goes to", "win"] #add more if necessary


###

def cat_typer(category_name):
    #returns 1 if the winner is a movie, 0 if a person
    
    person_cats = ['performance', 'in', 'director', 'actor']
    movie_cats = ['film', 'animated']
    person = 0
    movie = 0

    
    for key_word in person_cats:
        if key_word in category_name:
            person += 1
    for key_word in movie_cats:
        if key_word in category_name:
            movie += 1

  
    return 1 if movie >= person else 0

# print(cat_typer(categories[1]))






    


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




# x = sorter(filepath, categories)
# np.savetxt("processed_tweets_2.csv", x, fmt='%i', delimiter=',')


def cat_filters(csv):
    data = pd.read_csv(csv, header=None)
    index = data.index
    #init array of size len(catagories), ?*
    ret = []
    for i in range(len(categories)):
        ret.append(index[data[i]==1])

    return ret

def read_cat_filters(csv, categories):
    ret = []
    for i in range(len(categories)):
        ret.append([])

    with open(csv) as f:
        idx = 0
        for line in f.readlines():
            x = line
            ret[int(x)].append(idx)
            idx += 1

    return ret



    # data = pd.read_csv(csv, header=None)
    # print(data[0])

    # ret = []
    # return ret



# x = read_cat_filters("/Users/joshlevitas/Desktop/processed_tweets.csv", categories)
# sum = 0
# for i in x:
#     sum += len(i)

# print(sum)







def gets_vote(tweet_text):
    #returns 1 if tweet gets to vote for winner, 0 otherwise (1 if it contains "win", "won", etc.)
    for word in win_words:
        gets_vote = re.search(word, tweet_text)
        if gets_vote: return 1
    return 0 



#function to read through tweets, look for names of nominees, "win, won, goes to", etc. 
#tally and guess (make sure that the type is correct)

#put inside shell function

def max_idx(arr):
    max = 0
    max_idx = 0
    for elt in range(len(arr)):
        if arr[elt] > max:
            max = arr[elt]
            max_idx = elt
    return max_idx





def guess_winner(file, categories, category_filters, nominees):
    f = open(file)
    data = json.load(f)
    


    winners = []
    for cat in range(len(categories)):
        nom_votes = [0]*len(nominees[cat])

        for relevant_tweet_idx in category_filters[cat]:
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
        

        #look at each relevant tweet, vote for winner?
        
            
    




    

# tests #### 







assert cat_typer("best picture") == 1
assert cat_typer("best performance in a motion picture - drama") == 0




# print(x)
def get_dist(arr):
    cat_totals = np.zeros(len(arr[0]))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                cat_totals[j] += 1
    return cat_totals


def organize_nominees():
    ret = []
    for i in range(len(categories)):

        tmp = winner_data["award_data"][categories[i]]['nominees']
        tmp.append(winner_data["award_data"][categories[i]]['winner'])
        ret.append(tmp)

    
    return ret

def organize_winners():
    ret = []
    for i in range(len(categories)):
        ret.append(winner_data["award_data"][categories[i]]['winner'])
    
    return ret

