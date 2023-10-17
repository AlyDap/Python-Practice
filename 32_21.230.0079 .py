#  Latihan
# Memasukkan data ke dictionary, melaui inputan dari user.
# Langkah
# 1. Buat template dictionary
# 2. Buat dictionary kosong
# 3. Buat dictonary baru menggunakan keys dari di template yang sudah dibuat

import datetime # untuk format tanggal
import os # untuk membersihkan layar
#import string
#import random

TemplateSiswa = { # membuat template
 'nisn':'nisn',
 'nama':'nama',
 'nilai_akhir':0,
 'tgl_lhr':datetime.datetime(1111,1,11)
}

data_siswa = {} # membuat dictionary kosong untuk dictionary bersarang
os.system('cls') # membersihkan layar cmd

while True:

 print(f'{"SELAMAT DATANG":^20}')
 print(f'{"DATA SISWA":^20}\n')

 siswa = dict.fromkeys(TemplateSiswa.keys()) # membuat dictionary baru dari template berdasarkan keys

 key = input('Nomor Urut : ')
 nisnSiswa = input('NISN Siswa : ')
 namaSiswa = input('Nama Siswa : ')
 nilaiAkhir = int(input('Nilai Akhir : '))
 tgl = int(input('Tanggal Lahir (dd) : '))
 bln = int(input('Bulan Lahir (m) : '))
 thn = int(input('Tahun Lahir (YYYY) : '))

 siswa['nisn'] = nisnSiswa
 siswa['nama'] = namaSiswa
 siswa['nilai_akhir'] = nilaiAkhir
 siswa['tgl_lhr'] = datetime.datetime(thn,bln,tgl)

 #key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
 data_siswa.update({key:siswa}) #memasukkan data ke list data_siswa

 jawab=input('ketik data lagi = ? (y/n)')
 if jawab=="n":
  break
 if jawab!="y":
  break

print(data_siswa)