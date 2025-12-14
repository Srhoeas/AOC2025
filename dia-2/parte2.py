import os
def parse():
    s = open(os.path.join('input1.txt'),'r')
    lineas = s.read()
    s.close()
    res = []
    acc = ""
    redo = []
    for char in lineas:
        if char == ",":
            redo.append(acc)
            acc = ''
            res.append(redo)
            redo = []
        elif char == '-':
            redo.append(acc)
            acc = ''
        else:
            acc = acc + char
        
    redo.append(acc)
    res.append(redo)
    return res

def invalidsIdsween(firstID,lastID):
    res = 0
    actID = nextID(firstID)
    while menorA(actID,lastID):
        acc = '' + actID[0]
        for i in range(1,len(actID)):
            if (acc[0] == actID[i]) & (len(actID) % len(acc) == 0) & repeated(acc,actID):
                print(f'------{actID}')
                res += int(actID)
                break
            elif len(acc) > (len(actID) // 2):
                break
            else:
                acc = acc + actID[i]
        actID = nextID(actID)
    return res

def cut(s,i,end):
    res = ""
    while i < end:
        res = res + s[i]
        i += 1
    return res

def menorA(acID,LastID):
    return int(acID) < int(LastID)

def repeated(slice, scom):
    return scom == slice*(len(scom)//len(slice))

def nextID(pId):
    return f'{int(pId)+1}'

def sol():
    res = 0
    inpt = parse()
    print(inpt)
    for pairID in inpt:
        if not valid(pairID[0]):
            res += int(pairID[0])
        if not valid(pairID[1]):
            res += int(pairID[1])
        res += invalidsIdsween(pairID[0],pairID[1])
    return res
print(sol())

#re cabeza aksdjfkajsdlkjfaslkdfjlaksjfd