def LargePrimeFactor(X):
    for n in range(2,X):
        if X % n == 0:
            X = X/n