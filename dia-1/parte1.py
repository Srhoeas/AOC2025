import os
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

def abs(x):
    if (x<0):
        return -x
    else:
        return x

def cut(s,i,end):
    res = ""
    while i < end:
        res = res + s[i]
        i += 1
    return res

def solucion ():
    inpt = parse()
    init = 50
    acc = 0
    for instruc in inpt:
        dig = int(cut(instruc,1,len(instruc))) % 100
        if init == 0:
            acc += 1
        if instruc[0] == 'L':
            if init - dig < 0:
                init = 100 + init - dig
            else:
                init -= dig
        else:
            if dig + init > 99:
                init = init -100 + dig
            else:
                init += dig
        print(init)
    return acc

print(solucion())