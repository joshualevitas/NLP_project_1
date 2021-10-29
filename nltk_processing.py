import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# pattern = 'NP: {<DT>?<JJ>*<NN>}'
# cp = nltk.RegexpParser(pattern)

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





## tests
txt = "Jennifer Lopez's dress is jaw Argo droppingly amazing #GoldenGlobes #redcarpet"
print(preprocess(txt))