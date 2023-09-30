def solve():
    max = 100
    powerList = []
    for a in range(2, max+1):
        for b in range(2, max+1):
            value = a**b
            if value not in powerList:
                powerList.append(value)
    return len(powerList)