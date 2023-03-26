from unique_chrlst import getuniqchlst

#Function to read a file
def readtxtfile(fname):
    text_file = open(fname)
    text = text_file.readlines()
    return text

#Function to strip certain characters
def stripuniqch(text):
    ltext = len(text)
    ftext = ""
    for i in range(ltext):
        text[i] = text[i].strip('\n')
        text[i] = text[i].strip('\t')
        ftext += text[i]+" "
    text = ftext
    del(ftext)
    return text

#Function to remove spaces
def removespace(text):
    while '  ' in text:
        text = text.replace('  ',' ')

    return text

#Function to remove non-alphanumeric characters 
def removenonalphach(text):
    chlst = getuniqchlst(text)
    for ch in chlst:
        text = text.replace(ch, ' ')
    return text

#Function to remove unique characters
def removeuniqch(text):
    text=stripuniqch(text)
    text = text.lower()
    text=removenonalphach(text)
    text=removespace(text)
    return text

#Function to Pre-process the text
def preprotxt(fname):
    text=readtxtfile(fname)
    text=removeuniqch(text)
    text=text.split()
    return text

#preprotxt('Restaurant_Reviews.txt')