# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:56:04 2024

@author: DELL
"""
    
#Giai phuong trinh bac nhat
a=float(input("Nhap gia tri a:"))
b=float(input("Nhap gia tri b:"))
if a==0:
    print("Phuong trinh vo nghiem")
elif a>0:
        print("Phuong trinh co nghiem la",-b/a)
elif a<0:
    print("Phuong trinh co nghiem la",b/a)
# biện luận: cho 2 số thực a và b trong phương trinh bậc nhất: ax+b=0
#1 Nếu a = 0 thì phương trình vô nghiệm
#2 Nếu a>0 thì phương trình có nghiệm là -b/a
#3 Nếu a<0 thì phương trình có nghiệm là b/a