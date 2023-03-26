from prepro import preprotxt
from get_vocab import create_vocab
from windowsize import get_wsize

def get_old_ttr(vocab_size, corpus_size):
    return vocab_size/corpus_size

def get_new_ttr(corpus_tokens, corpus_size):
    wsize=get_wsize(corpus_size)
    nwin=int(corpus_size//wsize)
    new_ttr=0
    for i in range(nwin-1):
        curr_vocab=create_vocab(corpus_tokens[i*wsize:(i+1)*wsize])
        new_ttr+=(len(curr_vocab)/wsize)
    new_ttr/=nwin
    return new_ttr

#Get the File Namr
fname = input("Enter the filename with '.txt' extension: ")

#Tokenize the Corpus
corpus_tokens = preprotxt(fname)
corpus_size=len(corpus_tokens)

#Create the Vocabulary
corpus_vocab=create_vocab(corpus_tokens)
vocab_size=len(corpus_vocab)

print(f'Corpus Size: {corpus_size}\nVocab Size: {vocab_size}',end='\n\n')

#Get Old TTR
old_ttr=get_old_ttr(vocab_size,corpus_size)
print(f"Type-Token Ratio by old method: {old_ttr*100} %",end='\n\n')

#Get New TTR
new_ttr=get_new_ttr(corpus_tokens,corpus_size)
print(f"Type-Token Ratio by new method: {new_ttr*100} %")