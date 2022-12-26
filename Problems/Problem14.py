from Functions.Collatz import Collatz

def solve(b = 1000000):
    
    X = []
    for i in range(0, b):
        X.append([i+1])

    while len(X) > 1:
        for x in X:
            if x[-1] == 1:
                X.remove(x)
            x.append(Collatz(x[-1]))
            
    return(X[0])