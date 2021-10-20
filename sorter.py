import numpy as np
import json
import pandas as pd
import re
# import requests

filepath = "/Users/joshlevitas/Desktop/School/CS_337/project 1 data/gg2013.json" #2013

#sort by keyword?

winner_data = {"hosts": ["amy poehler", "tina fey"], "award_data": {"best screenplay - motion picture": {"nominees": ["zero dark thirty", "lincoln", "silver linings playbook", "argo"], "presenters": ["robert pattinson", "amanda seyfried"], "winner": "django unchained"}, "best director - motion picture": {"nominees": ["kathryn bigelow", "ang lee", "steven spielberg", "quentin tarantino"], "presenters": ["halle berry"], "winner": "ben affleck"}, "best performance by an actress in a television series - comedy or musical": {"nominees": ["zooey deschanel", "tina fey", "julia louis-dreyfus", "amy poehler"], "presenters": ["aziz ansari", "jason bateman"], "winner": "lena dunham"}, "best foreign language film": {"nominees": ["the intouchables", "kon tiki", "a royal affair", "rust and bone"], "presenters": ["arnold schwarzenegger", "sylvester stallone"], "winner": "amour"}, "best performance by an actor in a supporting role in a motion picture": {"nominees": ["alan arkin", "leonardo dicaprio", "philip seymour hoffman", "tommy lee jones"], "presenters": ["bradley cooper", "kate hudson"], "winner": "christoph waltz"}, "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": {"nominees": ["hayden panettiere", "archie panjabi", "sarah paulson", "sofia vergara"], "presenters": ["dennis quaid", "kerry washington"], "winner": "maggie smith"}, "best motion picture - comedy or musical": {"nominees": ["the best exotic marigold hotel", "moonrise kingdom", "salmon fishing in the yemen", "silver linings playbook"], "presenters": ["dustin hoffman"], "winner": "les miserables"}, "best performance by an actress in a motion picture - comedy or musical": {"nominees": ["emily blunt", "judi dench", "maggie smith", "meryl streep"], "presenters": ["will ferrell", "kristen wiig"], "winner": "jennifer lawrence"}, "best mini-series or motion picture made for television": {"nominees": ["the girl", "hatfields & mccoys", "the hour", "political animals"], "presenters": ["don cheadle", "eva longoria"], "winner": "game change"}, "best original score - motion picture": {"nominees": ["argo", "anna karenina", "cloud atlas", "lincoln"], "presenters": ["jennifer lopez", "jason statham"], "winner": "life of pi"}, "best performance by an actress in a television series - drama": {"nominees": ["connie britton", "glenn close", "michelle dockery", "julianna margulies"], "presenters": ["nathan fillion", "lea michele"], "winner": "claire danes"}, "best performance by an actress in a motion picture - drama": {"nominees": ["marion cotillard", "sally field", "helen mirren", "naomi watts", "rachel weisz"], "presenters": ["george clooney"], "winner": "jessica chastain"}, "cecil b. demille award": {"nominees": [], "presenters": ["robert downey, jr."], "winner": "jodie foster"}, "best performance by an actor in a motion picture - comedy or musical": {"nominees": ["jack black", "bradley cooper", "ewan mcgregor", "bill murray"], "presenters": ["jennifer garner"], "winner": "hugh jackman"}, "best motion picture - drama": {"nominees": ["django unchained", "life of pi", "lincoln", "zero dark thirty"], "presenters": ["julia roberts"], "winner": "argo"}, "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": {"nominees": ["max greenfield", "danny huston", "mandy patinkin", "eric stonestreet"], "presenters": ["kristen bell", "john krasinski"], "winner": "ed harris"}, "best performance by an actress in a supporting role in a motion picture": {"nominees": ["amy adams", "sally field", "helen hunt", "nicole kidman"], "presenters": ["megan fox", "jonah hill"], "winner": "anne hathaway"}, "best television series - drama": {"nominees": ["boardwalk empire", "breaking bad", "downton abbey (masterpiece)", "the newsroom"], "presenters": ["salma hayek", "paul rudd"], "winner": "homeland"}, "best performance by an actor in a mini-series or motion picture made for television": {"nominees": ["benedict cumberbatch", "woody harrelson", "toby jones", "clive owen"], "presenters": ["jessica alba", "kiefer sutherland"], "winner": "kevin costner"}, "best performance by an actress in a mini-series or motion picture made for television": {"nominees": ["nicole kidman", "jessica lange", "sienna miller", "sigourney weaver"], "presenters": ["don cheadle", "eva longoria"], "winner": "julianne moore"}, "best animated feature film": {"nominees": ["frankenweenie", "hotel transylvania", "rise of the guardians", "wreck-it ralph"], "presenters": ["sacha baron cohen"], "winner": "brave"}, "best original song - motion picture": {"nominees": ["act of valor", "stand up guys", "the hunger games", "les miserables"], "presenters": ["jennifer lopez", "jason statham"], "winner": "skyfall"}, "best performance by an actor in a motion picture - drama": {"nominees": ["richard gere", "john hawkes", "joaquin phoenix", "denzel washington"], "presenters": ["george clooney"], "winner": "daniel day-lewis"}, "best television series - comedy or musical": {"nominees": ["the big bang theory", "episodes", "modern family", "smash"], "presenters": ["jimmy fallon", "jay leno"], "winner": "girls"}, "best performance by an actor in a television series - drama": {"nominees": ["steve buscemi", "bryan cranston", "jeff daniels", "jon hamm"], "presenters": ["salma hayek", "paul rudd"], "winner": "damian lewis"}, "best performance by an actor in a television series - comedy or musical": {"nominees": ["alec baldwin", "louis c.k.", "matt leblanc", "jim parsons"], "presenters": ["lucy liu", "debra messing"], "winner": "don cheadle"}}}
categories = ["best screenplay - motion picture","best director - motion picture", "best performance by an actress in a television series - comedy or musical", "best foreign language film", "best performance by an actor in a supporting role in a motion picture", "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television", "best motion picture - comedy or musical", "best performance by an actress in a motion picture - comedy or musical", "best mini-series or motion picture made for television", "best original score - motion picture","best performance by an actress in a television series - drama", "best performance by an actress in a motion picture - drama","cecil b. demille award", "best performance by an actor in a motion picture - comedy or musical", "best motion picture - drama","best performance by an actor in a supporting role in a series, mini-series or motion picture made for television", "best performance by an actress in a supporting role in a motion picture", "best television series - drama", "best performance by an actor in a mini-series or motion picture made for television", "best performance by an actress in a mini-series or motion picture made for television","best animated feature film","best original song - motion picture","best performance by an actor in a motion picture - drama", "best television series - comedy or musical","best performance by an actor in a television series - drama","best performance by an actor in a television series - comedy or musical"]



