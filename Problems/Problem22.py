from Functions.alphabetValues import alphabetValues 

def calculateNameScore(name, log = False):
    nameValue = 0
    logString = name+ ": "
    for letter in name:
        letterValue = alphabetValues[letter.lower()]
        logString += f"{letter} {letterValue} + "
        nameValue += letterValue
    if log:
        print(logString)
    return nameValue
    

def solve22(input, log = False):
    names = input.split(',')
    sum = 0
    names.sort()
    for i, name in enumerate(names):
        name = name.replace('"', '')
        nameScore = calculateNameScore(name, log)
        if log:
            print(f"{nameScore}*{i+1}={nameScore*(i+1)}")
        sum += nameScore*(i+1)
    return sum