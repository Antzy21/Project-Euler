## From Uni - Number Theory Year 3
## Improved for Performace

from math import ceil, sqrt

def SieveOfErathostenes(n):
    P = [1]*n
    m = ceil(sqrt(n))
    for i in range(2,m):
        if P[i] == 1:
            for j in range(2*i,n,i):
                P[j] = 0
    P[0]=0
    P[1]=0
    return(P)