# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:02:21 2024

@author: Phương 
"""

a=int(input("Nhap gio:"))
b=int(input("Nhap phut:"))
c=int(input("Nhap giay:"))
if a>=0 and a<24 and b>=0 and b<60 and c>=0 and b<60:
    print("Gio la", a,"giờ",b,"phut",c,"giây")
    x=a*3600
    y=b*60
    print("Tong so giay duoc quy doi ra la:",x+y+c)
else:
    print("Sai rồi nhập lại mau")