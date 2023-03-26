from nltk import word_tokenize
from nltk.util import ngrams

def gramatize(sentences):
    unigrams=[]
    bigrams=[]
    trigrams=[]
    
    for content in sentences:
        content=content.lower()
        content=word_tokenize(content)
        for word in content:
            if word=='.':
                content.remove(word)
            else:
                unigrams.append(word)
        bigrams.extend(ngrams(content,2))
        trigrams.extend(ngrams(content,3))
    
    return unigrams,bigrams,trigrams
