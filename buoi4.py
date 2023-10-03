import sympy as sp
import tkinter as tk
from tkinter import Label, Entry, Button, Frame

# Hàm giải phương trình
def solve_equation():
    equation_str = equation_entry.get()
    x = sp.symbols('x')
    equation = sp.Eq(sp.sympify(equation_str), 0)
    solution = sp.solve(equation, x)
    equation_result_label.config(text=f"Kết quả: {solution}")

# Hàm tính đạo hàm
def calculate_derivative():
    expression_str = derivative_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    derivative = sp.diff(expression, x)
    derivative_result_label.config(text=f"Đạo hàm: {derivative}")

# Hàm tính tích phân
def calculate_integral():
    expression_str = integral_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    lower_limit = sp.sympify(integral_lower_limit_entry.get())
    upper_limit = sp.sympify(integral_upper_limit_entry.get())
    integral = sp.integrate(expression, (x, lower_limit, upper_limit))
    integral_result_label.config(text=f"Tích phân: {integral}")

def calculate_limit():
    expression_str = limit_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    limit_point = sp.sympify(limit_point_entry.get())
    limit_result = sp.limit(expression, x, limit_point)
    limit_result_label.config(text=f"Giới hạn: {limit_result}")

# Tạo giao diện tkinter
root = tk.Tk()
root.title("Tính Đạo Hàm và Tích Phân")
root.geometry("400x400")
# Frame cho giải phương trình
equation_frame = Frame(root)
equation_frame.pack()
equation_label = Label(equation_frame, text="Giải phương trình:")
equation_label.pack()
equation_entry = Entry(equation_frame)
equation_entry.pack()
solve_equation_button = Button(equation_frame, text="Giải", command=solve_equation)
solve_equation_button.pack()
equation_result_label = Label(equation_frame, text="Kết quả: ")
equation_result_label.pack()
# Frame cho tính đạo hàm
derivative_frame = Frame(root)
derivative_frame.pack()
derivative_label = Label(derivative_frame, text="Tính đạo hàm:")
derivative_label.pack()
derivative_entry = Entry(derivative_frame)
derivative_entry.pack()
calculate_derivative_button = Button(derivative_frame, text="Tính", command=calculate_derivative)
calculate_derivative_button.pack()
derivative_result_label = Label(derivative_frame, text="Đạo hàm: ")
derivative_result_label.pack()

# Frame cho tính tích phân
integral_frame = Frame(root)
integral_frame.pack()
integral_label = Label(integral_frame, text="Tính tích phân (cận trên và dưới):")
integral_label.pack()
integral_entry = Entry(integral_frame)
integral_entry.pack()
integral_lower_limit_label = Label(integral_frame, text="Giới hạn dưới:")
integral_lower_limit_label.pack()
integral_lower_limit_entry = Entry(integral_frame)
integral_lower_limit_entry.pack()
integral_upper_limit_label = Label(integral_frame, text="Giới hạn trên:")
integral_upper_limit_label.pack()
integral_upper_limit_entry = Entry(integral_frame)
integral_upper_limit_entry.pack()
calculate_integral_button = Button(integral_frame, text="Tính", command=calculate_integral)
calculate_integral_button.pack()
integral_result_label = Label(integral_frame, text="Tích phân: ")
integral_result_label.pack()

# Frame cho tính giới hạn
limit_frame = Frame(root)
limit_frame.pack()
limit_label = Label(limit_frame, text="Tính giới hạn (tại một điểm):")
limit_label.pack()
limit_entry = Entry(limit_frame)
limit_entry.pack()
limit_point_label = Label(limit_frame, text="Điểm giới hạn:")
limit_point_label.pack()
limit_point_entry = Entry(limit_frame)
limit_point_entry.pack()
calculate_limit_button = Button(limit_frame, text="Tính", command=calculate_limit)
calculate_limit_button.pack()
limit_result_label = Label(limit_frame, text="Giới hạn: ")
limit_result_label.pack()
# Khởi chạy giao diện
root.mainloop()
