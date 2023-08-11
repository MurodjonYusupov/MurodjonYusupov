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

def sonni_top_user(x=10):
    """
    O'ylagan sonni topish o'yini
    """
    
    pc_think_number = r.randint(1, x)
    ishora = True
    taxminlar_soni = 0
    while ishora:
        taxminlar_soni += 1
        user_taxmin = int(input("\n>>"))
        if user_taxmin == pc_think_number:
            # taxmin = user_taxmin
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
    print("\nEndi siz son o'ylang, men uni topaman!")
    input("Biron sonni o'ylagan bo'lsangiz, ENTERni bosing\n>>")
    xmin = 1
    xmax = x
    taxminlar_soni = 0
    while True:
        taxminlar_soni += 1
        pc_taxmin = r.randint(xmin, xmax)
        top = input(f"Siz o'ylagan son: {pc_taxmin}\nAgar to'g'ri bo'lsa 'T' | katta bo'lsa '+' | kichik bo'lsa '-'  ??\n>>".lower())
        if top == 't':
            print(f"Men topdim. {taxminlar_soni}ta urinishda siz o'ylagan sonni topdim\n")
            break
        elif top == '+':
            xmin = pc_taxmin + 1
        else:
            xmax = pc_taxmin - 1
    return taxminlar_soni

def play(x=10):
    print("\n\"SONNI TOP\" o'yinini o'ynaymiz!\n")
    
    while True:
        xmax = int(input("O'yin uchun oraliqni yuqori chegarasini kiriting:\n(masalan: 10)\n<<<"))
        print(f"\"Sonni top\" o'yinini 1dan {xmax}gacha sonlar oralig'ida o'ynaymiz!\nKo'rsatilgan oraliqda son o'yladim, toping?")
        taxminlar_soni_user = sonni_top_user(xmax)
        taxminlar_soni_pc = sonni_top_pc(xmax)
        if taxminlar_soni_pc > taxminlar_soni_user:
            print(f"Siz sonni topish bo'yicha meni yutdingiz, qoyil!")
        elif taxminlar_soni_pc < taxminlar_soni_user:
            print("Men g'olibman. Meni yutish ancha-munchasiga emas!")
        else:
            print("Durrang. Kuchayibsiz!")
        davom_et = int(input("Yana o'ynaymizmi? yes(1) | no(0)\n??"))
        if davom_et != 1:
            print("O'yin tugadi(:")
            break

play()