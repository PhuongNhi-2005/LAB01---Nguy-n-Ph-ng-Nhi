# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:35:42 2024

@author: DELL
"""

def doc_so(so):
  chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
  if 0 <= so <= 9:
    return chu_so[so]
  else:
    print ("Không đọc được")
a = int(input("Nhập một số nguyên: "))
ket_qua = doc_so(a)
print(ket_qua)

