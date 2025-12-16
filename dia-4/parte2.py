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

def replace(s,i,k):
    a = cut(s,0,i)
    b = cut(s,i+1,len(s))
    return a+k+b

def sol(oInpt):
    res = 0
    lap = len(oInpt[0])
    unrolled = unroll(oInpt)
    for i in range(len(unrolled)):
        if unrolled[i] == '@':
            if accesable(oInpt,i,lap):
                res += 1
                oInpt[i//lap] = replace(oInpt[i//lap],i % lap ,'.')
                (oInpt[i//lap])
    if res > 0:
        res += sol(oInpt)
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

def cut(s,i,end):
    res = ""
    while i < end:
        res = res + s[i]
        i += 1
    return res

print(sol(parse()))