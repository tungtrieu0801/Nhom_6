import sympy as sp
import tkinter as tk
from tkinter import Label, Entry, Button

# Hàm tính đạo hàm và tích phân
def calculate_derivative_integral():
    expression_str = expression_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    
    # Tính đạo hàm của biểu thức theo x
    derivative = sp.diff(expression, x)
    
    # Tính tích phân của biểu thức theo x
    integral = sp.integrate(expression, x)
    
    # Hiển thị kết quả lên giao diện
    derivative_label.config(text=f"Đạo hàm: {derivative}")
    integral_label.config(text=f"Tích phân: {integral}")

# Tạo giao diện tkinter
root = tk.Tk()
root.title("Tính Đạo Hàm và Tích Phân")
root.geometry("400x400")

# Nhập biểu thức
expression_label = Label(root, text="Nhập biểu thức:")
expression_label.pack()
expression_entry = Entry(root)
expression_entry.pack()

# Button để tính đạo hàm và tích phân
calculate_button = Button(root, text="Tính", command=calculate_derivative_integral)
calculate_button.pack()

# Kết quả đạo hàm và tích phân
derivative_label = Label(root, text="Đạo hàm: ")
derivative_label.pack()
integral_label = Label(root, text="Tích phân: ")
integral_label.pack()

# Khởi chạy giao diện
root.mainloop()
