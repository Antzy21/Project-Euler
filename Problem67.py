import copy
from Data.Problem67Triangle import triangle as T

T.reverse()
originalT = copy.deepcopy(T)

for i, x in enumerate(T):
    if len(T[i]) == 1:
        print(T[i], originalT[i])
        continue
    for j, x2 in enumerate(T[i+1]):
        T[i+1][j] += max(T[i][j], T[i][j+1])
    print(T[i], originalT[i])