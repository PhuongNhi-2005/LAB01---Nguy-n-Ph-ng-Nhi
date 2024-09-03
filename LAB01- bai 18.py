# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:03:14 2024

@author: DELL
"""

print("Nhập giờ thứ nhất:")
a=int(input("Giờ:"))
b=int(input("Phút:"))
c=int(input("Giây:"))
print("Nhập giờ thứ hai:")
x=int(input("Giờ:"))
y=int(input("Phút:"))
z=int(input("Giây:"))
if a>0 and a<24 and x>0 and x<=24 and b>=0 and b<60 and y>0 and y<60 and c>0 and c<60 and z>0 and z<60:
    print("aa",a+x,"giờ",b +y ,"phút" , c+z ,"giây")
    print("bb",abs(a-x),"giờ",abs(b -y) ,"phút" , abs(c-z) ,"giây")
else:
    print("sai rồi, nhập lại")