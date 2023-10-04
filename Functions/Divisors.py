from math import ceil, sqrt
from Functions.BitArray import NumsFromBits

def getDivisorsBitList(n):
    sqrtN = ceil(sqrt(n))
    divisorsList = [0]*(n+1)
    for x in range(1,sqrtN+1):
        if n % x == 0:
            divisorsList[x] = 1
            divisorsList[n//x] = 1
    return divisorsList

def getDivisors(n):
    divisorsBitList = getDivisorsBitList(n)
    return NumsFromBits(divisorsBitList)

def getProperDivisors(n):
    if n <= 1:
        return []
    divisorsBitList = getDivisorsBitList(n)
    divisorsBitList[-1] = 0
    return NumsFromBits(divisorsBitList)