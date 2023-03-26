def readfile(fname):
    corpusfile= open(fname,'r')
    rawcorpus=corpusfile.read()
    # print(f"Total no. of characters in read dataset: {len(rawCorpus)}")
    return rawcorpus