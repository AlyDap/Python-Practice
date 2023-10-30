# Kustomisasi Matplotlib dengan Style Sheets

# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)
plt.style.use('ggplot')

x = np.linspace(1, 10, 15)
plt.plot(x, x, 'bs-', label='lin')
plt.plot(x, np.log(x), 'ro', label='log')
plt.legend()
plt.xlabel('Sumbu Y')
plt.ylabel('Sumbu X')
plt.title('Contoh Plot')
plt.show()

# Membuat Style Sendiri
# axes.titlesize : 24
# axes.labelsize : 20
# lines.linewidht : 3
# lines.markersize : 10
# xtick.labelsize : 16
# ytick.labelsize : 16
custom_style = {
    'axes.titlesize': 24,
    'axes.labelsize': 20,
    'lines.linewidth': 3,
    'lines.markersize': 10,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16
}
# plt.style.use('default')  # Hapus semua pengaturan gaya sebelumnya
plt.style.use(custom_style)
x = np.linspace(1, 10, 15)
plt.plot(x, x, 'bs-', label='lin')
plt.plot(x, np.log(x), 'ro', label='log')
plt.legend()
plt.xlabel('Sumbu Y')
plt.ylabel('Sumbu X')
plt.title('Contoh Plot')
plt.show()

# Menerapkan Multiple Style
plt.style.use(['tableau-colorblind10', 'dark_background'])
x = np.linspace(1, 10, 15)
plt.plot(x, x, 'bs-', label='lin')
plt.plot(x, np.log(x), 'ro', label='log')
plt.legend()
plt.xlabel('Sumbu Y')
plt.ylabel('Sumbu X')
plt.title('Contoh Plot')
plt.show()

# Menerapkan Temporary Styling
plt.style.use('ggplot')
plt.plot(np.sin(np.linspace(0, 2*np.pi)), 'r-o')
plt.show()

with plt.style.context('dark_background'):
    plt.plot(np.sin(np.linspace(0, 2*np.pi)), 'r-o')
plt.show()

plt.plot(np.sin(np.linspace(0, 2*np.pi)), 'r-o')
plt.show()
