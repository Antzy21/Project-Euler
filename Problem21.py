from Functions.Divisors import getProperDivisors as pds
from Functions.HandleDigits import AddDigits

def d(n):
    return sum(pds(n))

n = 10000
ami = []

for i in range(1,n+1):
    j = d(i)
    if d(j) == i:
        if i != j:
            ami.append(i)
            ami.append(j)
            print(i, j)

print(ami)

print(sum(ami)/2)
