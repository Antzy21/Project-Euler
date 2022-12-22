from Functions.Divisors import getProperDivisors as pds
from Functions.NumbersFromBitArray import NumsFromBits
from numpy import matrix
import copy

m = 28124

ab = [0]*m

for i in range(m):
    s = sum(pds(i))
    if s > i:
        ab[i-1]=1
    
ab = NumsFromBits(ab)
print(matrix(ab))

AB = [0]*len(ab)

print(matrix(AB))


for i in ab:
    for j in ab:
        AB[i][j] = ab[i] + ab[j]
print(matrix(AB))

I = [1]*m
for i in range(m):
    print(i)
    for a in AB:
        if i in a:
            I[i] = 0
            continue

print(NumsFromBits(I))

