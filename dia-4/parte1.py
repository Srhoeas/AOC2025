def parse():
    s = open('input.txt','r')
    lineas = s.read()
    s.close()
    res = []
    acc = ""
    for char in lineas:
        if char == "\n":
            res.append(acc)
            acc = ""
        else:
            acc = acc + char
    res.append(acc)
    return res

def sol():
    res = 0
    inpt = parse()
    lap = len(inpt[0])
    unrolled = unroll(inpt)
    for i in range(len(unrolled)):
        if unrolled[i] == '@':
            if accesable(inpt,i,lap):
                res += 1
    return res

def unroll(s):
    res = ''
    for i in s:
        res = res + i
    return res

def accesable(inpt,ind,lap):
    dots = 0
    rulos = 0
    fil = ind // lap
    col = ind % lap
    for j in range(-1,2):
        if (rulos < 4) & (dots < 5):
            f = fil+j
            if (f > -1) & (f < len(inpt)):
                for i in range(-1,2):
                    q = col + i
                    if (q > -1) & (q <len(inpt[f])):
                        if not((f == fil) & (q == col)):
                            if inpt[f][q] == '@':
                                rulos += 1
                            else:
                                dots += 1
    return rulos < 4

print(sol())

    

    