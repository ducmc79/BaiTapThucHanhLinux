#!/bin/bash

FILE_PATH="$HOME/Documents/Linux/Duc_2300135/Sanpham/Doanh thu/doanhso.csv"

if [ ! -f "$FILE_PATH" ]; then
    echo "Không tìm thấy file doanhso.csv!"
    exit 1
fi

# Dùng awk để bỏ dòng tiêu đề và cộng dồn cột số 2
tong=$(awk -F',' 'NR>1 {sum+=$2} END {print sum}' "$FILE_PATH")

echo "Tổng doanh thu trong file doanhso.csv là: $tong"
