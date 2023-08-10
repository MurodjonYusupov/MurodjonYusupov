# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:28:33 2023

@author: MurodjonUser
"""
"""Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""
# buyurtmalar = []

# print("Buyurtmalarni qabul qilamiz!")
# savol = "\nAgar buyurtmangiz yo'q bo'lsa 'ENTER' ni bosing"
# n = 1

# while True:
#     buyurtma = input(f"{savol}\n{n}-buyutmani kiriting:\n>>>")
#     if buyurtma == '':
#         break
#     buyurtmalar.append(buyurtma)
#     n += 1
# print(f"Siz quyidagilarni buyurtma berdingiz: {buyurtmalar}")


"""e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
"""

# maxsulotlar = {}

# while True:
#     print("Dasturni tugatish uchun 'ENTER'")
#     maxsulot = input(f"Maxsulot nomini kiriting:\t")
#     if maxsulot == '':
#         break
#     narx = input(f"{maxsulot.capitalize()}ning narxini kiriting:\n>>>")
#     maxsulotlar[maxsulot] = narx
# print(maxsulotlar)

"""Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
"""

# maxsulotlar = {}
# print("e-bozor uchun maxsulotlarni shakllantirib olamiz:")
# print("Dasturni tugatish uchun shunchaki 'ENTER' kifoya qiladi")
# while True:
#     maxsulot = input(f"Maxsulot nomini kiriting:\t")
#     if maxsulot == '':
#         break
#     narx = input(f"{maxsulot.capitalize()}ning narxini kiriting:\n>>>")
#     maxsulotlar[maxsulot] = narx
# print(f"'e-bozor'da mavjud maxsulotlarimiz quyidagilar:\n\n{maxsulotlar}")


# buyurtmalar = []

# print("E-bozordan buyurtmalarni qabul qilamiz!")
# savol = "\nAgar buyurtmangiz yo'q bo'lsa 'ENTER' ni bosing"
# n = 1

# while True:
#     buyurtma = input(f"{savol}\n{n}-buyutmani kiriting:\n>>>")
#     if buyurtma == '':
#         break
#     buyurtmalar.append(buyurtma)
#     n += 1
# print(f"Siz quyidagilarni buyurtma berdingiz: {buyurtmalar}\n")

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in maxsulotlar.keys():
#         narx = maxsulotlar[buyurtma]
#         print(f"{buyurtma.capitalize()} - {narx}")
#     else:
#         print(f"Do'konda {buyurtma.title()} yo'q")

# for maxsulot in buyurtmalar:
#     if maxsulot in maxsulotlar:
#         print(f"{maxsulot.capitalize()} do'konimizda bor! Narxi: {maxsulotlar[maxsulot]}")
#     else:
#         print(f"{maxsulot} do'konda yo'q")
    