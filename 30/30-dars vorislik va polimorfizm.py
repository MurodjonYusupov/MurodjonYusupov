# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:36:13 2023

@author: MurodjonUser
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Professor(Shaxs):
    """professor clasini yaratamiz"""
    def __init__(self, ism, familiya, passport, tyil, ish_joyi):
        """professorning xususiyatlarini yaratamiz"""
        super().__init__(ism, familiya, passport, tyil)
        self.ish_joyi = ish_joyi
        self.unvoni = 'professor'
    def get_unvoni(self):
        return self.unvoni
    
    # def 

class Sotuvchi(Shaxs):
    """Sotuvchi klassi"""
    def __init__(self, ism, familiya, passport, tyil, ish_joyi, dokoni):
        super().__init__(ism, familiya, passport, tyil)
        self.ish_joyi = ish_joyi
        self.dokoni = dokoni
        
        
class Dokoni:
    """Sotuvchini do'koni haqida ma'lumotlar"""
    def __init__(self, nomi, manzili):
        self.d_nomi = nomi
        self.d_manzili = manzili
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.fanlar = []
    def fanga_yozil(self, science):
        self.fanlar.append(science)
    def remove_fan(self, science):
        self.fanlar.remove(science)
    def get_sciences(self):
        scis = []
        for fan in self.fanlar:
            scis.append(fan.fannomi)
        return scis
        
class Fan:
    def __init__(self, name, teacher, duration, science_type):
        self.fannomi = name
        self.fanteacher = teacher
        self.fandavomiyligi = duration
        self.fantipi = science_type
    
        

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
fan1 = Fan('matematika', 'alisher mamayusupov', 45, 'aniq fan')
fan2 = Fan('fizika', 'jaloliddin masharipov', 30, 'aniq fan')
fan3 = Fan('tarix', 'aziza raximova', 35, 'gumanitar')

talaba1 = Talaba("Valijon","Aliyev","FA112299",2000)
talaba1.fanga_yozil(fan1)


