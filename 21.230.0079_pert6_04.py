# Pengaturan Figure Layouts dengan GridSpec

# import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspex
import numpy as np

# Pengaturan Figure Layouts dengan subplots
siswa = ['HP', 'Attack', 'Mana', 'Difficult']
uts = [90, 80, 100, 75]
fig, axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
axes[0][0].bar(siswa, uts)
axes[0][1].pie(uts, labels=siswa)
axes[1][0].pie(uts, labels=siswa, explode=[0, 0, 0, 0.2])
axes[1][1].barh(siswa, uts)
plt.show()

# Pengaturan Figure Layouts dengan Gridspec
fig = plt.figure(constrained_layout=True)
gs = gridspex.GridSpec(ncols=2, nrows=2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax1.bar(siswa, uts)
ax2.pie(uts, labels=siswa)
ax3.pie(uts, labels=siswa, explode=[0, 0, 0, 0.2])
ax4.barh(siswa, uts)
plt.show()

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(ncols=2, nrows=2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax1.bar(siswa, uts)
ax2.pie(uts, labels=siswa)
ax3.pie(uts, labels=siswa, explode=[0, 0, 0, 0.2])
ax4.barh(siswa, uts)
plt.show()

# Rows Span dan Cols Span dengan GridSpec
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(ncols=2, nrows=2)
ax1 = fig.add_subplot(gs[0, :])  # menggunakan keseluruhan kolom
# ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax1.bar(siswa, uts)
# ax2.pie(uts, labels=siswa)
ax3.pie(uts, labels=siswa, explode=[0, 0, 0, 0.2])
ax4.barh(siswa, uts)
plt.show()


fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(ncols=3, nrows=3)

ax1 = fig.add_subplot(gs[0, :])
ax1.set_title('gs[0,:]')

ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title('gs[1,:-1]')
ax2.barh(siswa, uts)

ax3 = fig.add_subplot(gs[1:, -1])
ax3.set_title('gs[1:,-1]')
ax3.bar(siswa, uts)

ax4 = fig.add_subplot(gs[-1, 0])
ax4.set_title('gs[-1,0]')

ax5 = fig.add_subplot(gs[-1, -2])
ax5.set_title('gs[-1,-2]')
plt.show()
