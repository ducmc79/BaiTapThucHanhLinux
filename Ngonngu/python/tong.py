#!/usr/bin/env python3

try:
    n = int(input("Nhập vào một số nguyên dương N: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên lớn hơn 0.")
    else:
        # Tính tổng các số chẵn trong khoảng từ 1 đến N
        tong = sum(i for i in range(1, n + 1) if i % 2 == 0)
        print(f"Tổng các số chẵn từ 1 đến {n} là: {tong}")
        
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ! Vui lòng nhập số nguyên.")
