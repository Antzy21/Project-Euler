def solve(n = 600851475143):
    divisor = 2
    primeFactors = []
    while n > divisor:
        if n % divisor == 0:
            n = int(n/divisor)
            primeFactors.append(divisor)
        divisor=divisor+1
    return(n)