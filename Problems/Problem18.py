from Data.Problem18Triangle import triangle as T

def solve(triangle = T):
    triangle.reverse()
    for i, x in enumerate(triangle):
        if len(x) == 1:
            continue
        for j, x2 in enumerate(triangle[i+1]):
            triangle[i+1][j] += max(x[j], x[j+1])
    return(triangle[i][0])