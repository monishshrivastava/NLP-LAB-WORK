from collections import Counter


def predict_next_word(last_word,probdist):
    next_word = {}
    for k in probdist:
        if k[0:2] == last_word:
            next_word[k[2]] = probdist[k]
    k = Counter(next_word)
    high = k.most_common(1)
    return high[0]

def predict_next_3_words_trigram(token, probdist):
    return 0