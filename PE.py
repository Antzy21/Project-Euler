import math
import numpy as np

x=[0,1]
z=[0]
y=0
while x[-1]<4000000:
    x.append(x[-1]+x[-2])
    if x[-1] % 2 == 0:
        y=y+x[-1]
        z.append(x[-1])
print(x)
print(z)
print(y)

def LargePrimeFactor(X):
    n=2
    N=[]
    while X > n:
        if X % n == 0:
            X = int(X/n)
            N.append(n)
        n=n+1
    print(N)
    print(X)
LargePrimeFactor(600851475143)
#LargePrimeFactor(13195)

n=range(999,900,-1)
Pal=[]
P=[]
for i in n:
    for j in n:
        X=i*j
        X=str(X)
        if int(X[0])==int(X[-1]):
            if int(X[1])==int(X[-2]):
                if int(X[2])==int(X[-3]):
                    if X not in Pal:
                        Pal.append(X)
                        P.append([X,i,j])
print(P)

X=2*2*2*2*3*3*5*7*11*13*17*19
for n in range(1,21):
    print(X,'divided by',n,'is',X/n)
print(X)

Sum1=0
Sum2=0
for n in range(1,101):
    Sum1=Sum1+n*n
    Sum2=Sum2+n
Sum2=Sum2*Sum2
print(Sum2-Sum1)

X=2
P=[2]
while len(P)<10:
    N=[]
    n=2
    while n < math.sqrt(X)+1:
        if X % n == 0:
            #not prime
            N.append(n)
        n=n+1
    if N == []:
        P.append(X)
    X=X+1
print(P)

X=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
X=str(X)
Pro=[]
for n in range(0,1000-13):
    S=1
    P=[]
    for m in range(0,13):
        S=S*int(X[n+m])
        P.append(int(X[n+m]))
    Pro.append(S)
print(max(Pro))

for a in range(1,500):
    for b in range(1,500):
        c=(a**2+b**2)**(.5)
        if a+b+c == 1000:
            X=a*b*c
            print(X)

            def All_Primes_Below(Y):
                P=[2]
                X=1
                while P[-1]<Y:
                    N=[]
                    n=2
                    while n < math.sqrt(X)+1:
                        if X % n == 0:
                            #not prime
                            N.append(n)
                        n=n+1
                    if N == []:
                        P.append(X)
                    X=X+1
                print(P)

            All_Primes_Below(2000000)

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
p=get_primes(2000000)
print(p)
