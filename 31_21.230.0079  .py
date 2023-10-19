# Multy Keys dan Nesting Dictionary

import datetime as dt
siswa1 = {
    'nisn': '123',
    'nama': 'Ali',
    'nilai': 100,
    'ttl': dt.datetime(2003, 1, 1),
    'beasiswa': True
}
siswa2 = {
    'nisn': '222',
    'nama': 'Eko',
    'nilai': 50,
    'ttl': dt.datetime(2000, 10, 10),
    'beasiswa': False
}
siswa3 = {
    'nisn': '333',
    'nama': 'Asep',
    'nilai': 35,
    'ttl': dt.datetime(2012, 12, 12),
    'beasiswa': True
}

# membuat Dictionary bersarang
data_siswa = {
    '001': siswa1,
    '002': siswa2,
    '003': siswa3,
}

print(f'{"KEYS":<8} {"NISN":<8} {"NAMA":<8} {"SKOR":<8} {"TGL LAHIR":<8} {"BEASISWA":<8}')
print('=='*27)

for siswa in data_siswa:
    KEY = siswa
    NISN = data_siswa[KEY]['nisn']
    NAMA = data_siswa[KEY]['nama']
    SKOR = data_siswa[KEY]['nilai']
    LAHIR = data_siswa[KEY]['ttl'].strftime('%x')
    BEASISWA = data_siswa[KEY]['beasiswa']
    print(f'{KEY:<8} {NISN:<8} {NAMA:<8} {SKOR:<8} {LAHIR:<13} {BEASISWA:<8}')
