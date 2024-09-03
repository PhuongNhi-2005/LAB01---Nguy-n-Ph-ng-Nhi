# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:04:47 2024

@author: DELL
"""

hinh=input("Nhập hình:")
if hinh == "v":
    print("Tính P và S cua hình vuông")
    canh=float(input("Nhập cạnh hình vuông:"))
    print("Diện tích là:", canh * canh)
    print("Chu vi là:",4*canh)
elif hinh == "n":
    print("Tính P và S của hình chữ nhật")
    chieu_dai=float(input("Nhập chiều dài:"))
    chieu_rong=float(input("Nhập chiều rộng:"))
    print("Diện tích là:",chieu_dai * chieu_rong)
    print("Chu vi là:",2 * (chieu_dai + chieu_rong))
elif hinh == "t":
    print("Tính P và S của hình tròn")
    ban_kinh=float(input("Nhập bán kính:"))
    print("Diện tích là:",3,14 * ban_kinh**2)
    print("Chu vi là:", 2 *3,14* ban_kinh)
else:
    print("Không có hình khả dụng trong trường hợp này.")
