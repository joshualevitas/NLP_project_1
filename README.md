# Josh's and Komal's Project
Golden Globe Project Master

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