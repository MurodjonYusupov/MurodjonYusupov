# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:10:20 2023

@author: MurodjonUser
"""
import random as r

def sonni_top(pc):
    """
    O'ylagan sonni topish o'yini
    """
    ishora = True
    i = 1
    while ishora:
        x = int(input(">>"))
        if x == pc:
            print(f"Siz topdingiz. {i}ta urinishda men o'ylagan sonni topdingiz")
            ishora = False
        elif x > pc:
            print(f"Men o'ylagan son {x}dan kichik, yana urinib ko'ring")
            ishora = True
            i += 1
        else:
            print(f"Men o'ylagan son {x}dan katta, yana urinib ko'ring")
            ishora = True
            i += 1
    return i
    
def sonni_topaman():
    print("Endi siz son o'ylang, men uni topaman!")
    goo = input("Biron sonni o'ylagan bo'lsangiz, ENTERni bosing\n>>")
    
    aytilgan_sonlar = []
    xmin = 0
    xmax = 10
    x = 1
    i = 1
    while True:
        x_old = x
        x = r.randint(xmin, xmax)
        while x in aytilgan_sonlar:
            x = r.randint(xmin, xmax)
        top = input(f"Siz o'ylagan son: {x}\nAgar to'g'ri bo'lsa 't' | katta bo'lsa '+' | kichik bo'lsa '-'  ??\n>>")
        aytilgan_sonlar.append(x)
        if top == 't':
            print(f"Men topdim. {i}ta urinishda siz o'ylagan sonni topdim\n")
            break
        elif top == '+':
            xmin = x
            i += 1
        else:
            xmax = x
            i += 1
    return i

def flag():
    print("Keling \"sonni top\" o'yinini o'ynaymiz!\n1dan 10gacha sonlardan son o'yladim, toping?")
    pc_number = r.randint(1, 10)
    
def flag2():
    print("Qoyil, davom etamiz!\n1dan 10gacha sonlardan son o'yladim, toping?")
    pc_number = r.randint(1, 10)

first_run = True
davom_et = True
pc_number = r.randint(1, 10)

while davom_et:
    if first_run:
        flag()
        first_run = False
    else:
        flag2()
    pcgr = sonni_top(pc_number)
    usergr = sonni_topaman()
    if pcgr == usergr:
        print(f"Biz durrang o'ynadik', hisob: {pcgr}<<:>>{usergr}")
    elif pcgr > usergr:
        print(f"Men sonni topish bo'yicha sizni yutdim!")
    else:
        print(f"Siz sonni topish bo'yicha meni yutdingiz!")
    davom_et = int(input("Yana o'ynaymizmi? yes(1) | no(0)\n??"))
    
    if davom_et != 1:
        print("O'yin tugadi(:")
        break