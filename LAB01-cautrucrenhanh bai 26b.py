# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:52:26 2024

@author: DELL
"""

a = int(input("Nhập số: "))
# Chuyển số thành chuỗi
chuoi_so = str(a)
# từ chuỗi số đưa vào danh sách
list_so = list(chuoi_so)
#sắp xếp danh sách các chữ số theo thứ tự tăng dần
list_so.sort()
# Nối các chữ số lại thành một chuỗi
so_moi = ''.join(list_so)
print(so_moi)