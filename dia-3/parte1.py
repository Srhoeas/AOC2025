import os
def parse():
    s = open(os.path.join('input1.txt'),'r')
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
        res += int(maxComb(bat))
    return res

def maxComb(bat):
    fichr = imax(0,len(bat)-1,bat)
    s = cut(bat,fichr+1,len(bat))
    sichr = imax(0,len(s),s) + fichr +1
    return bat[fichr] + bat[sichr]

def imax(inx,endix,bat):
    res = 0
    for i in range(inx,endix):
        if bat[i] == '9':
            res = i
            break
        elif int(bat[i]) > int(bat[res]):
            res = i
    print(res)
    return res

def cut(s,i,end):
    res = ""
    while i < end:
        res = res + s[i]
        i += 1
    return res

print(sol())

#re cabeza pero bueno