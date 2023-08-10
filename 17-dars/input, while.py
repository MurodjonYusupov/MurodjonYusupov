# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:14:09 2023

@author: MurodjonUser
"""

# savol = "Yaxshi ko'rgan kitobingizni kiriting!\n"
# savol += "Dasturni to'xtatish uchun stop \n>>>"
# ishora = True
# kitoblar = []
# while ishora:
#     kitob = input(savol)
#     if kitob.lower() == 'stop':
#         ishora = False
#         print(f"Siz yoqtirgan kitoblar quyidagilar: \n{kitoblar}")
#     kitoblar.append(kitob)



# savol = "Yoshingiz nechchida? \n>>>"
# ishora = True

# while ishora:
#     yosh = input(savol)
    # if yosh == 'stop' or yosh == 'quit':
#         ishora = False
#     else:
#         yosh = int(yosh)
#         if yosh > 0 and yosh < 7:
#             narh = 2000
#         elif yosh >= 7 and yosh < 18:
#             narh = 3000
#         elif yosh >= 18 and yosh < 65:
#             narh = 10000
#         else:
#             print("Noldan katta va musbat son kiriting, iltimos!")
#             continue
#         print(f"{yosh} yoshdagilar uchun bilet narxi {narh}")
        

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.lower() == 'exit':
        break
    if float(qiymat) < 0:
        print("Musbat son kiriting iltimos: \n>>>")
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
 