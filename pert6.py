# pip intsall matplotlib
# pip install numpy
# untuk visualisasi data

import matplotlib.pyplot as grafik
import numpy as np

x=np.linspace(0,2,100)
# deret dari 0 sampai 2 yang angkanya ada 100
# print(x)

# variable figure
fig, ax =grafik.subplots()
# ploting menempatkan
ax.plot(x, x, label='linier')
# linier garis lurus
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.legend()
grafik.show()