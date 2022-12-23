# [0,1,0,1,0] -> [1,3]
def NumsFromBits(bitList):
    numList = [0]*sum(bitList)
    pos = 0
    for i in range(len(bitList)):
        if bitList[i] == 1:
            numList[pos] = i+1
            pos += 1
    return numList

def multiplyBitArrays(ary1, ary2):
    newAry = [0]*(len(ary1)*len(ary2))
    for i, b1 in enumerate(ary1, 1):
        for j, b2 in enumerate(ary2, 1):
            newAry[i*j-1] = b1*b2 | newAry[i*j-1]
    return newAry