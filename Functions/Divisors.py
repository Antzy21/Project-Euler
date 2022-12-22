from math import ceil, sqrt
from Functions.NumbersFromBitArray import NumsFromBits

def Divisors(n):
    m = ceil(sqrt(n))
    D = [0]*n
    for x in range(1, m):
        if n % x == 0:
            D[x-1] = 1
            D[n//x-1] = 1
    return D

def getDivisors(n):
    D = Divisors(n)
    return NumsFromBits(D)

def getProperDivisors(n):
    if n <= 1:
        return []
    D = Divisors(n)
    D[-1]=0
    return NumsFromBits(D)