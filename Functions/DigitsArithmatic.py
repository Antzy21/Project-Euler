def AddDigits(S):
    x = 0
    for s in str(S):
        x += int(s)
    return x

def MultiplyDigits(S):
    x = 1
    for s in str(S):
        x *= int(s)
    return x

def GetDigits(S):
    arr = []
    for s in str(S):
        arr.append(int(s))
    return arr