# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:27:09 2024

@author: DELL
"""

a=float(input("Nhap can nang cua ban(kg):"))
b=float(input("Nhap chieu cao cua ban(m):"))
if a>0 and b>0:
    x=a/(b**2)
    print("BMI cua ban la:",x)
else:
    print("Nhap sai roi kia, nhap lai di")
    