from Functions.Collatz import Collatz as Col, CollatzChain as CC

print(CC(837799))


b = 1000000
X = []
for i in range(0, b):
    X.append([i+1])

while len(X) > 1:
    for x in X:
        if x[-1] == 1:
            X.remove(x)
        x.append(Col(x[-1]))
    print(len(X))

print(X[0])
         
