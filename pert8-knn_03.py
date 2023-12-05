import pandas as pd
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
os.system('cls')
# Menginisialisasi LabelEncoder
label_encoder = LabelEncoder()

# Mendapatkan direktori saat ini dan menggunakannya
current_directory = os.getcwd()
print(current_directory)
os.chdir(current_directory)

nama_file = 'latihan.xlsx'
sheet_names = 'Sheet1'
daftar_sheet = pd.ExcelFile(nama_file).sheet_names
print('\nDaftar Sheet: ', daftar_sheet, '\n')

df = pd.read_excel(nama_file, sheet_name=sheet_names)
print(f'\nData pada excel keseluruhan:\n{df}\n')

X = df.iloc[0:8, 1:4].values
Y = df.iloc[0:8, 4:5].values
print(f'Ini data pada X:\n{X}\n')
print(f'Ini data pada Y:\n{Y}\n')

# # ERROR ValueError: could not convert string to float: 'tua'
# # X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2)
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
# knn_klasifikasi = KNeighborsClassifier(n_neighbors=3)
# knn_klasifikasi.fit(X_train, np.ravel(Y_train))

# data_yang_dicek = ['muda', 'overweight', 'wanita']
# cek_data = [data_yang_dicek]
# prediksinya = knn_klasifikasi.predict(cek_data)
# print(
#     f'Hasil prediksi dari cek_data {data_yang_dicek} masuk ke kelas: {prediksinya[0]}\n')
