# Visualisasi Data Pada Pandas Data frame Lanjutan

# import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspex
import pandas as pd

# Sample Data Frame
data = {'Tahun': ['2017', '2018', '2019', '2020', '2021', '2022'],
        'Jumlah': [551, 450, 400, 425, 350, 331]}
print(data)
df = pd.DataFrame(data)
print(df)

# Line plot sederhana
df.plot(x='Tahun', y='Jumlah', kind='line')
plt.title('Data Penerimaan Siswa Baru')
plt.ylabel('Populasi')
plt.xlabel('Tahun')
plt.show()

# Bar plot
data = {'Mahasiswa': ['Andi', 'Bandi', 'Candi', 'Dandi', 'Endi'],
        'ipk': [3.5, 4.0, 3.0, 3.7, 2.9]}
print(data)
df = pd.DataFrame(data)
print(df)

df.plot(x='Mahasiswa', y='ipk', kind='bar')
plt.title('IPK Mahasiswa')
plt.ylabel('IPK')
plt.xlabel('Nama Mahasiswa')
plt.show()

df.plot(x='Mahasiswa', y='ipk', kind='barh')
plt.title('IPK Mahasiswa')
plt.ylabel('IPK')
plt.xlabel('Nama Mahasiswa')
plt.show()

df.plot(x='Mahasiswa', y='ipk', kind='barh', color='g')
plt.title('IPK Mahasiswa')
plt.ylabel('IPK')
plt.xlabel('Nama Mahasiswa')
plt.show()

# Scatter plot
data = {'Mahasiswa': ['Andi', 'Bandi', 'Candi', 'Dandi', 'Endi'],
        'ipk': [3.5, 4.0, 3.0, 3.7, 2.9],
        'umur': [21, 20, 26, 23, 30]}
print(data)
df = pd.DataFrame(data)
print(df)

df.plot(x='Mahasiswa', y='ipk', kind='scatter', color='r')
plt.title('Data Mahasiswa')
plt.ylabel('IPK')
plt.xlabel('Nama')
plt.show()

# Pie plot
data = {'Tahun': ['2017', '2018', '2019', '2020', '2021', '2022'],
        'Jumlah': [800, 450, 400, 425, 350, 331]}
df = pd.DataFrame(data)
df.plot(kind='pie', y='Jumlah', figsize=(6, 6))
plt.title('Jumlah Siswa Baru')
plt.show()

df = df.set_index('Tahun')
df.plot(kind='pie', y='Jumlah', figsize=(6, 6))
plt.title('Jumlah Siswa Baru')
plt.show()

# Box Plot
data = {'Tahun': ['2017', '2018', '2019', '2020', '2021', '2022'],
        'Jumlah': [800, 450, 400, 425, 350, 331]}
df = pd.DataFrame(data)

df['Jumlah'].plot(kind='box')
plt.title('Penerimaan Siswa Baru')
plt.ylabel('Jumlah')
plt.show()
