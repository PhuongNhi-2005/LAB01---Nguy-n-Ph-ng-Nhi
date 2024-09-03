# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:53:12 2024

@author: Phương Nhi
"""

x=int(input("So nguyen duong co 2 chu so la:"))
if x>=10 and x<=99:
    a=x//10
    b=x%10
    print("Tong 2 chu so cua so nguyen duong do la:",a+b)
else:
    print("Nhap sai roi, nhap lai mau")