#function to guess whether a category's winner is a person or film


def cat_typer(category_name):
    #returns 1 if the winner is a movie, 0 if a person
    
    person_cats = ['performance', 'in', 'director', 'actor']
    movie_cats = ['film', 'animated', 'picture']
    person = 0
    movie = 0

    
    for key_word in person_cats:
        if key_word in category_name:
            person += 1
    for key_word in movie_cats:
        if key_word in category_name:
            movie += 1

  
    
    return 1 if movie >= person else 0
    
    

    

def reader(file):
    f = open(file)
    data = json.load(f)

    
    return len(data)
    # for i in data:
    #     print(i['text'])


# def sorter(file, categories):
#     #outputs a new array indicating which tweets are related to which categories
#     f = open(file)
#     data = json.load(f)

#     ret = [-1]*len(data)


#     for tweet in range(len(data)):
#         #guess which category the tweet is about
#         winning_cat = -1
#         max_votes = 0
#         for cat in range(len(categories)):
#             cat_words = categories[cat].split()
#             cat_votes = 0

            

#             for word in cat_words:
#                 if word in data[tweet]['text']:
#                     cat_votes += 1
                
#                 if cat_votes > max_votes:
#                     max_votes = cat_votes
#                     winning_cat = cat

#         ret[tweet] = winning_cat
             
    
#     return ret

def sorter(file, categories):
    f = open(file)
    data = json.load(f)
    ret = [-1]*len(data)
    #assume we know nominees
    for tweet in range(len(data)):
        
        for cat in range(len(categories)):
            nominees = winner_data['award_data'][categories[cat]]['nominees']
        
            for nom in nominees:
                nom_ = nom.split()
                for n in nom_:
                    #first and last names / movie title individual words
                    if n in data[tweet]['text'].lower():
                        ret[tweet] = cat


    return ret


#start with the first category, go through all of its tweets, then guess winner.
            



#function to read through tweets, look for names of nominees, "win, won, goes to", etc. 
#tally and guess (make sure that the type is correct)

#put inside shell function

def guess_winner(category, file):
    f = open(file) 
    data = json.load(f)
    pass


    

#tests





assert reader(filepath) == 174643

assert cat_typer("best picture") == 1
assert cat_typer("best performance in a motion picture - drama") == 0


# print(winner_data['award_data'][categories[3]])

x = sorter(filepath, categories)

# print(x)
def get_dist(arr):
    m = max(arr)
    new_arr = [0]*(m+1)
    for i in arr:
        new_arr[i] += 1

    return new_arr

def sum_arr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


# print(x[:100])





        
f = open(filepath) 
data = json.load(f)
c = 0
# for tweet in data:

    # if "argo" in tweet['text'].lower():
    #     c += 1
    
# print(c)

for i in range(len(x)):
    if x[i] == 2:
        print(data[i]['text'])



print(get_dist(x))

    

