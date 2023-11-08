def solve():
    x=[0,1]
    z=[0]
    y=0
    while x[-1]<4000000:
        x.append(x[-1]+x[-2])
        if x[-1] % 2 == 0:
            y=y+x[-1]
            z.append(x[-1])
    return y