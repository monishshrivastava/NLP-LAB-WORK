
def check_uniqch(text):
    chlst = list()
    alphalst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for ch in text:
        if ch not in alphalst and ch not in chlst:
            chlst.append(ch)
    return chlst

def getuniqchlst(text):
    chlst=check_uniqch(text)
    chlst.remove(' ')
    chlst.remove("'")
    chlst+=["'re","'m","'ll", "'s", "'nt", "'t", "'d","'ve","'",'?']
    # print(chlst)
    return chlst

