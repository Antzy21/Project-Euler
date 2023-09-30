from Functions.DigitsArithmatic import GetDigits

digitsToPower5 = [
    0,
    1,
    32,
    243,
    1024,
    3125,
    7776,
    16807,
    32768,
    59049
]

def solve():
    sum = 0
    for i in range(1,200000):
        digitToPower5Sum = 0
        for digit in GetDigits(i):
            digitToPower5 = digitsToPower5[digit]
            digitToPower5Sum += digitToPower5
        if i == digitToPower5Sum:
            totalSum += i
    return sum