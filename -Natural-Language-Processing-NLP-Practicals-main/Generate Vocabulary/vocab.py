from prepro import preprotxt
from get_vocab import create_vocab

#Get the File Namr
fname = input("Enter the filename with '.txt' extension: ")

#Tokenize the Corpus
coupus_tokens = preprotxt(fname)

#Create the Vocabulary
corpus_vocab=create_vocab(coupus_tokens)
print(corpus_vocab)
