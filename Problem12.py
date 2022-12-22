from Functions.Divisors import getDivisors, Divisors

S = 52403203
L = 0
x = 52413441-52403203
while L < 500:
    S += x
    x += 1
    #print(S)
    D = Divisors(S)
    L = sum(D)
    if (L > 100):
        print(L, S)


