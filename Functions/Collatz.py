def Collatz(n):
    if n%2==0:
        return(n//2)
    return 3*n+1