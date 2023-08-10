# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:49:53 2023

@author: MurodjonUser
"""

# py_dic = {
#     "int":"butun sonlar tipi",
#     "float":"o'nlik sonlar tipi",
#     "if":"agar, shart operatori",
#     "else":"if - operatori yolg'on qiymat olsa bajariluvchi operator"
#     }

# for kalit, qiymat in sorted(py_dic.items()):
#     print(f"Kalit : {kalit.title()}")
#     print(f"Qiymat: {qiymat.capitalize()}\n")

# davlatlar = {
#     "uzbekistan":"tashkent",
#     "russia":"moscow",
#     "turkey":"anqara",
#     "germany":"berlin"
#     }

# for davlat in sorted(davlatlar):
#     print(davlat.upper())
# print()
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.upper())

# soz = input("Istalgan davlat nomini yozing: >>>")

# if soz in davlatlar.keys():
#     print(f"{soz.title()}ning poytaxti - {davlatlar[soz].title()}")
# else:
#     print("Biz bunaqa davlat borligini bilmas ekanmiz, uzur!")
    
restoran = {
    "osh":32_000,
    "shashlik":8_000,
    "sho'rva":22_000,
    "lag'mon":20_000,
    "chaxoxbili":32_000,
    "qush boshi":35_000,
    "bifshteks":32_000,
    "tandir gril":48_000,
    "somsa":8_000
    }

buyurtmalar = []
for i in range(3):
    buyurtmalar.append(input(f"{i+1}-buyurtmani kiriting: >>>").lower())
    
# if buyurtma in restoran:
for taom in buyurtmalar:
    if taom in restoran:
        print(f"{taom.upper()} : {restoran[taom]}")
    else:
        print(f"{taom.upper()} : bizda yo'q")
        
