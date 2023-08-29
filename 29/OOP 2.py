# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:05:39 2023

@author: MurodjonUser
"""

"""Avto degan yangi klass yarating. 
Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
(model, rang, korobka, narh va hokazo) qo'shing. 
Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
"""

class Avto:
    def __init__(self, model, rang, korobka, narh, made):
        self.model = model
        self.rang = rang
        self.karobka = korobka
        self.narh = narh
        self.yili = made
        self.speedometr = 0
    def get_info(self):
        return f"{self.model}, {self.yili}-yilda ishlab chiqarilgan. Rangi: {self.rang}, karobkasi: {self.karobka}, bosgan yo'li {self.speedometr}km. Sotsam {self.narh}$ ga sotiladi, InshaAlloh!"
    def update_km(self, km):
        self.speedometr += km
    
class AvtoSalon:
    def __init__(self, nomi, manzili, avtomobillari):
        self.salon_nomi = nomi
        self.salon_manzili = manzili
        self.salon_cars = avtomobillari
        
    def add_car(self, car):
        self.salon_cars.append(car)
    
    def get_inf(self):
        return f"Salon nomi: {self.salon_nomi.title()}, Manzil: {self.salon_manzili.title()}. Salonimizda quyidagi avtomobillar bor: {self.salon_cars}"
        
avto1 = Avto('tico', 'yashil', 'mexanika', 3000, '1998')
avto2 = Avto('matiz', 'oq', 'mexanika', 3500, '2004')

salon1 = AvtoSalon('AvtoTex', 'andijon vil. andijon tum.', ['tico','damas'])