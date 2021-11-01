import numpy as np
import json
import pandas as pd
import string 
import re
from bs4 import BeautifulSoup
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

filepath = "/Users/apple/Downloads/NLP_FALL2021/gg2013.json" #2013

winner_data = {"hosts": ["amy poehler", "tina fey"], "award_data": {"best screenplay - motion picture": {"nominees": ["zero dark thirty", "lincoln", "silver linings playbook", "argo"], "presenters": ["robert pattinson", "amanda seyfried"], "winner": "django unchained"}, "best director - motion picture": {"nominees": ["kathryn bigelow", "ang lee", "steven spielberg", "quentin tarantino"], "presenters": ["halle berry"], "winner": "ben affleck"}, "best performance by an actress in a television series - comedy or musical": {"nominees": ["zooey deschanel", "tina fey", "julia louis-dreyfus", "amy poehler"], "presenters": ["aziz ansari", "jason bateman"], "winner": "lena dunham"}, "best foreign language film": {"nominees": ["the intouchables", "kon tiki", "a royal affair", "rust and bone"], "presenters": ["arnold schwarzenegger", "sylvester stallone"], "winner": "amour"}, "best performance by an actor in a supporting role in a motion picture": {"nominees": ["alan arkin", "leonardo dicaprio", "philip seymour hoffman", "tommy lee jones"], "presenters": ["bradley cooper", "kate hudson"], "winner": "christoph waltz"}, "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": {"nominees": ["hayden panettiere", "archie panjabi", "sarah paulson", "sofia vergara"], "presenters": ["dennis quaid", "kerry washington"], "winner": "maggie smith"}, "best motion picture - comedy or musical": {"nominees": ["the best exotic marigold hotel", "moonrise kingdom", "salmon fishing in the yemen", "silver linings playbook"], "presenters": ["dustin hoffman"], "winner": "les miserables"}, "best performance by an actress in a motion picture - comedy or musical": {"nominees": ["emily blunt", "judi dench", "maggie smith", "meryl streep"], "presenters": ["will ferrell", "kristen wiig"], "winner": "jennifer lawrence"}, "best mini-series or motion picture made for television": {"nominees": ["the girl", "hatfields & mccoys", "the hour", "political animals"], "presenters": ["don cheadle", "eva longoria"], "winner": "game change"}, "best original score - motion picture": {"nominees": ["argo", "anna karenina", "cloud atlas", "lincoln"], "presenters": ["jennifer lopez", "jason statham"], "winner": "life of pi"}, "best performance by an actress in a television series - drama": {"nominees": ["connie britton", "glenn close", "michelle dockery", "julianna margulies"], "presenters": ["nathan fillion", "lea michele"], "winner": "claire danes"}, "best performance by an actress in a motion picture - drama": {"nominees": ["marion cotillard", "sally field", "helen mirren", "naomi watts", "rachel weisz"], "presenters": ["george clooney"], "winner": "jessica chastain"}, "cecil b. demille award": {"nominees": [], "presenters": ["robert downey, jr."], "winner": "jodie foster"}, "best performance by an actor in a motion picture - comedy or musical": {"nominees": ["jack black", "bradley cooper", "ewan mcgregor", "bill murray"], "presenters": ["jennifer garner"], "winner": "hugh jackman"}, "best motion picture - drama": {"nominees": ["django unchained", "life of pi", "lincoln", "zero dark thirty"], "presenters": ["julia roberts"], "winner": "argo"}, "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": {"nominees": ["max greenfield", "danny huston", "mandy patinkin", "eric stonestreet"], "presenters": ["kristen bell", "john krasinski"], "winner": "ed harris"}, "best performance by an actress in a supporting role in a motion picture": {"nominees": ["amy adams", "sally field", "helen hunt", "nicole kidman"], "presenters": ["megan fox", "jonah hill"], "winner": "anne hathaway"}, "best television series - drama": {"nominees": ["boardwalk empire", "breaking bad", "downton abbey (masterpiece)", "the newsroom"], "presenters": ["salma hayek", "paul rudd"], "winner": "homeland"}, "best performance by an actor in a mini-series or motion picture made for television": {"nominees": ["benedict cumberbatch", "woody harrelson", "toby jones", "clive owen"], "presenters": ["jessica alba", "kiefer sutherland"], "winner": "kevin costner"}, "best performance by an actress in a mini-series or motion picture made for television": {"nominees": ["nicole kidman", "jessica lange", "sienna miller", "sigourney weaver"], "presenters": ["don cheadle", "eva longoria"], "winner": "julianne moore"}, "best animated feature film": {"nominees": ["frankenweenie", "hotel transylvania", "rise of the guardians", "wreck-it ralph"], "presenters": ["sacha baron cohen"], "winner": "brave"}, "best original song - motion picture": {"nominees": ["act of valor", "stand up guys", "the hunger games", "les miserables"], "presenters": ["jennifer lopez", "jason statham"], "winner": "skyfall"}, "best performance by an actor in a motion picture - drama": {"nominees": ["richard gere", "john hawkes", "joaquin phoenix", "denzel washington"], "presenters": ["george clooney"], "winner": "daniel day-lewis"}, "best television series - comedy or musical": {"nominees": ["the big bang theory", "episodes", "modern family", "smash"], "presenters": ["jimmy fallon", "jay leno"], "winner": "girls"}, "best performance by an actor in a television series - drama": {"nominees": ["steve buscemi", "bryan cranston", "jeff daniels", "jon hamm"], "presenters": ["salma hayek", "paul rudd"], "winner": "damian lewis"}, "best performance by an actor in a television series - comedy or musical": {"nominees": ["alec baldwin", "louis c.k.", "matt leblanc", "jim parsons"], "presenters": ["lucy liu", "debra messing"], "winner": "don cheadle"}}}
categories = ["best screenplay - motion picture","best director - motion picture", "best performance by an actress in a television series - comedy or musical", "best foreign language film", "best performance by an actor in a supporting role in a motion picture", "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television", "best motion picture - comedy or musical", "best performance by an actress in a motion picture - comedy or musical", "best mini-series or motion picture made for television", "best original score - motion picture","best performance by an actress in a television series - drama", "best performance by an actress in a motion picture - drama","cecil b. demille award", "best performance by an actor in a motion picture - comedy or musical", "best motion picture - drama","best performance by an actor in a supporting role in a series, mini-series or motion picture made for television", "best performance by an actress in a supporting role in a motion picture", "best television series - drama", "best performance by an actor in a mini-series or motion picture made for television", "best performance by an actress in a mini-series or motion picture made for television","best animated feature film","best original song - motion picture","best performance by an actor in a motion picture - drama", "best television series - comedy or musical","best performance by an actor in a television series - drama","best performance by an actor in a television series - comedy or musical"]
movies = ["motion","picture","movie"]
stop_words = ['to', '-', 'the', 'in', 'not', 'too', 'best']
win_words = ["won", "goes to", "win"] #add more if necessary
nominee_words = ["nominate","was nominated","nominating","nominated.","nominated","nominees"]
nom_keywords = ["for","best","in","nominee"]
nom_keywords1 = ["by","is","for","are"]
final_nom_cat = ["actor","director","movie","actress","tv","series","screenplay","comedy","foreign","picture","film","role","score"]
final_nom_cat1 = ["actor","director","movie","actress","tv","series","screenplay","comedy","foreign","picture","film","role","score","musical","language","mini-series","drama","demille","animated"]

