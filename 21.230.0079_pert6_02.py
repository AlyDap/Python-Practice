# Alur Hidup Plot atau Plot Lifecycle

from matplotlib.ticker import FuncFormatter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data = {'Item A': 109438,
        'Item B': 103569,
        'Item C': 104837,
        'Item D': 108648,
        'Item E': 198390,
        'Item F': 187308,
        'Item G': 189472,
        'Item H': 193740,
        'Item I': 190782,
        'Item J': 120958}
print(data)

items = tuple(data.keys())
print(items)
count = tuple(data.values())
print(count)

# Simple Plot
fig, ax = plt.subplots()
ax.barh(items, count)
plt.show()

# Pengaturan Style
print(plt.style.available)

fig, ax = plt.subplots()
plt.style.use('classic')
ax.barh(items, count)
plt.show()

# Pengaturan Tick Label
fig, ax = plt.subplots()
ax.barh(items, count)
labels = ax.get_xticklabels()
# set properties
plt.setp(labels,
         rotation=45,
         horizontalalignment='right')
plt.show()

# Pengaturan Format Ticker


def ribuan(x, pos):
    return f'{int(x/1000)}K'


fig, ax = plt.subplots()
ax.barh(items, count)
formatter = FuncFormatter(ribuan)
ax.xaxis.set_major_formatter(formatter)
ax.set(title='Contoh Plot',
       xlabel='jumlah',
       ylabel='Items')
plt.show()

# Pengaturan Label pada Sumbu (axix) dan Judul (title)
fig, ax = plt.subplots()
ax.barh(items, count)
ax.set(title='Contoh Plot',
       xlabel='Jumlah',
       ylabel='Items')
plt.show()

# Penambahan Garis (Vertikal, Horizontal) Pada Plot
fig, ax = plt.subplots()
ax.barh(items, count)
'''
ax.axvline(np.mean(count),
ls='--',
color='r')
'''
ax.axvline(80000,
           ls='--',
           color='r')
ax.set(title='Contoh Plot',
       xlabel='Jumlah',
       ylabel='Items')
plt.show()

# Menyimpan Hasil Plot Ke dalam File
print(fig.canvas.get_supported_filetypes())

fig, ax = plt.subplots()
ax.barh(items, count)
ax.axvline(np.mean(count),
           ls='--',
           color='r')
ax.set(title='Contoh Plot',
       xlabel='Jumlah',
       ylabel='Items')
fig.savefig('sales.png',
            transparent=False,
            dpi=80)
plt.show()
