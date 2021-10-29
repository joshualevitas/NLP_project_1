import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent



## tests
txt = "Jennifer Lopez's dress is jaw droppingly amazing #GoldenGlobes #redcarpet"
print(preprocess(txt))