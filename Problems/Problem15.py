# My first self written recusion <3

def Lpath(x,y):
    if x == 0:
        return(1)
    if y == 0:
        return(1)
    return(Lpath(x-1,y)+Lpath(x,y-1))

def solve():
    return Lpath(20,20)

# Shame it takes 16 hours... 40 choose 20 (combinatorics or something)