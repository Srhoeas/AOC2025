def parse():
    s = open('input.txt','r')
    lineas = s.readlines()
    s.close()
    res = []
    acc = ''
    div = []
    for line in lineas:
        if line != '\n':
            for char in line:
                if char == "\n":
                    div.append(acc)
                    acc = ''
                else:
                    acc = acc + char
        else:
            res.append(div)
            div = []
    div.append(acc)
    res.append(div)
    return res

def sol(rangosId,Ids):
    res  = 0
    cotas = refine(rangosId)
    print(cotas)
    for id in Ids:
        for cota in cotas:
            if estaEnCota(int(id),cota):
                res += 1
                break
    return res


def estaEnCota(id,cota):
    res = False
    if (id >= cota[0]) & (id <= cota[1]):
        res = True
    return res

def tailOverlap(seq,suq):
    #this function only checks if the tail of seq has overlap with suq
    res = False
    if (seq[0] >= suq[0]) & (seq[0] <= suq[1]): #this could be done in a mathematical form but i dont know how
        res = True
    return res

def headOverlap(se1,se2):
    #this function only checks if the head of seq has overlap with suq
    res = False
    if (se1[1] >= se2[0]) & (se1[0] <= se2[1]): #this could be done in a mathematical form but i dont know how
        res = True
    return res

def refine(rangosId):
    res = []
    intRangosId = rStrTorInt(rangosId)
    for i in range(len(intRangosId) - 1):
        redo = []
        if tailOverlap(intRangosId[i],intRangosId[i+1]):
            redo.append(intRangosId[i+1][0])
            if intRangosId[i][1] <= intRangosId[i+1][1]:
                redo.append(intRangosId[i+1][1])
            else:
                redo.append(intRangosId[i][1])
            res.append(redo)
            redo = []
            i += 1
        elif headOverlap(intRangosId[i],intRangosId[i+1]):
            if intRangosId[i][0] >= intRangosId[i+1][0]:
                redo.append(intRangosId[i][0])
            else:
                redo.append(intRangosId[i+1][0])
            res.append(redo)
            redo = []
            i += 1
        else:
            res.append(intRangosId[i])
    print(res)
    return res

def rStrTorInt(rangosID):
    intRangosId = []
    for seq in rangosID:
        redo = []
        acc  = ''
        for char in seq:
            if char != '-':
                acc += char
            else:
                redo.append(int(acc))
                acc  = ''
        redo.append(int(acc))
        intRangosId.append(redo)
    return intRangosId

rangosID,Ids = parse()
print(sol(rangosID,Ids))