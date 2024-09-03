# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:53:33 2024

@author: DELL
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))

# Giả sử số a là số lớn nhất ban đầu
so_lon_nhat = a
# So sánh và cập nhật giá trị lớn 
if b > so_lon_nhat:
    so_lon_nhat= b
if c > so_lon_nhat:
    so_lon_nhat = c
if d > so_lon_nhat:
    so_lon_nhat = d
print("Số lớn nhất là:", so_lon_nhat)