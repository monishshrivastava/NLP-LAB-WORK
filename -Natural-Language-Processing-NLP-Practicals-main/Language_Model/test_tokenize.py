from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def tokenize_sent(sent):
    
    token=word_tokenize(sent)
    ngram={1:[],2:[]}
    ngram[1]=list(ngrams(token,1))[-1]
    ngram[2] = list(ngrams(token, 2))[-1]
    
    return ngram