nominee_word=["nominated"]
movie_list = ["film"]
director_list = ["directing"]
presenter_list = ["present","presenting","presented","presenter","presenters"]


###

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
    
    


def sorter(file, categories):
    #categorizing tweets
    f = open(file)
    data = json.load(f)
    ret = np.zeros(shape=(len(data),len(categories)), dtype=int)
   
    #assume we know nominees
    for tweet in range(len(data)):
        

        for cat in range(len(categories)):
            
            
            ### REWORK AFTER STEP 1
            nominees_ = winner_data['award_data'][categories[cat]]['nominees'] #rewrite line to get_nominees(...)
            # nominees.append(winner_data['award_data'][categories[cat]]['winner'])
            # print(nominees)
            winner = winner_data['award_data'][categories[cat]]['winner']
            nominees = [winner]
            for n in nominees_:
                nominees.append(n)
            
    
            ###
            



            for nom in nominees:
                nom_ = [word for word in nom.split() if not word in stop_words]
                for n in nom_:
                    #first and last names / movie title individual words
                    if n in data[tweet]['text'].lower():
                        ret[tweet][cat] = 1




    return ret







def cat_filters(csv):
    data = pd.read_csv(csv, header=None)
    index = data.index
    #init array of size len(catagories), ?*
    ret = []
    for i in range(len(categories)):
        ret.append(index[data[i]==1])

    return ret







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

