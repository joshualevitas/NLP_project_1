# Josh's and Komal's Project
Golden Globe Project Master
https://github.com/joshualevitas/NLP_project_1
https://github.com/joshualevitas/NLP_project_1
https://github.com/joshualevitas/NLP_project_1

What we need:

- A paramaterizable script for the event (roles, subevents, event tracking)
- Methods for identifying relevant tweets to specific actions / roles in the script (keywords, hashtags, regular expressions, phrasal patterns, variables in tree structured syntactic templates)
- Methods for extracting and aggregating information from those tweets to parameterize the script


Award Ceremonies
- Announcement of nominees
- Selection of Winner
- Response of Winner

Roles:
 - Host
 - Categories (and presenters in each category)
 - Nominees in each category (and who people are rooting for)
 - Winners in each category (and winner reactions)
 
 - Categories
 - Actors, Producers, Directors, Writers, etc.
 - Movies

 ^ Look for any semantic relations (i.e., you must be nominated to win, one winner for each category, one or two hosts / presenters per category)


## Plan
0.5 - write function to clean data

1. write function to sort tweets into what we want (taking categories as input) (+ put into categories, can be a separate function that stores relevant indices). Later, write a function that spits out categories

1.5. write function to get nominees

2. write function to get "votes" for each category and predict a winner

3. write functions to get "votes" for hosts, etc.



## Instructions for running

As of now, our get_hosts function seems to be working great.
To use it, call get_hosts(year) where year is the link to the json file of tweets.

There will be instructions when you try to call functions after running main. For some of the functions, we need the hardcoded list of awards that canvas mentions we will default to to avoid cascading error.

Thanks for the help.

-Komal and Josh
