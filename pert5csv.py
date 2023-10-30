# pip list => untuk melihat list
# pip install pandas => menginstall pandas
import pandas as pd
import os
os.chdir("D:\\KULIAH S1 SI STMIK WP\SEMESTER 5\\1.1 Visualisasi Data dan Data Sciences\\Praktek\\Tugas")

# file_path = r'D:\KULIAH S1 SI STMIK WP\SEMESTER 5\1.1 Visualisasi Data dan Data Sciences\Praktek\Tugas\baru.csv'
# data = pd.read_csv(file_path)

# Membaca file CSV
# data=pd.read_csv('machine.csv')
data = pd.read_csv('baru.csv')

print(data)
print(f'Dimenasi data nya {data.shape}')
