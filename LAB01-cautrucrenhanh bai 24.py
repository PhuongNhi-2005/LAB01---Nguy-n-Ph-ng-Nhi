# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:49:10 2024

@author: DELL
"""

a=int(input("Nhap gio:"))
b=int(input("Nhap phut:"))
c=int(input("Nhap giay:"))
if a>=0 and a<24 and b>=0 and b<60 and c>=0 and b<60:
    print("Giờ là", a,"giờ",b,"phut",c,"giây")
    print("Hợp lệ")
else:
    print("Không hợp lệ ")