# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:47:36 2023
Object Oriented Programming

Telegram: @MurodjonYusuf
"""

"""Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan 
ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
"""

class User:
    def __init__(self, ism, familiya, username, tel_raqam, email):
        """User xususiyatlari"""
        self.ismi = ism
        self.familiyasi = familiya
        self.username = username
        self.telefoni = tel_raqam
        self.email = email
    def salomlash(self):
        salom = f"Salom {self.ismi.title()}, web saytimizga xush kelibsiz!"
        return salom
    def get_info(self):
        infos = {
            'ismi':self.ismi,
            'familiyasi':self.familiyasi,
            'telefon raqami':self.telefoni,
            'pochtasi':self.email
            }
        return infos