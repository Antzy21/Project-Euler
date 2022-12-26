from Data.numberNames import units, tens, teens

def GetWrittenName(n):
    if n == 0:
        return 'zero'
    strn = str(n)
    name = ''
    name += powerten(strn, 4, 'thousand')
    name += powerten(strn, 3, 'hundred', True)
    name += GetTensAndUnits(int(strn[-2:]))
    return name

def GetUnitName(n):
    if n>9 or 0>n:
        raise Exception("Single digit only")
    return units[n]

def GetTensAndUnits(n):
    if n>99 or n<0:
        raise Exception("Invalid Number")
    if n<10:
        return GetUnitName(n)
    if n<20:
        return teens[n-10]
    nunits = int(str(n)[1])
    ntens = int(str(n)[0])
    return tens[ntens]+GetUnitName(nunits)

def powerten(strn, p, word, addand = False):
    name = ''
    if strn[-p:] == '0'*p:
        return ''
    if len(strn) >= p:
        name += GetUnitName(int(strn[-p]))
        name += word
        if strn[1-p:] == '0'*(p-1):
            return name
        if addand:
            name += 'and'
    return name
    
def solve():
    S = ''
    for n in range(1,1001):
        s = GetWrittenName(n)
        S += s
    return len(S)