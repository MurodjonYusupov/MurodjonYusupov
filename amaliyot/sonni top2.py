# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:35:17 2023

@author: MurodjonUser
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:10:20 2023

@author: MurodjonUser
"""
import random as r
import os
import time
def sonni_top_user(x=10):
    """
    Foydalanuvchi sonni topadi, funksiyasi
    """
    
    pc_think_number = r.randint(1, x)
    ishora = True
    taxminlar_soni = 0
    while ishora:
        taxminlar_soni += 1
        user_taxmin = qiymat_mosligiga_tekshir(user_taxmin = 1, x = x)
        if user_taxmin == pc_think_number:
            print(f"Siz topdingiz. {taxminlar_soni}ta urinishda men o'ylagan sonni topdingiz")
            ishora = False
        elif user_taxmin > pc_think_number:
            print(f"\nMen o'ylagan son {user_taxmin}dan kichik, yana urinib ko'ring")
            ishora = True
        else:
            print(f"\nMen o'ylagan son {user_taxmin}dan katta, yana urinib ko'ring")
            ishora = True
    return taxminlar_soni
    
def sonni_top_pc(x=10):
    """
    PC sonni topadi, funksiyasi
    """
    xmin = 1
    xmax = x
    taxminlar_soni = 0
    ishora = True
    while ishora:
        taxminlar_soni += 1
        if xmin > xmax or xmin < 1 or xmax > x:
            taxminlar_soni = 0
            break
        # try:
        pc_taxmin = r.randint(xmin, xmax)
        # except TypeError:
            # print("Siz meni aldadingiz! Aldashlik musulmon kishiga hos emas, Brodar!")
            # return 0
            # break
        top = qiymat_mosligiga_tekshir(pc_taxmin = pc_taxmin, x = x)
        if top == 't':
            print(f"Men topdim. {taxminlar_soni}ta urinishda siz o'ylagan sonni topdim\n")
            ishora = False
        elif top == '+':
            xmin = pc_taxmin + 1
        else:
            xmax = pc_taxmin - 1
    return taxminlar_soni

def qiymat_mosligiga_tekshir(pc_taxmin = 0, user_taxmin = 0, x = 10):
    if user_taxmin != 0:
        ishora = True        
        while ishora:
            ishora = False
            try:
                user_taxmin = int(input("\nTaxminingizni kiriting\n>>"))
                if (user_taxmin < 1) or (user_taxmin > x):
                    user_taxmin + 'Xatolik: {TypeError} sodir etish uchun'
                return user_taxmin
            except TypeError:
                print(f"\nIltimos faqat ko'rsatilgan oraliqdagi sonlardan foydalaning!\n\n1dan {x}gacha sonlar oralig'ida son o'yladim, toping?")
                ishora = True
            except ValueError:
                print(f"\nIltimos faqat ko'rsatilgan oraliqdagi sonlardan foydalaning!\n\n1dan {x}gacha sonlar oralig'ida son o'yladim, toping?")
                ishora = True
    
    if pc_taxmin != 0:
        ishora = True
        while ishora:
            ishora = False
            try:
                top = input(f"Siz o'ylagan son: {pc_taxmin}\nAgar to'g'ri bo'lsa 'T' | katta bo'lsa '+' | kichik bo'lsa '-'  ??\n>>".lower())
                if top == 't' or top == '+' or top == '-':
                    return top
                else:
                    top + 1 + "Xatolikni aniqlash uchun yozdim"
            except TypeError:
                print("Iltimos faqat ko'rsatilgan belgilardan foydalaning!\n")
                ishora = True

def davom_et(davom = 1):
    ishora = True
    while ishora:
        ishora = False
        try:
            davom = int(input("Yana o'ynaymizmi?  yes(1) | no(0)\n<<<"))
            if davom == 0:
                print("O'yin tugadi(:")
                return davom
            elif davom == 1:
                return davom
            else:
                f = int('xatolik sodir etish uchun yozdim')
        except ValueError:
            print("\nIltimos 1 yoki 0 raqamlaridan foydalaning\n")
            ishora = True

def play(x=10):
    print("\n\"SONNI TOP\" o'yinini o'ynaymiz!\n")
    davom = 1
    while davom:
        try:
            xmax = int(input("O'yin uchun oraliqni yuqori chegarasini kiriting:\n(masalan: 10)\n<<<"))
            if xmax < 0:
                xmax = int('xatolik!')
            print(f"\"Sonni top\" o'yinini [1;{xmax}] ushbu oraliqda o'ynaymiz!\nKo'rsatilgan oraliqda son o'yladim, toping?")
            taxminlar_soni_user = sonni_top_user(xmax)
            print("\nEndi siz son o'ylang, men uni topaman!")
            input("Biron sonni o'ylagan bo'lsangiz, ENTERni bosing\n>>")
            taxminlar_soni_pc = sonni_top_pc(xmax)
            if taxminlar_soni_pc == 0:
                print("\n\nSIZ '+','-' ISHORALARNI KIRITISHDA XATOLIKKA YO'L QO'YDINGIZ YOKI...\n\nSiz meni aldadingiz! Aldashlik musulmon kishiga hos emas, Brodar!\n\nQaytadan, ", end = '')
            elif taxminlar_soni_pc > taxminlar_soni_user:
                print(f"Siz sonni topish bo'yicha meni yutdingiz, qoyil!")
            elif taxminlar_soni_pc < taxminlar_soni_user:
                print("Men g'olibman. Meni yutish ancha-munchasiga emas!")
            else:
                print("Durrang. Kuchayibsiz!")
            davom = davom_et()
        except ValueError:
            print("\nIltimos musbat va butun sonlardan foydalaning\n")
            pass

play()
time.sleep(5)
os.system("cls")
print(runcell(0, 'C:/Github files/MurodjonYusupov/amaliyot/sonni top2.py')10)
print("O'yin tugadi(:")


