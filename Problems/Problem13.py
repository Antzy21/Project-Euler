from Data.Problem13Numbers import numbers as n

def solve():
    S = 0
    for x in n:
        S += x
    return(str(S)[0:10])