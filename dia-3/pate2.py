import os
def parse():
    s = open(os.path.join('input.txt'),'r')
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
    inpt = parse()
    res = 0
    for bat in inpt:
        res += int(maxComb(bat,11))
    return res

def maxComb(bat,digitos):
    if digitos == 0:
        return bat[imax(0,len(bat),bat)]
    else:
        fichr = imax(0,len(bat)-digitos,bat)
        return bat[fichr] + maxComb(cut(bat,fichr + 1,len(bat)),digitos - 1)

def imax(inx,endix,bat):
    res = 0
    for i in range(inx,endix):
        if bat[i] == '9':
            res = i
            break
        elif int(bat[i]) > int(bat[res]):
            res = i
    return res

def cut(s,i,end):
    res = ""
    while i < end:
        res = res + s[i]
        i += 1
    return res

print(sol())

#re cabeza pero bueno