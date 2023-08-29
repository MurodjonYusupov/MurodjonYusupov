# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:03:51 2023

INKAPSULYATSIYA

@author: MurodjonUser
"""

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
    
    def get_info(self):
        shaxs = f"{self.ism.title()} {self.familiya.title()} "
        shaxs += f"{self.tyil}-yil {self.tjoy.title()}da tug'ilgan!"
        return shaxs

    def get_pasport(self):
        return f"Pasport seria va raqami: {self.__pseria.upper()}{self.__praqam}"
    
    def set_pasport(self, ps, pr):
        self.__pseria = ps
        self.__praqam = pr
    
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
