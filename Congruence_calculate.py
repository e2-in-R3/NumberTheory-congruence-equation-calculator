#!/usr/bin/env python3
from NumberTheory_function import *

print("請按形式 Ax^2 + Bx + C ≡ D (mod. M) 分別輸入 A, B, C, D & M")
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = int(input("D = "))
m = int(input("M = "))
c = c-d
M = m
m = m*4*a if m % 2 ==0 else m
c = mod(b**2 - 4*a*c, m)
a = mod(2*a, m)
b = mod(b, m)
print("\n=> ({:-}x {:+})^2 ≡ {:-} (mod. {})\n".format(a, b, c, m))

P = power(prime(m))
n = 0
for i in P:
    print("=> ({:-}x {:+})^2 ≡ {:-} (mod. {}^{})".format(a, b, c, i, P[i]))
    
    if len(shell(c, i, P[i])) == 0:
        print("無解")
        sol = ""
        break
    else:
        if n == 0:
            sol = shell(c, i, P[i])
            if i == 2:
                for j in range(0,len(sol)):
                    sol[j] = int(mod(sol[j] - b, i**P[i]) / a)
            else:
                for j in range(0,len(sol)):
                    sol[j] = mod((sol[j] - b) * inv(a,i**P[i]), i**P[i])
        else:
            sol = [[x,y] for x in sol for y in shell(c, i, P[i])]
            for j in range(0,len(sol)):
                sol[j][n] = mod((sol[j][n] - b) * inv(a,i**P[i]), i**P[i])
    n += 1
print("\n",sol)

ANS = set()

try:
    for k in sol:
        k[0] = k[0]
        ANS.add(int(mod(Chi(k,P),M))) # (,tuple(k))
except:
    ANS = {mod(k,M) for k in sol if mod((a*k+b)**2,M) == mod(c,M)}
print(ANS)
