a, b = map(int, input().split()) 
# for i in range(1, a*b + 1):
#     if(i%a == 0 and i%b == 0):
#         print(i)
#         break
acop, bcop = a, b
aD = []
bD = []
if a == 1: aD.append(1)
else:
    for i in range(2, a + 1):
        while a % i == 0:
            aD.append(i)
            a = a / i

if b == 1: bD.append(1)
else:
    for i in range(2, b + 1):
        while b % i == 0:
            bD.append(i)
            b = b / i

res = 1
if acop == bcop: print(acop)
if acop > bcop:
    for i in bD:
        if (i not in aD) or bD.count(i) > aD.count(i):
            aD.append(i)
    for i in aD:
        res = res * i
    print(res)
if acop < bcop:
    for i in aD:
        if (i not in bD) or bD.count(i) < aD.count(i):
            bD.append(i)
    for i in bD:
        res = res * i
    print(res)
