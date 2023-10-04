# My first self written recusion <3

def Lpath(x,y):
    if x == 0:
        return(1)
    if y == 0:
        return(1)
    return(Lpath(x-1,y)+Lpath(x,y-1))

def solve_old():
    return Lpath(20,20)

# Shame it takes 16 hours... 40 choose 20 (combinatorics or something)

### 5 years later

# Use a dictionary lol

def solve(x = 20, y = 20):
    
    LpathDict = {}

    def Lpath2(x,y):
        if (x,y) in LpathDict:
            return LpathDict[(x,y)]
        if (y,x) in LpathDict:
            return LpathDict[(y,x)]
        if x == 0 or y == 0:
            LpathDict[(x,y)] = 1
            return 1

        value = Lpath2(x-1,y)+Lpath2(x,y-1)
        LpathDict[(x,y)] = value

        return value

    return Lpath2(x,y)