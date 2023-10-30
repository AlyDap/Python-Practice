# Visualisasi Data Pada Pandas Data frame Lanjutan

# import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspex
import pandas as pd
import os
os.chdir("D:\\KULIAH S1 SI STMIK WP\SEMESTER 5\\1.1 Visualisasi Data dan Data Sciences\\Praktek\\Tugas")

# Membaca file csv
# df = pd.read_csv('./business.csv')
df = pd.read_csv('Country-data.csv')
print(df.head())
print()

# Bar Plot
# Ganti nama kolom
df.rename(columns={
    'country': 'Negara', 'child_mort': 'Anak Mati', 'life_expec': 'Harapan Hidup', 'total_fer': 'Tingkat Subur', 'gdpp': 'Gross Domestic Product Per Capita'}, inplace=True)
print(df.columns)
print(df)

# Ambil 5 cord awal
df[:5].plot(x='Negara',
            y=['Anak Mati', 'Harapan Hidup', 'exports', 'imports',  'inflation'],
            kind='bar')
plt.title('Bar Plot')
plt.ylabel('Nilai')
# plt.show()

# Line Plot
df[:5].plot(x='Negara',
            y=['Anak Mati', 'Harapan Hidup', 'exports', 'imports',  'inflation'],
            kind='line')
plt.title('Line Plot')
plt.ylabel('Nilai')
# plt.show()

# Box Plot
df[:5].plot(x='Negara',
            y=['Anak Mati', 'Harapan Hidup', 'exports', 'imports',  'inflation'],
            kind='box')
plt.title('Box Plot')
plt.ylabel('Nilai')
# plt.show()

# Scatter Plot
df.plot(x='Anak Mati', y='Harapan Hidup', kind='scatter')
plt.xlim(0, 200)
plt.ylim(0, 100)
plt.title('Scatter Plot')
# plt.show()

# Histogram
# bins mengindikasikan jumlah kelompok
df.plot(x='Negara', y='income', kind='hist', bins=50)
plt.title('Histogram Plot')
plt.xlabel('Nilai')
# plt.show()

# Subplots
df.plot(x='Negara',
        y=['exports', 'imports', 'health', 'inflation'],
        kind='hist',
        subplots=True,
        layout=(2, 2))
plt.title('SubPlotS')
plt.tight_layout()
plt.show()
