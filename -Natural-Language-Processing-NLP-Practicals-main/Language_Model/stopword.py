from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def filter_tokens(words):
    filtered_tokens=[w for w in words if not w.lower() in stop_words]
    return filtered_tokens


def remove_stopwords(n, gram):
    processed_gram = []
    
    def checkword(count,word):
        if word in stop_words:
            count = count or 0
        else:
            count = count or 1
        return count
    
    def appendobj(count,obj):
        if (count == 1):
            processed_gram.append(obj)
    
    if n == 1:
        count=0
        for word in gram:
            count=checkword(count,word)
            appendobj(count,word)
    else:
        for pair in gram:
            count = 0
            for word in pair:
                count=checkword(count,word)
            appendobj(count,pair)
    
    return (processed_gram)
