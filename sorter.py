import numpy as np
import json
import pandas as pd
import re
# import requests

filepath = "/Users/joshlevitas/Desktop/School/CS_337/project 1 data/gg2013.json" #2013

#sort by keyword?

categories = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance in a motion picture - drama', 'best performance in a motion picture - musical or comedy', 'best supporting performance in a motion picture - drama, musical or comedy', 'best director', 'best screenplay', 'best original score', 'best original song', 'best animated feature film', 'best foreign language film']



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

    
    print(len(data))
    # for i in data:
    #     print(i['text'])
    
    



reader(filepath)
assert cat_typer("best picture") == 1
assert cat_typer("best performance in a motion picture - drama") == 0
