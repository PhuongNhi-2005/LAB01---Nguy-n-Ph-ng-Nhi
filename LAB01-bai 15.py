# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:16:11 2024

@author: DELL
"""

import math
a=float(input("Nhap so thuc a:"))
b=float(input("Nhap so thuc b:"))
B=((math.sqrt(a)-math.sqrt(b))/(pow(a,1/4)-pow(b,1/4)))-((math.sqrt(a)+pow(a*b,1/4))/(pow(a,1/4)+pow(b,1/4)))
print("Ket qua la:",round(B,3))