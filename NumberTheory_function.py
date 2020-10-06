#!/usr/bin/env python3

# mod之下最小的正數
def mod(x, m) :
    return x % m

# 判斷 質數 與 非質數之質因數分解
import math

def prime(n) :
    N = n
    k = ""
    for j in range(len(str(N))*4) :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                k = '{}{}*'.format(k,i)
                n /= i
                break
    if n != N :
        return "{}{}".format(k,int(n))
    else :
        return "{}".format(N)

# 質因數分解 因次式
def power(s) :
    s = s.split("*")
    for i in range(0,len(s)) :
        s[i] = int(s[i])
    D = dict()
    for j in s :
        D[j] = s.count(j)
    return D

# 從mod. p 做到mod. p power
def shell(c, p, n) :
    if n == 1 :
        sol = list()
        for i in range(0,p) :
            if mod(i**2,p) == mod(c,p) :
                sol.append(i)
        return sol
    else :
        Sol = list()
        for obj in shell(c, p, n-1) :
            sol = list()
            for j in range(0,p) :
                if mod((obj + j*p**(n-1))**2,p**n) == mod(c,p**n) :
                    sol.append(obj + j*p**(n-1))
            Sol += sol
        return Sol

# 找反元素
def inv(c, m) :
    e = ""
    for i in range(0,m) :
        e = i if mod(i*c,m) == 1 else e
    return e

# 中國剩餘定理找共同解
def Chi(lst, P) :
    M = 1
    for i in P :
        M *= i**P[i]
    Ans = 0
    n = 0
    for i in P :
        ans = lst[n] * (M/i**P[i]) * inv(M/i**P[i],i**P[i])
        n += 1
        Ans += ans
    return Ans

import fractions
# Φ函數
def phy(m) :
    s = list()
    for i in range(1, m) :
        if fractions.gcd(m, i) == 1 :
            s.append(i)
        else :
            pass
    return(len(s))

# Order
def Ord(m, a) :
    if fractions.gcd(m, a) != 1 :
        return "沒有Order"
    else :
        for i in range(1, phy(m)+1) :
            if mod(a**i, m) == 1 :
                n = i
                break
            else :
                pass
        return n

# Primitive Roots
def pr(m) :
    s = list()
    for i in range(2,m) :
        if fractions.gcd(i, m) == 1 :
            s.append(i)
    t = list()
    for j in s :
        if Ord(m, j) == phy(m) :
            t.append(j)
    t = "沒有p.r." if len(t) == 0 else t
    return t

