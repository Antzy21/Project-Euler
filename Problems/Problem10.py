from Functions.SieveOfEratosthenes import SieveOfErathostenes
from Functions.BitArray import NumsFromBits

def solve(n = 2000000):
    primeBitsBelowN = SieveOfErathostenes(n)
    primesBelowN = NumsFromBits(primeBitsBelowN)
    sum = 0
    for x in primesBelowN:
        sum += x
    return(sum)