# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:42:45 2024

@author: DELL
"""

#Giai phuong trinh bac hai
a=float(input("Nhap gia tri a:"))
b=float(input("Nhap gia tri b:"))
c=float(input("Nhap gia tri c:"))
d=float(b**2-4*a*c)
if d==0:
    print("Phuong trinh co nghiem kep",-b/2*a)
elif d>0:
    print("Phuong trinh co hai nghiem phan biet:",(-b+d**0.5)/(2*a),(-b-d**0.5)/(2*a))
else:
    print("Phuong trinh vo nghiem")
#Biện luận: Cho 3 số thực a,b,c trong phương trình bậc hai: ax^2 + bx + c = 0
# delta (d)=  b^2-4xaxc
#1 Nếu delta = 0 thì Phương trình có nghiệm kép là -b/2xa
#2 Nếu delta > 0 thì Phương trình có hai nghiệm phân biệt là (-b+d**0.5)/(2*a) và (-b-d**0.5)/(2*a)
#3 Nếu delta < 0 thì Phương trình vô nghiệm