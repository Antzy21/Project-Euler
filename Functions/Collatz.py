def Collatz(n):
    if n%2==0:
        return(n//2)
    return 3*n+1

def CollatzChain(n):
    X = [n]
    while X[-1] != 1:
        X.append(Collatz(X[-1]))
    return(X)