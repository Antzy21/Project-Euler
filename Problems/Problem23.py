from Functions.Divisors import getProperDivisors
from Functions.Divisors import getDivisors

def solve(maxNum = 28124):

    abundantNumbers = []

    for i in range(1, maxNum, 1):
        if i in abundantNumbers:
            continue
        
        if sum(getProperDivisors(i)) > i:
            for multipleOfAbNum in range(i, maxNum, i):
                abundantNumbers.append(multipleOfAbNum)

    sumsOfAbundantNumbers = {}
    for abundantNum1 in abundantNumbers:
        for abundantNum2 in abundantNumbers:
            curSum = abundantNum1 + abundantNum2
            if curSum < maxNum and curSum not in sumsOfAbundantNumbers:
                sumsOfAbundantNumbers[curSum] = (abundantNum1, abundantNum2)

    nonSumOfAbundantNumbers = []

    returnSum = 0
    for i in range(0, maxNum):
        if i not in sumsOfAbundantNumbers:
            nonSumOfAbundantNumbers.append(i)
            returnSum += i

    return returnSum