# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:23:18 2024

@author: DELL
"""

import string
a=int(input("Nhập biển số xe bạn vào đây:"))
if a>=1000 and a<=9999:
    x=str(a)
    sodautien=x[0:1]
    sothu2=x[1:2]
    sothu3=x[2:3]
    sothu4=x[3:4]
    b=int(sodautien)
    c=int(sothu2)
    d=int(sothu3)
    e=int(sothu4)
    print("Số nút của xe bạn là:",(b+c+d+e)%10)
else:
    print("Sai rồi, nhập lại")
