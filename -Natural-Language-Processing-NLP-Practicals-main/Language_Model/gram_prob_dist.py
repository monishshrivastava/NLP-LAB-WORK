def get_prob_dist(unigram_freqdist,bigram_freqdist,trigram_freqdist):
    smoothed_bigram_probdist={}
    v=len(unigram_freqdist)
    
    for i in bigram_freqdist:
        smoothed_bigram_probdist[i]=(bigram_freqdist[i]+1)/(unigram_freqdist[i[0]]+v)
    
    smoothed_trigram_probdist={}
    for i in trigram_freqdist:
        smoothed_trigram_probdist[i]=(trigram_freqdist[i]+1)/(bigram_freqdist[i[0:2]]+v)
        
    return smoothed_bigram_probdist,smoothed_trigram_probdist