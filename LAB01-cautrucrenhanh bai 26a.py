# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:09:23 2024

@author: DELL
"""

# Nhập 3 số từ bàn phím
a = int(input("Nhập số thứ nhất:"))
b = int(input("Nhập số thứ hai:"))
c = int(input("Nhập số thứ ba:"))
 # Giả sử a là số nhỏ nhất tạm thời
so_nho_nhat = a
# So sánh và hoán đổi để tìm số nhỏ nhất
if b < so_nho_nhat:
    so_nho_nhat = b
    b = a
    a = so_nho_nhat
if c < so_nho_nhat:
    so_nho_nhat = c
    c = a
    a = so_nho_nhat
# Bây giờ, a là số nhỏ nhất
# Tiếp tục so sánh b và c để tìm số lớn nhất
if b > c:
    b,c = c,b
# Hoán đổi b và c nếu b lớn hơn c
print(a, b, c)