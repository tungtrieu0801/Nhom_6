import numpy as np

n = int(input("Nhap n: "))

a = np.zeros((n, n))
b = np.zeros((n))
for i in range(n):
    for j in range(n):
        a[i, j] = float(input(f"a{i + 1},{j + 1}: "))
for i in range(n):
    b[i] = float(input(f"b{i + 1}: "))
det=np.linalg.det(a)
if det==0:
    print("he vo nghiem hoac vo so nghiem")

x = np.linalg.solve(a, b)
print(x)

tung commit
truong commit
