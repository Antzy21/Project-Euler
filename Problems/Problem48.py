def solve():
    sum = 0
    n = 1000
    for i in range(1,n+1):
        interProd = 1
        for p in range(0,i):
            interProd = interProd * i
        sum = (sum + interProd) % 10**10
    return(sum)