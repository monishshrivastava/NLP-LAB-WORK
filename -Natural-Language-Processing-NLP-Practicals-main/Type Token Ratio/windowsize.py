def calc_wsize(n,fact_lst):
    wsize=fact_lst[-1]
    i=2
    max_val=int((10/100)*n)
    while wsize<max_val:
        wsize*=fact_lst[-i]
        i+=1
    return wsize

def get_wsize(n):
    c = 2
    fact_lst=[]
    n1=n
    while (n > 1):
        if (n % c == 0):
            fact_lst.append(c)
            n = n / c
        else:
            c = c + 1
    n=n1
    wsize=calc_wsize(n,fact_lst)
    return wsize