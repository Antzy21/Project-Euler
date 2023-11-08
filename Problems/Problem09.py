def solve():
    for a in range(1,500):
        for b in range(1,500):
            c = (a**2+b**2)**(.5)
            if a+b+c == 1000:
                x = a*b*c
                return round(x)