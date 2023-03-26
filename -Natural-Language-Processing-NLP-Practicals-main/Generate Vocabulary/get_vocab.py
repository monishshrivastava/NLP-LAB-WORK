def arrange_vocab(corpus_vocab):
    arranged_corpus_vocab = dict()
    sort_dict=dict()
    
    for key,value in corpus_vocab.items():
        if value in sort_dict:
            sort_dict[value].append(key)
        else:
            sort_dict[value]=list()
            sort_dict[value].append(key)
    
    for value in sort_dict.keys():
        if len(sort_dict[value])>1:
            sort_dict[value].sort()
    
    mykeys = list(sort_dict.keys())
    mykeys.sort(reverse=True)
    sort_dict = {i: sort_dict[i] for i in mykeys}
    
    for value,keys in sort_dict.items():
        for key in keys:
            arranged_corpus_vocab[key]=value
    
    return arranged_corpus_vocab


def create_vocab(corpus_tokens):
    corpus_vocab=dict()
    for token in corpus_tokens:
        if token not in corpus_vocab.keys():
            corpus_vocab[token]=1
        else:
            corpus_vocab[token]+=1
    corpus_vocab=arrange_vocab(corpus_vocab)
    return corpus_vocab
