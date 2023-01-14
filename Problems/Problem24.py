# Fibonacci sequenece without recursion to avoid stack limit
def solve(digitLength = 1000):
    f1 = 1
    f2 = 1
    n = 3
    while len(str(f1 + f2)) < digitLength:
        #print(f"f{n} = {f1+f2}")
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        n = n+1
    return n
