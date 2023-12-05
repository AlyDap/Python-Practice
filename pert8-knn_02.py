import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import os

# Mendapatkan direktori saat ini dan menggunakannya
current_directory = os.getcwd()
print(current_directory)
os.chdir(current_directory)

nama_file = 'pert8-Book1.xlsx'
sheet_names = 'Sheet2'
daftar_sheet = pd.ExcelFile(nama_file).sheet_names
print('\nDaftar Sheet: ', daftar_sheet, '\n')

df = pd.read_excel(nama_file, sheet_name=sheet_names)
print(f'\nData pada excel keseluruhan:\n{df}\n')

X = df.iloc[1:11, 1:6].values
Y = df.iloc[1:11, 6:7].values
print(f'Ini data pada X:\n{X}\n')
print(f'Ini data pada Y:\n{Y}\n')

# X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
knn_klasifikasi = KNeighborsClassifier(n_neighbors=5)
knn_klasifikasi.fit(X_train, np.ravel(Y_train))

data_yang_dicek = [173, 70, 75, 90, 31]
cek_data = [data_yang_dicek]
prediksinya = knn_klasifikasi.predict(cek_data)
print(
    f'Hasil prediksi dari cek_data {data_yang_dicek} masuk ke kelas: {prediksinya[0]}\n')
