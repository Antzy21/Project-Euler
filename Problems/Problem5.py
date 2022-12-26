from Functions.SieveOfEratosthenes import SieveOfErathostenes
from Functions.BitArray import NumsFromBits

def solve(n = 20, log = False):
    primeBitsBelowN = SieveOfErathostenes(n)
    primesBelowN = NumsFromBits(primeBitsBelowN)
    result = 1
    for prime in primesBelowN:
        primePower = prime
        while primePower < n:
            primePower *= prime
        result *= (primePower//prime)
    if log:
        for n in range(1,n+1):
            print(result,'divided by',n,'is',result/n)
    return result