import string
from reader import readfile

def preprorawcorpus(fname):
    string.punctuation=string.punctuation+'"'+'-'+"'"
    string.punctuation=string.punctuation.replace('.','')
    rawCorpus=readfile(fname)
    rawCorpus_new=""
    for line in rawCorpus:
        line_new=line.replace('n',' ')
        rawCorpus_new=rawCorpus+line_new
    processedCorpus= "".join(chr for chr in rawCorpus_new if chr not in string.punctuation)
    return processedCorpus