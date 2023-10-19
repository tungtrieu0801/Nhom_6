import pandas as pd
import tkinter as tk
from tkinter import ttk
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import numpy as np

# Đọc tệp CSV
df = pd.read_csv('diemPython.csv')  # Thay 'duong_dan_den_tep_csv.csv' bằng đường dẫn tới tệp CSV của bạn
df['Mã lớp'] = df['Mã lớp'].str.strip('"')

# Hàm xem kết quả
def xem_ket_qua():
    ket_qua.config(text=tong_sinh_vien)
    lop = lop_dropdown.get()
    diem = diem_dropdown.get()
    filtered_df = df[df['Mã lớp'] == lop][diem]
    if not filtered_df.empty:
        ket_qua.config(text=str(filtered_df.values[0]))
    else:
        ket_qua.config(text="Chưa có dữ liệu cho lựa chọn này")

# Hàm tính trung bình cộng theo loại điểm và lớp
def tinh_trung_binh_cong():
    lop = lop_dropdown.get()
    diem = diem_lop_dropdown.get()

    filtered_df = df[df['Mã lớp'] == lop][diem]
    if not filtered_df.empty:
        diem_trung_binh = filtered_df.mean()
        ket_qua.config(text=f"Số {diem} của lớp {lop}: {diem_trung_binh:}")
    else:
        ket_qua.config(text="Chưa có dữ liệu cho lựa chọn này")

# Tạo cua so
root = tk.Tk()
root.geometry("600x600")
root.title("Ứng dụng Dropdown Box")

# Hiển thị lựa chọn "Xem tổng số sinh viên tham gia môn học"
tong_sinh_vien = tk.Label(root, text="", padx=10, pady=10)
tong_sinh_vien.pack()

# Dropdown box cho lựa chọn lớp
lop_options = df['Mã lớp'].unique()
lop_options = [option.replace("'", "") for option in lop_options]
lop_dropdown = ttk.Combobox(root, values=lop_options)
lop_dropdown.set(lop_options[0])  # Thiết lập giá trị mặc định
lop_dropdown.pack()

diem_options = ["Loại A+", "Loại A", "Loại B+", "Loại B", "Loại C+", "Loại C"]
diem_dropdown = ttk.Combobox(root, values=diem_options)
diem_dropdown.set(diem_options[0])  # Thiết lập giá trị mặc định
diem_dropdown.pack()

diem_lop_options = ["Loại A+", "Loại A", "Loại B+", "Loại B", "Loại C+", "Loại C"]
diem_lop_dropdown = ttk.Combobox(root, values=diem_lop_options)
diem_lop_dropdown.set(diem_lop_options[0])  # Thiết lập giá trị mặc định
diem_lop_dropdown.pack()

xem_ket_qua_button = tk.Button(root, text="Xem kết quả", command=xem_ket_qua)
xem_ket_qua_button.pack()


tinh_tb_button = tk.Button(root, text="Chi tiết từng loại điểm ", command=tinh_trung_binh_cong)
tinh_tb_button.pack()

ket_qua = tk.Label(root, text="", padx=10, pady=10)
ket_qua.pack()

# Lấy tổng số sinh viên tham gia môn học
in_data = array(df.iloc[:, 2])
tong_sinh_vien["text"] = "Tổng số sinh viên tham gia môn học: " + str(np.sum(in_data))

# Bắt đầu vòng lặp chạy ứng dụng
root.mainloop()
