import cv2
import tkinter as tk
from tkinter import ttk

class ImageProcessor:
    def __init__(self, image_path):
        self.scale_factor = 1.0
        self.original_image = cv2.imread(image_path)

        self.root = tk.Tk()
        self.root.title("Chức năng với ảnh")

        self.angle_label = tk.Label(self.root, text="Nhập góc quay (độ):")
        self.angle_label.pack()

        self.angle_entry = tk.Entry(self.root)
        self.angle_entry.pack()

        self.rotate_button = tk.Button(self.root, text="Quay ảnh", command=self.rotate_image, width=20, height=2)
        self.rotate_button.pack()

        self.zoom_scale = tk.Scale(self.root, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL,
                                   label="Zoom Scale", command=self.update_images)
        self.zoom_scale.set(self.scale_factor)
        self.zoom_scale.pack()

        self.chuan_hoa_button = tk.Button(self.root, text="Chuẩn hóa ảnh", command=self.chuan_hoa_anh, width=20, height=2)
        self.chuan_hoa_button.pack()

        self.bien_anh_button = tk.Button(self.root, text="Biên ảnh", command=self.bien_anh, width=20, height=2)
        self.bien_anh_button.pack()

        self.display_image(self.original_image)

        self.root.mainloop()

    def rotate_image(self):
        angle = float(self.angle_entry.get())
        matrix = cv2.getRotationMatrix2D((self.original_image.shape[1] / 2, self.original_image.shape[0] / 2),
                                         angle, 1)
        self.original_image = cv2.warpAffine(self.original_image, matrix,
                                              (self.original_image.shape[1], self.original_image.shape[0]))
        self.update_images()

    def update_images(self, scale=None):
        if scale:
            self.scale_factor = float(scale)
        zoomed_img = cv2.resize(self.original_image, None, fx=self.scale_factor, fy=self.scale_factor,
                                interpolation=cv2.INTER_LINEAR)
        self.display_image(zoomed_img)

    def chuan_hoa_anh(self):
        final = cv2.normalize(self.original_image, None, 0, 255, cv2.NORM_MINMAX)
        self.display_image(final)

    def bien_anh(self):
        img_rgb = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        edges = cv2.Canny(image=img_rgb, threshold1=0, threshold2=200)
        self.display_image(edges)

    def display_image(self, image):
        cv2.imshow('anh goc', image)
        cv2.waitKey(1)


if __name__ == "__main__":
    image_path = "anh.png"  # Thay đổi đường dẫn đến ảnh của bạn
    ImageProcessor(image_path)