from Functions.Collatz import Collatz

def solve(b = 1000000):
    
    def GetCollatzLength(i):
        if i in CollatzLengthDict:
            return CollatzLengthDict[i]
        else:
            j = Collatz(i)
            CollatzLengthDict[i] = GetCollatzLength(j) + 1
            return CollatzLengthDict[i]

    # Initialize 1 with Collatz length of 1
    CollatzLengthDict = {1:1}

    longestCollatzLengthValue = 0
    longestCollatzLengthKey = 1

    for i in range(1, b+1):
        GetCollatzLength(i)
        if CollatzLengthDict[i] > longestCollatzLengthValue:
            longestCollatzLengthValue = CollatzLengthDict[i]
            longestCollatzLengthKey = i

    return longestCollatzLengthKey