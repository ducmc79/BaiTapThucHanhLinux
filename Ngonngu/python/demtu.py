import re

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập vào một chuỗi: ")

# Tách các từ (bỏ qua các dấu câu cơ bản)
danh_sach_tu = re.findall(r'\b\w+\b', chuoi)

# Đếm số từ
so_tu = len(danh_sach_tu)
print(f"Số từ trong chuỗi: {so_tu}")

# Liệt kê các từ dài hơn 5 ký tự
tu_dai_hon_5 = [tu for tu in danh_sach_tu if len(tu) > 5]

print("Các từ dài hơn 5 ký tự là:")
if tu_dai_hon_5:
    for tu in set(tu_dai_hon_5): # Sử dụng set để lọc các từ trùng lặp
        print(f"- {tu} ({len(tu)} ký tự)")
else:
    print("Không có từ nào dài hơn 5 ký tự.")
