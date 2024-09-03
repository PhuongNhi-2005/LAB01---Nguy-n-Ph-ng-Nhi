# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:46:34 2024

@author: DELL
"""

a = int(input("Nhập ngày:"))
b = int(input("Nhập tháng:"))
c = int(input("Nhập năm:"))
ngay = str(a)
thang = str(b)
nam = str(c)
x=ngay+"/"+thang+"/"+nam[2:4]
print("Ngày tháng năm bạn đã nhập là:",x)
