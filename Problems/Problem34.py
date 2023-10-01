from Functions.DigitsArithmatic import GetDigits
from math import factorial

def solve():
    result = 0
    for i in range(0,1000000):
        sum = 0
        for digit in GetDigits(i):
            sum += factorial(digit)
        if sum == i:
            result += sum
    return result