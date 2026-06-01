#!/usr/bin/fish

# Đếm số dòng có chuỗi "Việt Nam" trong file monan2.csv bằng lệnh grep
set count (grep -c "Việt Nam" /home/kvasir/Documents/Linux/Duc_2300135/Monan/Thucdon/monan2.csv)

echo "Số dòng chứa chuỗi 'Việt Nam' là: $count"
