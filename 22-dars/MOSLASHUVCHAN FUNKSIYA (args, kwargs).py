# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:40:24 2023

@author: MurodjonUser

"""

def kopaytir(*sonlar):
    """Bir nechta sonlarni ko'paytmasini qaytaruvchi funksiya"""
    kopaytma = 1 
    for son in sonlar:
        kopaytma = kopaytma * son
    return kopaytma

sonlar = [5,7,9]
print(kopaytir(*sonlar))
# print("3ta son kiriting, men ko'paytmasini aytaman!\n")
# for i in range(0, 3):
    # sonlar.append(int(input("")))
