from Functions.Divisors import sumOfProperDivisors
from Functions.DigitsArithmatic import AddDigits

def solve(n = 10000):
    amicableNumbers = []

    for i in range(1,n+1):
        j = sumOfProperDivisors(i)
        if sumOfProperDivisors(j) == i:
            if i != j:
                amicableNumbers.append(i)
                amicableNumbers.append(j)

    return(sum(amicableNumbers)//2)
