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

def sol(rangosId):
    res = 0
    intRangosId = rStrTorInt(rangosID)
    insertionSort(intRangosId)
    print(f'{intRangosId}-------')
    cotas = refine(intRangosId)
    print(cotas)
    for cota in cotas:
        res += abs(cota) + 1
    return res

def abs(seq):
    return  (seq[1] - seq[0])

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

def refine(intRangosId):
    res = [intRangosId[0]]
    for i in range(1,len(intRangosId)):
        redo = []
        if tailOverlap(intRangosId[i],res[len(res)-1]):
            redo.append(res[len(res)-1][0])
            if intRangosId[i][1] <= res[len(res)-1][1]:
                redo.append(res[len(res)-1][1])
            else:
                redo.append(intRangosId[i][1])
            res[len(res)-1] = redo
            redo = []
            i += 1
        else:
            res.append(intRangosId[i])
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

def insertionSort(arr):
    i = 1
    hook = 0
    while i < len(arr):
        if i == 0 :
            i = hook + 1
            hook = 0
        elif arr[i-1][0] > arr[i][0]:
            swap(arr,i,i - 1)
            if hook == 0:
                hook = i
            i -= 1
        else:
            i += 1
    return arr

def swap(arr,i,back):
    rest = []
    rest.append(arr[back][0])
    rest.append(arr[back][1])
    arr[back][0] = arr[i][0]
    arr[back][1] = arr[i][1]
    arr[i][0] = rest[0]
    arr[i][1] = rest[1]

rangosID,Ids = parse()

print(sol(rangosID))