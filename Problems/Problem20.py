from math import factorial
from Functions.DigitsArithmatic import AddDigits

def solve(n = 100):
    factorialN = factorial(n)
    return AddDigits(factorialN)