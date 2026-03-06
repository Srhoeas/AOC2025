def optiPago(b,i,j):
    if j <= 0:
          return [j,0]
    elif i == 0: 
            return [1,-1]
    else:
          frs = optiPago(b,i-1,j-b[i-1])
          snd = optiPago(b,i-1,j)
          frs[1] = frs[1] + 1
          return minCQ(frs,snd)

def minCQ(a,b):
     if a[0] == 1:
          return b
     elif b[0] == 1:
          return a
     elif a[0] > b[0]:
          return a
     elif b[0] > a[0]:
          return b
     else:
          if a[1] == -1:
               return b
          elif b[1] == -1:
               return a
          elif a[1] < b[1]:
               return a
          else:
               return b
          
print(optiPago([2,3,5,10,20,20],6,14))