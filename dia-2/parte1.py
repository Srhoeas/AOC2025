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
    actID = nextNotValidID(firstID)
    print(f'res {res}')
    while menorA(actID,lastID):
        res += int(actID)
        print(f'res {res}')
        actID = nextNotValidID(actID)
        print(actID)
    print(res)
    return res

def cut(s,i,end):
    res = ""
    while i < end:
        res = res + s[i]
        i += 1
    return res

def valid(id):
    res = True
    if int(id) >= 10:
        if len(id) % 2  == 0:
            pri = cut(id,0,len(id)//2)
            sec = cut(id,len(id)//2,len(id))
            if pri == sec:
                res = False
    return res

def menorA(acID,LastID):
    print(f'{acID} < {LastID}')
    return int(acID) < int(LastID)

def nextNotValidID(actID):
    if len(actID) % 2 != 0:
        actID = ('1' + '0'*(((len(actID) + 1)//2)-1))*2
    else:
        actID = nextID(cut(actID,0,len(actID)//2),cut(actID,len(actID)//2,len(actID)))
    return actID

def nextID(priMid,secMid):
    if int(secMid) < int(priMid):
        return priMid*2
    else:
        return f'{int(priMid)+1}'*2

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
        print(f'posta :{res}')
    return res
print(sol())