# Membuat Simple Plotting

import matplotlib.pyplot as grafik
import numpy as np

# sample data
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

fig, ax = grafik.subplots()  # membuat figure dan sebuah axes
ax.plot(x, y)  # plotting data pada axes
grafik.show()  # menampilkan grafik

# Alternatif lain
grafik.plot()
grafik.show()

# Langkah Membuat Figure
fig = grafik.figure()
grafik.show()

# membuat figure dan sebuah axes
fig, ax = grafik.subplots()
grafik.show()

# membuat figure dan 2x1 axes, artinya dalam 1 figure terdapat 6 axes
fig, ax = grafik.subplots(2, 3)
grafik.show()
