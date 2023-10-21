import cv2
import tkinter as tk
from tkinter import ttk

#xoay anh
def rotate_image():
    global original_image
    angle = float(angle_entry.get())  # Lấy góc quay từ hộp văn bản
    matrix = cv2.getRotationMatrix2D((original_image.shape[1] / 2, original_image.shape[0] / 2), angle, 1)
    original_image = cv2.warpAffine(original_image, matrix, (original_image.shape[1], original_image.shape[0]))
    update_imagesxoay()
def update_imagesxoay():
    cv2.imshow('anh goc', original_image)
    cv2.waitKey(1)
#zoom
def zoom_in():
    global scale_factor
    scale_factor += 0.1
    update_images()

def zoom_out():
    global scale_factor
    scale_factor -= 0.1
    update_images()

def update_images():
    # Tạo ảnh co dãn
    zoomed_img = cv2.resize(original_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    # Hiển thị ảnh co dãn
    cv2.imshow('anh goc', zoomed_img)
def chuan_hoa_anh():
    global original_image
    final = cv2.normalize(original_image, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imshow("anh goc",final)
def bien_anh():
    global original_image
    img_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    edges=cv2.Canny(image=img_rgb,threshold1=0,threshold2=200)
    cv2.imshow("anh goc",edges)
# Đọc ảnh
original_image = cv2.imread('anhmeo.jpg')

# Hiển thị ảnh gốc
cv2.imshow('anh goc', original_image)
# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Chức năng với ảnh")

# Tạo nhãn và hộp văn bản để nhập góc quay
angle_label = tk.Label(root, text="Nhập góc quay (độ):")
angle_label.pack()
angle_entry = tk.Entry(root)
angle_entry.pack()
# Tạo nút để thực hiện phép quay
rotate_button = tk.Button(root, text="Quay ảnh", command=rotate_image)
rotate_button.pack()

# Tạo nút nhấn
zoom_in_button = tk.Button(root, text="Zoom In", command=zoom_in)
zoom_in_button.pack()

zoom_out_button = tk.Button(root, text="Zoom Out", command=zoom_out)
zoom_out_button.pack()

chuan_hoa_button = tk.Button(root, text="Chuẩn hóa ảnh", command=chuan_hoa_anh)
chuan_hoa_button.pack()

bien_anh_button = tk.Button(root, text="Biên ảnh", command=bien_anh)
bien_anh_button.pack()

# Khởi tạo biến tỉ lệ co dãn
scale_factor = 1.0

root.mainloop()
cv2.destroyAllWindows()
