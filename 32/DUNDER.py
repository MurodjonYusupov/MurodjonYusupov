# # -*- coding: utf-8 -*-
# """
# Created on Tue Aug 29 16:37:42 2023

# @author: MurodjonUser
# """
# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
    
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto: {self.rang} {self.make} {self.model}"
    
#     def __eq__(self,boshqa_avto):
#         """Tenglik"""
#         return self.narh == boshqa_avto.narh
    
#     def __lt__(self,boshqa_avto):
#         """Kichik"""
#         return self.narh<boshqa_avto.narh
    
#     def __le__(self,boshqa_avto):
#         """Kichik yoki teng"""
#         return self.narh<=boshqa_avto.narh


# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def add_avto(self,avto):
#         if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto classiga tegishli obyekt kiriting!")
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self, index):
#         return self.avtolar[index]
    
#     def __setitem__(self,index, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar[index] = avto
            
# salon1 = AvtoSalon("MaxAvto")
# # Avto obyektlarini yaratamiz
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

# # Yuqoridagi obyektlarni salon1 ga qo'shamiz
# for avto in [avto1, avto2, avto3]: 
#     salon1.add_avto(avto)



class Shaxs:
    """shaxs klassi"""
    __shaxslar = 0
    def __init__(self, ism, familiya, tyil, tjoy, pseria='', praqam=None):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__pseria = pseria
        self.__praqam = praqam
        self.tjoy = tjoy
        Shaxs.__shaxslar += 1
    
    def __repr__(self):
        return f"{self.ism.title()} {self.familiya.title()}"
    def get_info(self):
        shaxs = f"{self.ism.title()} {self.familiya.title()} "
        shaxs += f"{self.tyil}-yil {self.tjoy.title()}da tug'ilgan!"
        return shaxs

    def get_pasport(self):
        return f"Pasport seria va raqami: {self.__pseria.upper()}{self.__praqam}"
    
    def set_pasport(self, ps, pr):
        self.__pseria = ps
        self.__praqam = pr
    
    def set_friends(self, friend):
        self.friends = []
        self.friends.append(friend)
    
    def get_friends(self):
        return self.friends
    
    def __add__(self,friend):
        self.set_friends(friend)
        
    def __lt__(self,y):
        return self.tyil>y.tyil
    
    
    @classmethod
    def get_shaxslar_soni(cls):
        return cls.__shaxslar

class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar = 0
    def __init__(self, ism, familiya, tyil, tjoy, tid, tuniversitet, tkirishball):
        super().__init__(ism, familiya, tyil, tjoy)
        self.__tid = tid
        self.tuniversitet = tuniversitet
        self.tkirishball = tkirishball
        self.tbosqich = 1
        Talaba.__talabalar += 1
        
    def get_info(self):
        talaba = f"{self.ism.title()} {self.familiya.title()}, "
        talaba += f"{self.tuniversitet.title()}da {self.tbosqich}-kursda o'qiydi!"
        return talaba
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar


shaxs1 = Shaxs("murodjon", "yusupov", 1997, "andijon")
shaxs2 = Shaxs("saydullo", "usurov", 1999, "namangan")



talaba1 = Talaba("azizbek", "samonov", 1999, "andijon", 3218566, "andijon davlat universiteti", 110)
talaba2 = Talaba("murodjon", "soipov", 2000, "farg'ona", 3218577, "farg'ona davlat universiteti", 117)
