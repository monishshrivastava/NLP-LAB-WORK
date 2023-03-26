from tokenizecorpus import corpustokens
from stopword import filter_tokens, remove_stopwords
from gramization import gramatize
from gram_freq_dist import getfreq_dist
from gram_prob_dist import get_prob_dist

def get_probdist(fname):
    # Sentence and Word Tokenization
    words, sentences = corpustokens(fname)

    # print("1st 5 sentences of the processed corpus are: ")
    # print(sentences[0:5])
    # print("1st 5 words of the processed corpus are: ")
    # print(words[0:5])

    # Word Token Flitration
    words = filter_tokens(words)

    # Gramization into Uni-, Bi- & Tri-grams
    unigrams, bigrams, trigrams = gramatize(sentences)

    # print("UNIGRAMS: "+str(unigrams[:5])+"...n")
    # print("BIGRAMS: "+str(bigrams[:5])+"...n")
    # print("TRIGRAMS: "+str(trigrams[:5])+"...n")

    #Stopword Removal
    unigrams_processed=remove_stopwords(1,unigrams)
    bigrams_processed = remove_stopwords(2, bigrams)
    trigrams_processed = remove_stopwords(3, trigrams)

    # print("UNIGRAMS: "+str(unigrams_processed[:5])+"...n")
    # print("BIGRAMS: "+str(bigrams_processed[:5])+"...n")
    # print("TRIGRAMS: "+str(trigrams_processed[:5])+"...n")

    #Frequency Distribution
    unigram_freq_dist =getfreq_dist(unigrams)
    unigram_processed_freq_dist =getfreq_dist(unigrams_processed)
    bigram_freq_dist =getfreq_dist(bigrams)
    bigram_processed_freq_dist =getfreq_dist(bigrams_processed)
    trigram_freq_dist =getfreq_dist(trigrams)
    trigram_processed_freq_dist =getfreq_dist(trigrams_processed)

    # print(unigram_freq_dist)
    # print(bigram_freq_dist)
    # print(trigram_freq_dist)
    # print(unigram_processed_freq_dist)
    # print(bigram_processed_freq_dist)
    # print(trigram_processed_freq_dist)

    #Probability Distribution by Add-1 smoothing
    smoothed_bigram_probdist,smoothed_trigram_probdist=get_prob_dist(unigram_freq_dist,bigram_freq_dist,trigram_freq_dist)
    
    return smoothed_bigram_probdist,smoothed_trigram_probdist