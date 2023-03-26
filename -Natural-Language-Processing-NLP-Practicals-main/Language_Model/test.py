from lang_model import get_probdist
from test_tokenize import tokenize_sent
from predict3bigram import predict_next_3_words_bigram
from predict3trigram import predict_next_3_words_trigram
#from predict3trigram

#Test Sentences
testSent1 = "There was a sudden jerk, a terrific convulsion of the limbs; and there he"
testSent2 = "They made room for the stranger, but he sat down"
testSent3 = "The hungry and destitute situation of the infant orphan was duly reported by"

#Tokenization of Test Sentences
ngram_1=tokenize_sent(testSent1)
ngram_2=tokenize_sent(testSent2)
ngram_3=tokenize_sent(testSent3)

print("Sentence 1: ", ngram_1,"Sentence 2: ",ngram_2,"Sentence 3: ",ngram_3)

#The probability distribution from the corpus
fname = 'rawCorpus.txt'
smoothed_bigram_probdist,smoothed_trigram_probdist=get_probdist(fname)

#Predicting Next 3 words using smoothed bigram model
pred1,pred2 = predict_next_3_words_bigram(ngram_1[1][0],smoothed_bigram_probdist)
print(testSent1+'-'+pred1[0][0]+'-'+pred1[1][0]+'-'+pred1[2][0])
print(testSent1+'-'+pred2[0][0]+'-'+pred2[1][0]+'-'+pred2[2][0])
print()
pred1,pred2 = predict_next_3_words_bigram(ngram_2[1][0],smoothed_bigram_probdist)
print(testSent2+'-'+pred1[0][0]+'-'+pred1[1][0]+'-'+pred1[2][0])
print(testSent2+'-'+pred2[0][0]+'-'+pred2[1][0]+'-'+pred2[2][0])
print()
pred1,pred2 = predict_next_3_words_bigram(ngram_3[1][0],smoothed_bigram_probdist)
print(testSent3+'-'+pred1[0][0]+'-'+pred1[1][0]+'-'+pred1[2][0])
print(testSent3+'-'+pred2[0][0]+'-'+pred2[1][0]+'-'+pred2[2][0])
