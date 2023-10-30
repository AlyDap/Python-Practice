# Visualisasi Data Pada Pandas Data frame

# import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspex
import pandas as pd

# Sample Data Frame
df = pd.DataFrame({
    'nama': ['Andi', 'Bandi', 'Candi', 'Dandi', 'Endi', 'Fandi', 'Gandi'],
    'usia': [21, 30, 43, 54, 60, 65, 18],
    'gender': ['L', 'L', 'L', 'P', 'P', 'P', 'L'],
    'provinsi': ['Jabar', 'Jatim', 'Jateng', 'Jateng', 'Jabar', 'Jatim', 'Jateng'],
    'n_anak': [1, 6, 5, 4, 3, 2, 1],
    'n_pets': [0, 10, 1, 0, 4, 5, 1]})
print(df)

# Scatter
df.plot(kind='scatter', x='n_anak', y='n_pets', color='red')
plt.title('Scatter Plot')
plt.xlabel('Jumlah Anak')
plt.ylabel('Jumlah Pets')
plt.show()

# Histogram
df[['usia']].plot(kind='hist', bins=[0, 20, 40, 60, 80, 100])
plt.title('Histogram')
plt.xlabel('Usia')
plt.ylabel('Jumlah')
plt.show()

# Line Plot
df.plot(kind='line', x='nama', y='n_anak', color='g')
plt.title('Line Plot')
plt.ylabel('Jumlah')
plt.show()

df.plot(kind='line', x='nama', y='n_anak', color='g')
df.plot(kind='line', x='nama', y='n_pets', color='r')
plt.title('Line Plot')
plt.ylabel('Jumlah')
plt.show()

ax = plt.gca()
df.plot(kind='line', x='nama', y='n_anak', color='g', ax=ax)
df.plot(kind='line', x='nama', y='n_pets', color='r', ax=ax)
plt.title('Multiple Line Plot')
plt.ylabel('Jumlah')
plt.show()

# Bar Plot
df.plot(kind='bar', x='nama', y='usia')
plt.title('Bar Plot')
plt.ylabel('Jumlah')
plt.show()

df.groupby('provinsi')['nama'].count().plot(kind='bar')
plt.title('Bar Plot')
plt.ylabel('Jumlah')
plt.show()

# Stacked Bar PLot dengan 2 level group by
df.groupby(['provinsi', 'gender']).size(
).unstack().plot(kind='bar', stacked=True)
plt.title('Bar Plot')
plt.ylabel('Jumlah')
plt.show()

df.groupby(['gender', 'provinsi']).size(
).unstack().plot(kind='bar', stacked=True)
plt.title('Bar Plot')
plt.ylabel('Jumlah')
plt.show()
