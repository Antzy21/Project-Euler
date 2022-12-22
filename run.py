from Problems.Problem22 import solve22, calculateNameScore

file = open('Data\p022_names.txt', 'r')
input = file.read()
result = solve22(input)
print(result)