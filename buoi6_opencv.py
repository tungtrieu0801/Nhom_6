import cv2
import tkinter as tk
from tkinter import ttk

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
    # Hiển thị ảnh gốc
    cv2.imshow('Original Image', original_image)
    # Hiển thị ảnh co dãn
    cv2.imshow('Zoomed Image', zoomed_img)


# Đọc ảnh
original_image = cv2.imread('anhmeo.jpg')

# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Zoom Image")

# Tạo nút nhấn
zoom_in_button = ttk.Button(root, text="Zoom In", command=zoom_in)
zoom_in_button.pack()

zoom_out_button = ttk.Button(root, text="Zoom Out", command=zoom_out)
zoom_out_button.pack()

# Khởi tạo biến tỉ lệ co dãn
scale_factor = 1.0

update_images()
root.mainloop()
cv2.destroyAllWindows()