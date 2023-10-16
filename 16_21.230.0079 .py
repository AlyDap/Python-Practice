#Date Time

import datetime  as d #import library datetime

#Menampilkan tanggal sekarang
t=d.date.today()
print(f"Sekarang hari {t:%A}, tanggal {t}")
t=d.date(1945,8,17)
print(f"Indonesia Merdeka pada hari {t:%A}, tanggal {t}\n")

#Format Tanggal
from datetime import datetime
x = datetime.strptime("1945-08-17", "%Y-%m-%d")
# ubah format tanggal Indonesia
print(x)
print('format tanggal menjadi ' + x.strftime("%d/%m/%Y"))
print('format tanggal menjadi ' + x.strftime("%d %b %Y"))
print('format tanggal menjadi ' + x.strftime("%d %B %Y"))
print('format tanggal menjadi ' + x.strftime('%A, %d %B %Y'))
h = d.date.today()
x = datetime.strptime(str(h), "%Y-%m-%d")
# ubah format tanggal Indonesia
print('format tanggal menjadi ' + x.strftime("%d / %m / %Y"))
print('format tanggal menjadi ' + x.strftime("%d %b %Y"))
print('format tanggal menjadi ' + x.strftime("%d %B %Y"))
print('format tanggal menjadi ' + x.strftime("%A, %d %B %Y")+'\n')
print

import datetime as dt
print(f'Silahkan masukkan tanggal bulan dan tahun')
tanggal = int(input('tanggal\t:'))
bulan = int(input('bulan\t:'))
tahun = int(input('tahun\t:'))
cariTgl = dt.date(tahun,bulan,tanggal)
hari_ini = dt.date.today()
umurHari = hari_ini - cariTgl
umurTahun = umurHari.days // 365
sisaBulan = (umurHari.days % 365) // 30 
print(f'\nHari, Tanggal yang anda inputkan: {cariTgl:%A}, {cariTgl}\nUmur Anda \t\t\t:{umurTahun:} tahun, {sisaBulan} bulan')

a=umurHari.days // 365
print(a)
a=umurHari.days % 365
print(a)
a=(umurHari.days % 365) // 30 
print(a)
