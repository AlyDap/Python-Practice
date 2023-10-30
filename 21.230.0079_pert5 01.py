# 1. Pandas Data Frame
# Pandas DataFrame adalah struktur data 2 Dimensi. Data distrukturisasi seperti tabel yang berisi baris dan kolom, sehingga mudah untuk melakukan
# queri atau mengakses data tersebut. Baris merepresentasikan record dan kolom merepresentasikan field

import pandas as pd

# Data Frame
data = pd.DataFrame(
    data={
        'Menu': ['Telur', 'Ikan', 'Soto'],
        'Harga': [5000, 2000, 3500]
    }
)
print(data, '\n')

# Membuat Index
data = pd.DataFrame(data={
    'ALI': ['SAKIT', 'IZIN'],
    'AHMAD': ['ALPHA', 'SAKIT'],
}, index=['Senin', 'Selasa']
)
print(data, '\n')


# series = data 1 kolom
data = pd.Series(data=[2, 4, 3.5, 1, 1.2])
print(data, '\n')

data = pd.Series(data=[2, 4, 3], index=['a', 'b', 'c'], name='Huruf')
print(data, '\n')

# membaca data csv pada DataFrame
data_wine = pd.read_csv('./winemag-data-130k-v2.csv')
# print(data_wine.head()) #menampilkan 5 data pertama
print(data_wine, '\n')  # menampilkan semua data

# Melihat Dimensi Data
print(data_wine.shape, '\n')

# Menggunakan salah 1 kolom sebagai index
data_wine = pd.read_csv('./winemag-data-130k-v2.csv', index_col=0)
print(data_wine.head(), '\n')  # menampilkan 5 data pertama

# Menyimpan DataFrame ke file csv
menu_minuman = pd.DataFrame(
    data={
        'Minuman': ['Kopi', 'Teh Anget', 'Jeruk Anget', 'Es Teh', 'Es Jeruk'],
        'Harga': [3000, 2500, 3000, 3500, 3500]
    }
)
print(menu_minuman, '\n')

menu_minuman.to_csv('menu_minuman_index.csv')  # akan membuat file csv

# Menyimpan DataFrame ke file CSV tanpa index
menu_minuman.to_csv('menu_minuman_noindex.csv', index=False)

# Membaca data excel pada dataframe
data_mhs = pd.read_excel('./data-mahasiswa.xlsx', sheet_name='data_mhs')
print(data_mhs.head(), '\n')

print(data_mhs.shape, '\n')

data_mhs = pd.read_excel('./data-mahasiswa.xlsx',
                         sheet_name='data_mhs', index_col=0)
print(data_mhs.head(), '\n')  # menampilkan 5 data pertama

# Menyimpan Data Frame ke file Excel tanpa index
menu_makanan = pd.DataFrame(
    data={
        'Makanan': ['Nasi Goreng', 'Mie Goreng', 'Mie Kuah'],
        'Harga': [3000, 2500, 3000]
    })
print(menu_makanan, '\n')
menu_makanan.to_excel('output1_noindex.xlsx', index=False)

# Mengakses kolom data frame
print(menu_minuman, '\n')

# Cara pertama atribut
print(menu_minuman.Minuman, '\n')

# Cara ke2 dictionary index
print(menu_minuman['Minuman'], '\n')

# Akses data pada frame
# Index-based selection
print('Index-based selection')
print(menu_minuman.iloc[0], '\n')
print(menu_minuman.iloc[2][0], '\n')  # ada warning

# Slicing iloc
print('Slicing ILOC')
print(menu_minuman.iloc[:, 0], '\n')
print(menu_minuman.iloc[0, :2], '\n')
print(menu_minuman.iloc[1:3, 0], '\n')

# Label-based selection
print('Label based selection')
print(menu_minuman.loc[0, 'Minuman'], '\n')
print(menu_minuman.loc[0:3, 'Minuman'], '\n')

# memanggil kolom tertentu, dan menampilkan 5 data pertama
print(menu_minuman.loc[:, ['Minuman', 'Harga']].head(), '\n')
print(menu_minuman[['Minuman', 'Harga'][:5]], '\n')

# Hapus Data
print('Hapus Data')
data = pd.DataFrame(
    data={
        'Menu': ['Nasi Goreng', 'Nasi Megono', 'Tempe Goreng', 'Nasi Goreng'],
        'Harga': [14000, 5000, 2500, 14000]
    })
print(data, '\n')

df = data.drop_duplicates(subset=['Menu'], keep='first')
print(df, '\n')
