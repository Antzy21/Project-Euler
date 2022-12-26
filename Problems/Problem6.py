def solve():
    Sum1=0
    Sum2=0
    for n in range(1,101):
        Sum1=Sum1+n*n
        Sum2=Sum2+n
    Sum2=Sum2*Sum2
    return Sum2-Sum1