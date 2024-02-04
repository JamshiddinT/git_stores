#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:57:57 2024

@author: j
"""
#1-Asosi va balandligi berilgan uchburchakning yuzasini topish dasturini
#tuzing.
# Yechim: s=(1/2)*a*h;
# 
# bu yerda, a - uchburchakning asosi, h - uchburchakning balandligi.

import math

# a=10
# h=15

# s=(1/2)*a*h
#better way (a*h/2)
# print(s)

#2-Kiritilgan butun tipdagi n sonni n+nn+nnn ko`rinishida hisoblash dasturini
# tuzing.
# Masalan, n=5 -> 5+55+555=615

# n=5
# a=n+(n*10)
# b=n+(a*10)
# n=n+b+a
# print(n)

#yoki

# x=5
# x=x+(x*11)+(x*111)
# print(x)
# yoki
# a = int(input("Butun raqam kiriting: "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)


# # 3-.   1 dan N gacha musbat butun songacha bo`lgan sonlarning yig`indisini
# # hisoblash dasturini tuzing. arfmetik progressiya
# a=1 
# # b=N
# # b=int(input('Butun musbat raqam kiriting: '))
# n=b
# s=(a+b)*n/2
# # print(s)

# soniya=86399
# minut=soniya/60
# soat=minut/60
# kun=soat/23.99
# print(f"Bir kun: {round(kun)} sutka, {round(soat)} soat, {round(minut)} daqiqa va {soniya} soniyadan iborat.")


# vaqt=float(input("Sekund birligidagi vatni kiriting: "))
# kun=vaqt//(24*3600)
# vaqt=vaqt%(24*3600)
# soat=vaqt//3600
# vaqt%=3600
# daqiqa=vaqt//60
# vaqt%=60
# soniya=vaqt
# print("kun, soat, daqiqa, soniya-> %d:%d:%d:%d" %(kun, soat, daqiqa, soniya))


# son=input("Son kiriting: ")
# if son.isdigit():
#     print(son)
# else:
#     print("Siz son kiritmadingiz.")



# x = 5.0
# x_int = x.is_integer()
# print("x butun sonligini tekshirish!")
# print(x_int)
# y= 12.1
# y_int = y.is_integer()
# print("y butun sonligini tekshirish!")
# print(y_int)


# 2.9-masala. Satr sifatida ifodalangan ikkita musbat sonlar num1 va num2 berilgan
#bo'lsa, 1- va 2-sonning ko'paytmasini qaytaring.


# num1=6
# num2=7
# result=num1*num2
# print(result)


# def multiply(num1,num2):
#     a=int(num1)*int(num2)
#     return str(a)

# print(multiply("25", "5"))


#2.10-masala. tugri burchakli uchburchakning 
#bir birchagini gradusini topish.

# y=int(input("son kiriting: "))
# x=int(input("son kiriting: "))
# tau=math.atan((y/x))
# print(int(round(math.degrees(tau), 0)), sep='')

#2.11-masala. 𝑎, 𝑏, 𝑐, 𝑑 4 ta butun sonni kiritib, 𝑎𝑏 + 𝑐 𝑑 natijani chiqarish uchun Python
#dasturini yozing.

# a=int(input("son kiriting: "))
# b=int(input("son kiriting: "))
# c=int(input("son kiriting: "))
# d=int(input("son kiriting: "))

# result=(a**b)+(c**d)
# print(result)



# 2.12-masala
# Ixtiyoriy haqiqiy sonning n-butun darajasini hisoblash uchun Python
# dasturini yozing.
# Dastur kodi

# a=float(input("haqiqiy son kiriting: "))
# n=int(input("darajasini butun sonda kiriting: "))
# print(a**n)

# def myPow(x,n):
#     return math.pow(x,n)
# print(myPow(2.0,10))



#SATRLI MASALALAR.

#Pythonda original satrdagi berilgan simvollar sonini topuvchi dastur tuzing.
# count( ) funksiyasi.

s="Am a make a money, hassle everyday".lower()
print(f"Original satr: {s}")
print("Satrdagi 'a' simvollar soni: ", s.count("a"))

