def get_nomination_cat(doc):
    cate=0
    for k in nom_keywords:
        if k in doc:
            cate=doc.index(k)
            if(cate):
                break
    if cate != 0:
        d=doc[cate:]
        #d=doc
        str = ' '.join(d)
        s_nlp=nlp(str)
        
        commonNouns = [token.text for token in s_nlp if token.pos_ =='NOUN']
        for c in final_nom_cat:
            if any(c in s for s in commonNouns):
                return c
    return ""

def get_presenter_cat(doc):
    cate=0
    for k in nom_keywords:
        if k in doc:
            cate=doc.index(k)
            if(cate):
                break
    if cate != 0:
        d=doc[cate:]
        #d=doc
        str = ' '.join(d)
        s_nlp=nlp(str)
        
        commonNouns = [token.text for token in s_nlp if token.pos_ =='NOUN']
        for c in final_nom_cat1:
            if any(c in s for s in commonNouns):
                return c
    return ""


def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)


def guess_presenters(file, categories, category_filters):
    f = open(file)
    data = json.load(f)
    
    #print("TTTTT",type(data))
    # data=str(data)
    # for dg in data:
    #     data=list(strip_all_entities(strip_links(dg)))


    presenters = {}
    #for cat in range(len(final_nom_cat1)):


    for d in data:
        doc = d['text'].lower().split()
        
        for i,nw in enumerate(presenter_list):    
            if nw in doc:
                index=doc.index(nw)
                
                dw=doc[:index]
                #dw = list(re.sub(r"@:", "", str(dw)))
                str1 = ' '.join(dw)
                cate=get_presenter_cat(doc)
                sents = nlp(str1) 
                list_=[ee for ee in sents.ents if ee.label_ == 'PERSON']
                list_ = [s.text.strip() for s in list_]
                prefixes = ('rt','@')
                list_ = [x for x in list_ if not x.startswith(prefixes)]
                if len(list_)>0 and cate:
                    #print("NW:",nw,"ACTOR:",list_,"CATEGORY: ",cate,"TWEET",d['text'])
                    if cate in presenters:
                        
                        x = presenters[cate]
                        x.extend(list_)
                        presenters[cate]=list(set(x))
                    else:
                        presenters[cate] = list_
    print(presenters)



