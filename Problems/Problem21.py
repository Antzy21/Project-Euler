from Functions.Divisors import getProperDivisors
from Functions.DigitsArithmatic import AddDigits

def solve(n = 10000):
    amicableNumbers = []

    for i in range(1,n+1):
        j = sum(getProperDivisors(i))
        if i > j and sum(getProperDivisors(j)) == i:
            amicableNumbers.append(i)
            amicableNumbers.append(j)

    return(sum(amicableNumbers))
