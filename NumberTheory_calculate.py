#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# **********************************************
#    106學年度第2學期 程式設計期末報告          
#  
#    題目：數論
#    學生：林以寧
#    模組：easygui (, fractions)
#
# **********************************************

from easygui import *
from NumberTheory_function import *

choose = -1
q = 1 # 判斷「繼續」或是「回主選單」
while choose != None : # 用 True 會關不掉
    msg = """請選擇想要的運算：
    
    A：一元一次 Congruence equation
    B：二元一次 Congruence equation
    C：一元二次 Congruence equation
    D：Φ函數
    E：Order
    F：Primitive roots"""
    title = "數論"
    
    if q == 1 :
        choose = indexbox(msg, title, ("A", "B", "C", "D", "E", "F"), None)

    q = 1
    eq = list()
    ANS = list()

    # 一元一次 Congruence equation
    if choose == 0 :
        msg = "請按形式 Ax + B ≡ C (mod. M) 分別輸入 A, B, C & M"
        title = "一元一次 Congruence equation"
        EQ = ["A = ", "B = ", "C = ", "M = "]
        eq = multenterbox(msg, title, EQ) # 若按 Cancle 則傳回 None
        if eq == None :
            pass
        else :
            a = int(eq[0]) # 清單→變數
            b = int(eq[1])
            c = int(eq[2])
            m = int(eq[3])
            for i in range(m) : # 0 ~ (m-1) 一個一個代
                if mod(a*i + b - c, m) == 0:
                    ANS.append(i)
                else:
                    pass
            if len(ANS) != 0 : # 判斷有解無解 並 列印
                msg = "{:-}x {:+} ≡ {:-} (mod. {}) 的解為：\n".format(a, b, c, m)
                for j in ANS :
                    msg += "\nx ≡ {} (mod. {})".format(j, m)
            else :
                msg = "{:-}x {:+} ≡ {:-} (mod. {}) 無解".format(a, b, c, m)
            choice = ccbox(msg, title, ("回主選單", "繼續"), None) # (1, 0)
            if choice == 0 :
                q = 0
                choose = 0
            else :
                q = 1
    
    # 二元一次 Congruence equation
    elif choose == 1 :
        msg = "請按形式 Ax + By + C ≡ D (mod. M) 分別輸入 A, B, C, D & M"
        title = "二元一次 Congruence equation"
        EQ = ["A = ", "B = ", "C = ", "D = ", "M = "]
        eq = multenterbox(msg, title, EQ)
        if eq == None :
            pass
        else :
            a = int(eq[0])
            b = int(eq[1])
            c = int(eq[2])
            d = int(eq[3])
            m = int(eq[4])
            for i in range(m) :
                for j in range(m) :
                    if mod(a*i + b*j + c - d, m) == 0:
                        ANS.append((i,j))
                    else:
                        pass
            if len(ANS) != 0 :
                msg = "{:-}x {:+}y {:+} ≡ {:-} (mod. {}) 的解為：\n".format(a, b, c, d, m)
                for k in ANS :
                    msg += "\nx ≡ {} (mod. {})\ny ≡ {} (mod. {})\n".format(k[0], m, k[1], m)
            else :
                msg = "{:-}x {:+}y {:+} ≡ {:-} (mod. {}) 無解".format(a, b, c, d, m)
            choice = ccbox(msg, title, ("回主選單", "繼續"), None)
            if choice == 0 :
                q = 0
                choose = 1
            else :
                q = 1
    
    # 一元二次 Congruence equation
    elif choose == 2 :
        msg = "請按形式 Ax^2 + Bx + C ≡ D (mod. M) 分別輸入 A, B, C, D & M"
        title = "一元二次 Congruence equation"
        EQ = ["A = ", "B = ", "C = ", "D = ", "M = "]
        eq = multenterbox(msg, title, EQ)
        if eq == None :
            pass
        else :
            a = int(eq[0])
            b = int(eq[1])
            c = int(eq[2])
            d = int(eq[3])
            m = int(eq[4])
            for i in range(m) :
                if mod(a*i**2 + b*i + c - d, m) == 0:
                    ANS.append(i)
                else:
                    pass
            if len(ANS) != 0 :
                msg = "{:-}x^2 {:+}x {:+} ≡ {:-} (mod. {}) 的解為：\n".format(a, b, c, d, m)
                for j in ANS :
                    msg += "\nx ≡ {} (mod. {})".format(j, m)
            else :
                msg = "{:-}x^2 {:+}x {:+} ≡ {:-} (mod. {}) 無解".format(a, b, c, d, m)
            choice = ccbox(msg, title, ("回主選單", "繼續"), None)
            if choice == 0 :
                q = 0
                choose = 2
            else :
                q = 1

    # Φ函數
    elif choose == 3:
        msg = "請輸入 Φ(m) 中的 m"
        title = "Φ函數"
        try :
            m = int(enterbox(msg, title, "", True, None, None))
            msg = "Φ({}) = {}".format(m, phy(m))
            choice = ccbox(msg, title, ("回主選單", "繼續"), None)
            if choice == 0 :
                q = 0
                choose = 3
            else :
                q = 1
            eq = None
        except :
            pass
    
    # Order
    elif choose == 4 :
        msg = "請按形式 Ord_m (a) 分別輸入 m & a"
        title = "Order"
        EQ = ["m = ", "a = "]
        eq = multenterbox(msg, title, EQ)
        if eq == None :
            pass
        else :
            m = int(eq[0])
            a = int(eq[1])
            msg = "Ord_{} ({}) = {}".format(m, a, Ord(m, a))
            choice = ccbox(msg, title, ("回主選單", "繼續"), None)
            if choice == 0 :
                q = 0
                choose = 4
            else :
                q = 1
    
    # Primitive Roots
    elif choose == 5 :
        msg = "請輸入你要找 p.r. 的 m"
        title = "Primitive Roots"
        try :
            m = int(enterbox(msg, title, "", True, None, None))
            msg = pr(m)
            if msg == "沒有p.r." :
                msg += "\n\n因為 {} = {}\n不符合 2, 4, p^n, 2*p^n 的形式 (p : odd prime)".format(m, prime(m))
            choice = ccbox(msg, title, ("回主選單", "繼續"), None)
            if choice == 0 :
                q = 0
                choose = 5
            else :
                q = 1
            eq = None
        except :
            pass

            
