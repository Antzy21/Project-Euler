def solve():
    n=range(999,900,-1)
    Palendromes=[]
    for i in n:
        for j in n:
            T=i*j
            T=str(T)
            if int(T[0])==int(T[-1]):
                if int(T[1])==int(T[-2]):
                    if int(T[2])==int(T[-3]):
                        if T not in Palendromes:
                            Palendromes.append(T)
    return max(Palendromes)