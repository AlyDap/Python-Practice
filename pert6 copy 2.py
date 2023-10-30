# pip intsall matplotlib
# pip install numpy
# untuk visualisasi data

import matplotlib.pyplot as grafik
# import numpy as np

x=['A1','A2','A3','B','C','D','E','F','G','H','I','J','K','L','M','N1','N2','N3']
y=[5,5,5,5,2,7,2,7,-3,10,2,7,2,7,5,5,5,5]
d=[-2,-2,-2,-4,-2,-4,-2,-4,-2,-4,-2,-4,-2,-4,-2,-4,-4,-4]
z=[-1,-1,-1,-3,-1,-3,-1,-3,-1,-3,-1,-3,-1,-3,-1,-3,-3,-3]
# fig, ax =grafik.subplots()
grafik.plot(x, y, d, label='Nilai IP')
grafik.plot(x, z, label='Skor')
grafik.bar(x, d, label='IP Bar') #grafik bar
grafik.legend() #menampilkan label
grafik.title('Nyacak')
grafik.show()

# print('1')