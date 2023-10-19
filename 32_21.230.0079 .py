#  Latihan
# Memasukkan data ke dictionary, melaui inputan dari user.
# Langkah
# 1. Buat template dictionary
# 2. Buat dictionary kosong
# 3. Buat dictonary baru menggunakan keys dari di template yang sudah dibuat

import datetime  # untuk format tanggal
import os  # untuk membersihkan layar
# import string
# import random

TemplateSiswa = {  # membuat template
    'nisn': 'nisn',
    'nama': 'nama',
    'nilai_akhir': 0,
    'tgl_lhr': datetime.datetime(1111, 1, 11)
}

data_siswa = {}  # membuat dictionary kosong untuk dictionary bersarang
os.system('cls')  # membersihkan layar cmd

print(f'{"SELAMAT DATANG":^20}')
print(f'{"DATA SISWA":^20}\n')

cek = True
key = 0
while (cek):

    # membuat dictionary baru dari template berdasarkan keys
    siswa = dict.fromkeys(TemplateSiswa.keys())

    key += 1
    # key = input('Nomor Urut : ')
    print('Nomor Urut :', key)

    nisnSiswa = input(f'NISN Siswa : ')
    namaSiswa = input('Nama Siswa : ')
    nilaiAkhir = int(input('Nilai Akhir : '))
    tgl = int(input('Tanggal Lahir (dd) : '))
    bln = int(input('Bulan Lahir (mm) : '))
    thn = int(input('Tahun Lahir (YYYY) : '))

    print()
    edit = input('Edit data ketik [y/Y], jika tidak enter saja : ')
    if (edit == 'y' or edit == 'Y'):

        nisnSiswa = input(
            f'NISN Siswa sebelumnya {nisnSiswa} \nNISN siswa baru : ')
        namaSiswa = input(
            f'Nama Siswa sebelumnya {namaSiswa} \nNama siswa baru : ')
        nilaiAkhir = int(
            input(f'Nilai Akhir sebelumnya {nilaiAkhir} \nNilai Akhir baru : '))
        tgl = int(
            input(f'Tanggal Lahir (dd) sebelumnya {tgl} \nTanggal Lahir baru : '))
        bln = int(
            input(f'Bulan Lahir (mm) sebelumnya {bln} \nBulan Lahir baru : '))
        thn = int(
            input(f'Tahun Lahir (YYYY) sebelumnya {thn} \nTahun Lahir baru : '))

        print('data berhasil diedit')
        print()
    else:
        print('data tidak jadi di update')
        print()

    print()
    hapus = input('hapus data ketik [y/Y], jika tidak enter saja : ')
    if (hapus == 'y' or hapus == 'Y'):
        print('data sudah dihapus')
        print()
        key -= 1
    else:
        print('data tidak dihapus')
        print()
        siswa['nisn'] = nisnSiswa
        siswa['nama'] = namaSiswa
        siswa['nilai_akhir'] = nilaiAkhir
        siswa['tgl_lhr'] = datetime.datetime(
            thn, bln, tgl).strftime('%d/%m/%Y')

        # key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
        data_siswa.update({key: siswa})  # memasukkan data ke list data_siswa

# cek apakah mau input lagi atau tidak
    while (cek):
        jawab = input('ketik data lagi = ? (y/n)')
        if jawab == "n" or jawab == "N":
            cek = False
        elif jawab == "y" or jawab == "Y":
            cek = True
            break
        else:
            cek = True

    print()


print(f"{'No Urut':<13} {'NISN':<15} {'NAMA':<13} {'NILAI AKHIR':<13} {'TGL LAHIR'}")
print(17*'----')

for sis in data_siswa:
    KEY = sis
    nisn = data_siswa[KEY]['nisn']
    nama = data_siswa[KEY]['nama']
    nilai_akhir = data_siswa[KEY]['nilai_akhir']
    tgl_lhr = data_siswa[KEY]['tgl_lhr']
    print(f"{KEY:<13} {nisn:<15} {nama:<13} {nilai_akhir:<13} {tgl_lhr}")
print(17*'----')
print()
# print(data_siswa)
# print()
# print(17*'----')
# print()