def guess_nominees(file, categories, category_filters):
    f = open(file)
    data = json.load(f)
    


    nominees = {}
    for cat in range(len(final_nom_cat)):


        for d in data:
            #print(data[fil]['text'])
            doc = d['text'].lower().split()
            #if any([word in data[fil]['text'] for word in nominee_word]):
            #if any(nominee_word[0] in s for s in doc):
                #print(doc)
                #print(data[fil]['text'])
                
            #if data[fil]['text'].split() in (nominee_words):
            for i,nw in enumerate(nominee_words):    
                #print(nw)
                if nw in doc:
                    #print(nw)
                    index=doc.index(nw)
                    #index2=doc.index(nw)-2
                    #index3=doc.index(nw)-3
                    #print(doc[index1],doc[index2],doc[index3])
                    #str1=doc[index3] + " " + doc[index2] + " " + doc[index1]
                    dw=doc[:index]
                    str1 = ' '.join(dw)
                    #print("STRINGGGG",str1)
                    # n1=nlp(doc[index1])
                    # n2=nlp(doc[index2])
                    # n3=nlp(doc[index3])
                    #commonNouns=[]
                    cate=get_nomination_cat(doc)
                    

                    # if "best" in doc:
                    #     cate=doc[doc.index("best")+1]


    #             print(doc)
    #             print([(X.text, X.label_) for X in doc.ents])
                    sents = nlp(str1) 
                    list_=[ee for ee in sents.ents if ee.label_ == 'PERSON']
                    list_ = [s.text.strip() for s in list_]
                    prefixes=('rt','@')
                    list_ = [x for x in list_ if not x.startswith(prefixes)]
                    # if cate == 'movie':
                    #     list_=[token.text for token in sents if token.pos_ =='NOUN']
                    #     list_ = [s.strip() for s in list_]
                    
                    # if len(list_)>0 and cate:
                    #     print("NW:",nw,"ACTOR:",list_,"CATEGORY: ",cate)
                    if len(list_)>0 and cate:
                        #print("NW:",nw,"ACTOR:",list_,"CATEGORY: ",cate,"TWEET",data[fil]['text'])
                        #print("NW:",nw,"ACTOR:",list_,"CATEGORY: ",cate,"TWEET",d['text'])
                        
                        if cate in nominees:
                            
                            x = nominees[cate]
                            x.extend(list_)
                            nominees[cate]=list(set(x))
                        else:
                            nominees[cate] = list_
    print(nominees)
                # nouns = []
                # for token in doc:
                #     print(token)
                #     if token.pos_ == 'NOUN':
                #         nouns.append(token)
                # print(nouns)

                
    #     # winners.append(nominees[cat][max_idx(nom_votes)])
       
    #     if nominees[cat] != []:
    #         winners.append(nominees[cat][max_idx(nom_votes)])
    #     else:
    #         winners.append(['?'])
    
    # return winners








# def guess_winner(file, categories, category_filters, nominees):
#     f = open(file)
#     data = json.load(f)
    


#     winners = []
#     for cat in range(len(categories)):
#         nom_votes = [0]*len(nominees[cat])

#         for relevant_tweet_idx in category_filters[cat]:
#             if gets_vote(data[relevant_tweet_idx]['text']):
#                 #figure out which category? maybe not
#                 #vote!
#                 for nom in range(len(nominees[cat])):
#                     nom_ = [word for word in nominees[cat][nom].split() if not word in stop_words]
#                     for n in nom_:
#                         #first and last names / movie title individual words
#                         if n in data[relevant_tweet_idx]['text'].lower():
#                             nom_votes[nom] += 1
#                             break

                
#         # winners.append(nominees[cat][max_idx(nom_votes)])
       
#         if nominees[cat] != []:
#             winners.append(nominees[cat][max_idx(nom_votes)])
#         else:
#             winners.append(['?'])
    
#     return winners
        

        #look at each relevant tweet, vote for winner?
        
            
    

    

#tests







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








x = sorter(filepath, categories)
np.savetxt("processed_tweets.csv", x, delimiter=",")

    
# for cat in categories:
#     print(winner_data['award_data'][cat]['nominees'])
# print(len(organize_nominees()))
# print(organize_nominees()[13])


truths = organize_winners()
guesses = guess_nominees(filepath, categories, cat_filters("/Users/apple/Downloads/NLP_FALL2021/NLP_project_2/NLP_project_1/processed_tweets.csv"))
guesses1 = guess_presenters(filepath, categories, cat_filters("/Users/apple/Downloads/NLP_FALL2021/NLP_project_2/NLP_project_1/processed_tweets.csv"))

# denom = len(truths)
# numir = 0

# for i in range(len(truths)):
#     if truths[i] == guesses[i]:
#         numir += 1

# print(numir/denom)

# print(organize_nominees())