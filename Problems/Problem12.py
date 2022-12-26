from Functions.Divisors import getDivisorsBitList
from Functions.BitArray import *

def getNthTriangleNumber(n):
    return (n+1)*n//2

def getSplitDivisorListForNthTriangleNumber(n):
    if n%2 == 0:
        divisorList1 = getDivisorsBitList(n//2)
        divisorList2 = getDivisorsBitList(n+1)
    else:
        divisorList1 = getDivisorsBitList(n)
        divisorList2 = getDivisorsBitList((n+1)//2)
    return divisorList1, divisorList2

def solve(n=500):
    L = 0
    x = 0
    while L < n:
        x += 1
        d1, d2 = getSplitDivisorListForNthTriangleNumber(x)
        L = sum(d1)*sum(d2)
    return getNthTriangleNumber(x)