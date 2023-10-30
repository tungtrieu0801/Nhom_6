import tkinter as tk
import sympy as sp

def solve_equations():
    # Lấy giá trị từ các trường đầu vào
    coefficients = []
    constants = []

    for i in range(num_equations):
        equation_coeffs = []
        for j in range(num_variables):
            equation_coeffs.append(float(entry_coeffs[i][j].get()))
        coefficients.append(equation_coeffs)
        constants.append(float(entry_constants[i].get()))

    # Tạo các biến và phương trình
    variables = sp.symbols('x0:%d' % num_variables)
    eqns = []
    for i in range(num_equations):
        eqn = sp.Eq(0, constants[i])
        for j in range(num_variables):
            eqn = eqn + variables[j] * coefficients[i][j]
        eqns.append(eqn)

    # Giải phương trình tuyến tính
    solution = sp.solve(eqns, variables)

    # Hiển thị kết quả trong vùng hiển thị
    result_label.configure(text="Kết quả:")
    for i, var in enumerate(variables):
        result_label.configure(text=result_label.cget("text") + f" {var} = {solution[var]:.2f}")

def update_entries():
    global num_equations, num_variables, entry_coeffs, entry_constants

    num_equations = int(num_equations_entry.get())
    num_variables = int(num_variables_entry.get())

    # Xóa các trường đầu vào hiện tại (nếu có)
    for i in range(len(entry_coeffs)):
        for j in range(num_variables):
            entry_coeffs[i][j].destroy()
        entry_constants[i].destroy()

    # Tạo các trường đầu vào mới
    entry_coeffs = []
    entry_constants = []
    for i in range(num_equations):
        equation_coeffs = []
        for j in range(num_variables):
            entry = tk.Entry(window)
            entry.grid(row=i+2, column=j+1)
            equation_coeffs.append(entry)
        entry_coeffs.append(equation_coeffs)

        entry = tk.Entry(window)
        entry.grid(row=i+2, column=num_variables+2)
        entry_constants.append(entry)

# Tạo cửa sổ giao diện
window = tk.Tk()

# Tạo trường nhập số phương trình và số ẩn
num_equations_label = tk.Label(window, text="Số phương trình:")
num_equations_label.grid(row=0, column=0)
num_equations_entry = tk.Entry(window)
num_equations_entry.grid(row=0, column=1)

num_variables_label = tk.Label(window, text="Số ẩn:")
num_variables_label.grid(row=0, column=2)
num_variables_entry = tk.Entry(window)
num_variables_entry.grid(row=0, column=3)

update_button = tk.Button(window, text="Cập nhật", command=update_entries)
update_button.grid(row=0, column=4)

# Tạo các trường đầu vào và nút giải
entry_coeffs = []
entry_constants = []
num_equations = 0
num_variables = 0

solve_button = tk.Button(window, text="Giải", command=solve_equations)
solve_button.grid(row=1, columnspan=6)

# Tạo vùng hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=2, columnspan=6)

# Chạy vòng lặp chính của ứng dụng
window.mainloop()