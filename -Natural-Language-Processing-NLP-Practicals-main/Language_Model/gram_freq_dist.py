def getfreq_dist(gramlst):
    ngram_freq_dict={}
    for gram in gramlst:
        if gram in ngram_freq_dict:
            ngram_freq_dict[gram]+=1
        else:
            ngram_freq_dict[gram] = 1
    
    return ngram_freq_dict