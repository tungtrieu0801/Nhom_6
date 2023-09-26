import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])
tongsv = in_data[:, 1]
print("Tổng sinh viên tham gia môn học: ", np.sum(tongsv))

diemA = in_data[:, 3]
diemBc = in_data[:, 4]
diemB = in_data[:, 5]
diemCc = in_data[:, 6]
diemC = in_data[:, 7]
diemDc = in_data[:, 8]
diemD = in_data[:, 9]
diemF = in_data[:, 10]
print("Tổng sinh viên đạt A: ", np.sum(diemA))
print("Tổng sinh viên đạt B+: ", np.sum(diemBc))
print("Tổng sinh viên đạt B: ", np.sum(diemB))
print("Tổng sinh viên đạt C+: ", np.sum(diemCc))
print("Tổng sinh viên đạt C: ", np.sum(diemC))
print("Tổng sinh viên đạt D+: ", np.sum(diemDc))
print("Tổng sinh viên đạt D+: ", np.sum(diemD))
print("Tổng sinh viên đạt F: ", np.sum(diemF))

print("Tbc sinh viên đạt A: ", np.mean(diemA))
print("Tbc sinh viên đạt B+: ", np.mean(diemBc))
print("Tbc sinh viên đạt B: ", np.mean(diemB))
print("Tbc sinh viên đạt C+: ", np.mean(diemCc))
print("Tbc sinh viên đạt C: ", np.mean(diemC))
print("Tbc sinh viên đạt D+: ", np.mean(diemDc))
print("Tbc sinh viên đạt D+: ", np.mean(diemD))
print("Tbc sinh viên đạt F: ", np.mean(diemF))

arr_sv = in_data[:, 1]
arr_svl1 = in_data[:, 11]
arr_svl2 = in_data[:, 12]
arr_svtx1 = in_data[:, 13]
arr_svtx2 = in_data[:, 14]
arr_svck = in_data[:, 15]
kdatl1 = np.subtract(arr_sv, arr_svl1)
kdatl2 = np.subtract(arr_sv, arr_svl2)
kdattx1 = np.subtract(arr_sv, arr_svtx1)
kdattx2 = np.subtract(arr_sv, arr_svtx2)
kdatck = np.subtract(arr_sv, arr_svck)
print("Tổng sinh viên không đạt L1: ", np.sum(kdatl1))
print("Tổng sinh viên không đạt L2: ", np.sum(kdatl2))
print("Tổng sinh viên không đạt TX1: ", np.sum(kdattx1))
print("Tổng sinh viên không đạt TX2: ", np.sum(kdattx2))
print("Tổng sinh viên không đạt cuối kỳ: ", np.sum(kdatck))

maxa = diemA.max()
i, = np.where(diemA == maxa)
mina = diemA.min()
z, = np.where(diemA == mina)
print('Lớp có nhiều điểm A là {0} có {1} sv đạt điểm A'.format(in_data[i, 0], maxa))
print('Lớp có ít điểm A là {0} có {1} sv đạt điểm A'.format(in_data[z, 0], mina))
plt.plot(range(len(diemA)), diemA, 'r-', label="Diem A")
plt.plot(range(len(diemBc)), diemBc, 'g-', label="Diem B +")
plt.plot(range(len(diemB)), diemB, 'b-', label="Diem B")
plt.plot(range(len(diemCc)), diemCc, 'c-', label="Diem C+")
plt.plot(range(len(diemC)), diemC, 'm-', label="Diem C")
plt.plot(range(len(diemDc)), diemDc, 'y-', label="Diem D+")
plt.plot(range(len(diemD)), diemD, 'k-', label="Diem D")
plt.plot(range(len(diemF)), diemF, 'p-', label="Diem F")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()

