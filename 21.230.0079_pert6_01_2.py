# Object Oriented Style

import matplotlib.pyplot as grafik
import numpy as np

# Membuat figure beserta axes, dan memanggil method dari keduanya
# membuat deret bilangan dari O sampai dengan 2, dengan jumlah 100 data
x = np.linspace(0, 2, 100)
print(x)

fig, ax = grafik.subplots()
# plotting tiga variant data pada axes
ax.plot(x, x, label='liner')
ax.plot(x, x**2, label='kuadrat')
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('x label')  # membuat label x
ax.set_ylabel('y label')  # membuat label y
ax.set_title('Plot Sederhana')  # membuat Judul axes
ax.legend()  # menambahkan legenda
grafik.show()

# pyplot Style
# Membuat dan mengelola figure dan axes, serta menggunakan fungsi plot untuk menampilkan grafik
# plotting tiga variant data pada axes
grafik.plot(x, x, label='liner')
grafik.plot(x, x**2, label='kuadrat')
grafik.plot(x, x**3, label='cubic')
grafik.xlabel('x label')  # membuat label x
grafik.ylabel('y label')  # membuat label y
grafik.title('Plot Sederhana')  # membuat Judul axes
grafik.legend()  # menambahkan legenda
grafik.show()
