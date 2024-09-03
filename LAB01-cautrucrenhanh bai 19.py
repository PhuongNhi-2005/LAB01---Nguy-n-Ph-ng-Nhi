# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:42:30 2024

@author: DELL
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))

# Giả sử số a là số nhỏ nhất ban đầu
so_nho_nhat = a
# So sánh và cập nhật giá trị nhỏ nhất
if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat:
    so_nho_nhat = d
print("Số nhỏ nhất là:", so_nho_nhat)