from nltk.tokenize import word_tokenize,sent_tokenize
from preprocourpus import preprorawcorpus

def corpustokens(fname):
    processedCorpus=preprorawcorpus(fname)
    sentences=sent_tokenize(processedCorpus)
    words=word_tokenize(processedCorpus)
    return words,sentences
