# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:40:06 2023

@author: MurodjonUser
"""

# def oraliq(a, b, qadam = 1):
#     """
#     berilgan oraliqlar bo'yicha qiymatlarni ro'yxatga yuklab, ro'yxat qaytaradigan funksiya'
#     """
#     natija = []
#     while a<b:
        
#         natija.append(a)
#         a += qadam
#     return natija

# oraliqqiymatlar = oraliq(4,15,2)

# print(oraliqqiymatlar)        

# """
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili,
#  tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
#  lug'at ko'rinishida qaytaruvchi funksiya yozing. 
#  Lug'atda foydalanuvchu yoshi ham bo'lsin. 
#  Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# """

# def info_user_jamla(ism, familiya, tug_yil, tug_joy, gmail = '', tel = ''):
#     info_user = {
#         'ism' : ism,
#         'familiya' : familiya,
#         'tug_yil' : tug_yil,
#         'tug_joy' : tug_joy,
#         'gmail' : gmail,
#         'tel' : tel
#         }
#     return info_user
#     print(info_user)
    
# info_user_jamla('hamidjon', 'shokirov', 1997, 'farg\'ona')


# """
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, 
# va mijozlar degan ro'yxatni shakllantiring. 
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

# """

# mijozlar = []

# while True:
#     ism = input("Dasturni yakunlash uchun shunchaki 'ENTER'ni bosing\nyoki\nIsmingizni kiriting")
#     if ism == '':
#         break    
#     # ism = input("Ism kiriting:\n>>>")
#     familiya = input("Familiyangizni kiriting:\n>>>")
#     tug_joy = input("tug'ilgan joyingizni kiriting:\n>>>")
#     tug_yil = input("Tug'ilgan yilingizni kiriting:\n>>>")
#     tel = input("Tel raqamingizni kiriting:\n>>>")
    
#     mijozlar.append(info_user_jamla(ism, familiya, tug_yil, tug_joy, tel = tel))


# def engkattasi(a,b,c):
#     kattasi = a
#     if a>b and a>c:
#         kattasi = a
#     elif b>a and b>c:
#         kattasi = b
#     else:
#         kattasi = c
#     print(f"Siz kiritgan eng katta son -> {kattasi}")
#     return kattasi

# a = input("1-sonni kiriting: >>>")
# b = input("2-sonni kiriting: >>>")
# c = input("3-sonni kiriting: >>>")

# engkattasi(a, b, c) 


# """
# Foydalanuvchidan aylaning radiusini qabul qilib olib, 
# uning radiusini, diametrini, perimetri va yuzini 
# lug'at ko'rinishida qaytaruvchi funksiya yozing
# """

# def hisobla(r):
#     aylana = {
#         'yuzi' : 3.14*(r)**2,
#         'diametri' : 2*r,
#         'perimetri' : 2*3.14*r
#         }
#     return aylana

# hisobla(int(input("Aylananing radiusini kiriting: >>>")))


# """
# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi 
# funksiya yozing (tub sonlar —faqat birga va 
#                  o'ziga qoldiqsiz bo'linuvchi, 
#                  1 dan katta musbat sonlar)
# """

# def tubsonlar(a,b):
#     tubsonlar = []
#     tub = False
#     for tek_son in range(a, b+1):
#         if tek_son == 1:
#             tub = False
#         elif tek_son == 2:
#             tub = True
#         else:
#             for i in range(2, tek_son):
#                 if tek_son%i == 0:
#                     tub = False
#                     break
#                 else:
#                     tub = True
#         if tub:
#                 tubsonlar.append(tek_son)
#     return tubsonlar


# oraliq1 = int(input("\nSiz kiritadigan oraliqdagi tub sonlarni ko'rsatib beraman!\nQuyi chegarani kiriting"))
# oraliq2 = int(input("yuqori chegarani kiriting"))
# tubsonlar(oraliq1, oraliq2)
    
# """fibonachi sonlari"""

# def fibonachi(a):
#     fib_sonlar = [1, 2]
#     for i in range(a):
#         fib_sonlar.append(fib_sonlar[i]+fib_sonlar[i+1])
#     return fib_sonlar

# miqdor = int(input(f"Nechta Finochi sonlarini ko'rmoqchisiz? \n>>>")) 
# fibonachi(miqdor-2)       
        
    # print(f"{}")