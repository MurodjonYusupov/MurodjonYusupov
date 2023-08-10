# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:50:43 2023

@author: MurodjonUser
"""

# olimlar = {
#     'abu-rayxon beruniy':{
#         'tavalludi':{
#             'tug_yili':973,
#             'tug_joyi':"Qoraqalpogʻistonning Beruniy tumani"            
#             },
#         'vafoti':{
#             'vaf_yili':1048,
#             'vaf_joyi':"Gʻazna, qisman Movaraunnahr"
#             },
#         'izlanishlari':['islom', 'fiqh', 'ilohiyot', 'grammatika', 'riyoziyot', 'falakiyot', 'tibbiyot va falsafa', 'fizika']
#         },
#     'amir temur':{
#         'tavalludi':{
#             'tug_yili':1336,
#             'tug_joyi':"Kesh (hozirgi Shahrisabz)"
#             },
#         'vafoti':{
#             'vaf_yili':1405,
#             'vaf_joyi':"Oʻtror, (Qozogʻiston)"
#             },
#         'izlanishlari':['davlat arbobi', 'buyuk turkiy sarkardasi', 'kuchli, markazlashgan davlat asoschisi', 'ilm-fan va madaniyat homiysi']
#         }
    
#     }
# for olim, yashagan_info in olimlar.items():
#     # print(olim.title())
#     # print(type(yashagan_info))
#     for tug_vaf_izl, faktlar in yashagan_info.items():
#         # print(f"{tug_vaf_izl}:")
#         # print(type(faktlar))
#         # print(faktlar['tug_yili'])
#         # for i in range(2):
#             # print(f"{faktlar['tug_yili']}", end = ', ')
#     # for olim_tavalludi, tug_info in yashagan_info.items():
#         print(f"{olim.title()} {olim_tavalludi['tug_yili']}-yili {yashagan_info['tavalludi']['tug_joyi']}da tug'ilgan")
# print()

# alisher = {
#     "fish":"alisher navoiy",
#     "tyili":1441,
#     "vyili":1501,
#     "kasbi":'novvoy',
#     "tjoyi":'navoiy',
#     "asar":["yulduz turkum","sayohatnoma"]
#     }

# temur = {
#     "fish":"amir temur",
#     "tyili":1581,
#     "vyili":1601,
#     "kasbi":'temirchi',
#     "tjoyi":'toshkent',
#     "asar":["fatvo","islom nuri"]
#     }

# murodjon = {
#     "fish":"murodjon yusupov",
#     "tyili":1997,
#     "vyili":2023,
#     "kasbi":'dasturchi',
#     "tjoyi":'andijon',
#     "asar":["fiqx","tasavvuf"]
#     }

# shaxslar = [alisher, temur, murodjon]

# for shaxs in shaxslar:
#     ism = shaxs['fish']
#     asarlar = shaxs['asar']
#     print(f"{ism.title()}ning asarlari:")
#     for asar in asarlar:
#         print(f"{asar.title()}", end = ', ')
#     print("\n")
# # for shaxs in shaxslar:
# #     print(f"{shaxs['fish'].title()} {(shaxs['vyili'])-(shaxs['tyili'])} yil yashagan. Kasbi: {shaxs['kasbi']}. {shaxs['tjoyi'].title()}da tug'ilgan.")

# # for shaxs in shaxslar:
# #     print(f"{shaxs['fish'].title()} - {shaxs['asar']}")
    
# dostlar = {
#     "alimbek":[],
#     "valijon":[],
#     "arabboy":[]
#     }

# for dost,filmlar in dostlar.items():
#     print(f"Do'stim {dost.title()} 3ta sevimli serialingizni kiriting")
#     for i in range(3):
#         filmlar.append(input(f"{i+1}-sevimli serial yoki kinoingiz nomini kiriting: >>>"))

# for dost, filmlar in dostlar.items():
#     for kino in filmlar:
#         print(f"{dost.title()}ning {filmlar.index(kino)+1}-sevimli kinosi: {kino.title()}")
#     print()


# davlatlar = {
#     "rossiya":{
#         "short":"ru",
#         "poytaxt":"moskva",
#         "aholi":146_240_000,
#         "big_city":"moskva",
#         "prizident":"vladimir putin",
#         "pul_birligi":"rubl",
#         "til":"rus"
#         },
#     "birlashgan arab amirliklari":{
#         "short":"baa",
#         "poytaxt":"abu-dabi",
#         "aholi":5_000_000,
#         "big_city":"dubay",
#         "prizident":"Muhammad bin Zoid-al Nahayon",
#         "pul_birligi":"dinor",
#         "til":"arab"
#         },
#     "qozog'iston":{
#         "short":"kz",
#         "poytaxt":"astona",
#         "aholi":18_157_078,
#         "big_city":"almata",
#         "prizident":"qosim-jomart toqayev",
#         "pul_birligi":"tenge",
#         "til":"qozoq"
#         }
#     }

# # for davlat, davlat_info in davlatlar.items():
# #     print(f"{davlat.title()}:\n"
# #         f"Poytaxti: {davlat_info['poytaxt'].title()} shaxri\n"
# #         f"Davlat qisqartmasi: {davlat_info['short'].upper()}\n"
# #         f"Aholi soni: {davlat_info['aholi']}ta \n"
# #         f"Eng katta shaxari: {davlat_info['big_city'].title()} shaxri\n"
# #         f"Hozirgi prizidenti: {davlat_info['prizident'].title()} \n"
# #         f"Pul birligi: {davlat_info['pul_birligi']}\n"
# #         f"Davlat tili: {davlat_info['til']}\n"
# #         )

# userdav = input("Qaysi davlat haqida ma'lumot olmoqchisiz? >>>")
# dav_info = davlatlar[userdav]

# if userdav in davlatlar:
#     print(
#         f"Poytaxti: {dav_info['poytaxt'].title()} shaxri\n"
#         f"Davlat qisqartmasi: {dav_info['short'].upper()}\n"
#         f"Aholi soni: {dav_info['aholi']}ta \n"
#         f"Eng katta shaxari: {dav_info['big_city'].title()} shaxri\n"
#         f"Hozirgi prizidenti: {dav_info['prizident'].title()} \n"
#         f"Pul birligi: {dav_info['pul_birligi']}\n"
#         f"Davlat tili: {dav_info['til']}\n"
#         )    
# else:
#     print("Bizda bunday davlat haqida ma'lumot yo'q")
