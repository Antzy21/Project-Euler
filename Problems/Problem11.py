from Data.Problem11Array import getArray

A = getArray()

lengthA = len(A[0])
heightA = len(A)

L = 0
s = 4

for x in range(0, lengthA-s):
    for y in range(0, heightA-s):
        cursum = 1
        for i in range(0, s):
            cursum *= A[x+i][y+i]
        if cursum > L:
            L = cursum


for x in range(0, lengthA-s):
    for y in range(0, heightA):
        cursum = 1
        for i in range(0, s):
            cursum *= A[x+i][y]
        if cursum > L:
            L = cursum


for x in range(0, lengthA):
    for y in range(0, heightA-s):
        cursum = 1
        for i in range(0, s):
            cursum *= A[x][y+i]
        if cursum > L:
            L = cursum


for x in range(s, lengthA):
    for y in range(0, heightA-s):
        cursum = 1
        for i in range(0, s):
            cursum *= A[x-i][y+i]
        if cursum > L:
            L = cursum

print(L)
