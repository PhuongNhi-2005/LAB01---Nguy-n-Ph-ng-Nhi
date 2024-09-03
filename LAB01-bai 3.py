# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:48:34 2024

@author: Phương Nhi
"""

a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
if a>0 and b>0:
    x=a%b
    y=a//b
    print("Chia lay du cua 2 so a va b la:",x)
    print("Chia lay nguyen cua 2 so a va b la:",y)
else:
    print("Sai rồi, mời nhập lại")
