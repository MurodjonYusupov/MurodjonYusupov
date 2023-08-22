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
        
avto1 = Avto('tico', 'yashil', 'mexanika', 3000, '1998')