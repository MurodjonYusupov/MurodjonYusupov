# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:41:02 2023

@author: MurodjonUser
"""

# son = int(input("Istalgan juft sonni kiriting: >>>"))

# if son % 2:
#     print("Iltimos juft son kiriting")
    
# else:
#     print("Raxmat")

# yosh = int(input("Yoshingiz nechida? >>>"))

# if yosh < 4 or yosh > 60:
#     print("Sizga kirish bepul")
# elif yosh < 18:
#     print("Sizga kirish  10 000 so'm")
# else:
#     print("Sizga kirish 20 000 so'm")

# son1 = int(input("1-sonni kiriting: >>>"))
# son2 = int(input("2-sonni kiriting: >>>"))

# if son1 == son2:
#     print("siz kiritgan sonlar teng!")
# elif son1 > son2:
#     print(f"{son1}>{son2}")
# else:
#     print(f"{son1}<{son2}")

# mahsulotlar = ["sabzi", "makaron", "guruch", "go\'sht", "pishloq", "anjir", "karam", "lavlagi"]

# savat = []
# # mahsulot_soni = int(input("Nechta "))
# print("\nHarid uchun 5ta mahsulot kiritasiz:\n")
# for i in range(5):
#     savat.append(input(f"{i+1}-maxsulotni kiriting >>>"))
# bor_mahsulotlar = []
# yoq_mahsulotlar = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} do'konimizda bor")
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")
#         yoq_mahsulotlar.append(mahsulot)

# if not yoq_mahsulotlar:
#     print("Siz so'ragan barcha masulotlarimiz do'konimizda bor")
# else:
#     print(f"do'konimizda quyidagi mahsulotlar yo'q:\n {yoq_mahsulotlar}")

foydalanuvchilar = ["admin", "lobar", "oydin", "zarifa", "murodjon"]

new_login = input("yangi login kiriting: >>>")

if new_login.lower() in foydalanuvchilar:   
    print("Login band. Yangi login tanlang")
else:
    print(f"Xush kelibsiz {new_login.title()}")