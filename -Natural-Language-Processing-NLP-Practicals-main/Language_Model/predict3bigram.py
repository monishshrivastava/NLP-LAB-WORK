from collections import Counter

def predict_next_word(last_word,probdist):
    next_word={}
    for k in probdist:
        if k[0]==last_word[0]:
            next_word[k[1]]=probdist[k]
    k=Counter(next_word)
    high=k.most_common(1)
    return high[0]

def predict_next_3_words_bigram(token,probdist):
    pred1=[]
    pred2=[]
    next_word={}
    print(token)
    for i in probdist:
        if i[0]==token:
            next_word[i[1]]=probdist[i]
    print(next_word)
    k=Counter(next_word)
    high=k.most_common(2)
    w1a=high[0]
    w1b=high[1]
    w2a=predict_next_word(w1a,probdist)
    w3a=predict_next_word(w2a,probdist)
    w2b=predict_next_word(w1b,probdist)
    w3b=predict_next_word(w2b,probdist)
    pred1.append(w1a)
    pred1.append(w2a)
    pred1.append(w3a)
    pred2.append(w1b)
    pred2.append(w2b)
    pred2.append(w3b)
    return pred1,pred2