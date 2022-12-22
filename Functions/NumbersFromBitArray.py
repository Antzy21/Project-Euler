def NumsFromBits(bitList):
    numList = [0]*sum(bitList)
    pos = 0
    for i in range(len(bitList)):
        if bitList[i] == 1:
            numList[pos] = i+1
            pos += 1
    return numList