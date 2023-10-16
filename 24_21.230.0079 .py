# Operasi List #2
# Duplikasi List
data1 = ['ali', 'ali11','ali123']
data2 = data1.copy() # copy list
print(f'data 1 : {data1}')
print(f'data 2 : {data2}')
print()

# List Bersarang / Nested List
data_0 = [1,4,5,5]
data_1 = ['ali','ali11','ali123']
list_2d = [data_0,data_1]
print(f'{list_2d}')
print()

data_0 = [1,4,5,5]
data_1 = ['ali','ali11','ali123']
list_2d = [data_0,data_1,'joni',6]
print(f'{list_2d}')
print()

# list peserta memiliki variabel nama[0], umur[1], dan jns_kel[2]. ada 3 peserta berarti ada 3 list.
peserta_0 = ['rina', 28, 'wanita']
peserta_1 = ['joni', 18, 'laki-laki']
peserta_2 = ['slamet', 27,'laki-laki']
peserta_gab = [peserta_0, peserta_1, peserta_2]
print(peserta_gab,'\n')
# bagaimana mengakses data tersebut, maka gunakan perulangan
aa=0
for peserta in peserta_gab:
 aa+=1
 print(aa)
 print(f'nama\t:{peserta[0]}')
 print(f'umur\t:{peserta[1]}')
 print(f'jns_kel\t:{peserta[2]}\n')

# Ambil data dari list bersarang
peserta_0 = ['rina', 28, 'wanita']
peserta_1 = ['joni', 18, 'laki-laki']
peserta_2 = ['slamet', 27,'laki-laki']
peserta_gab = [peserta_0, peserta_1, peserta_2]
print(peserta_gab,'\n')
print(peserta_gab[0]) # akan menampilkan index ke 0 yaitu list data_0
print(peserta_gab[1]) # akan menampilkan index ke 1
print(peserta_gab[-1],'\n') # akan menampilkan index terakhir

x=0
for data in peserta_gab: # lakukan perulangan untuk menampilkan isi list_2d
 print(f'data list peserta[{x}] :{data}')
 x += 1
#cara menampilkan index tertentu
print(f'\n{peserta_gab[0][0]}') # akan menampilkan index ke 0 pada lis peserta_gab dan indeks ke 0 pada list peserta_0
print(f'\n{peserta_gab[-1][-1]}') # akan menampilkan index terakhir dengan data terakhir juga
print()

# Duplikat List Bersarang
from copy import deepcopy
peserta_0 = ['rina', 28, 'wanita']
peserta_1 = ['joni', 18, 'laki-laki']
peserta_2 = ['slamet', 27,'laki-laki']
peserta_gab = [peserta_0, peserta_1, peserta_2]
print(peserta_gab)
peserta_gab_copy = deepcopy(peserta_gab)
print(peserta_gab_copy)

print()
peserta_gab_copy = peserta_gab.copy() # shallow copy / salinan dangkal
print(peserta_gab_copy)

# Jika Anda hanya menggunakan copy, itu akan membuat salinan dangkal (shallow copy) di mana daftar dalam peserta_gab_copy masih akan merujuk pada daftar asli di dalamnya.

# Dengan menggunakan deepcopy, Anda akan menciptakan salinan yang sepenuhnya independen, sehingga perubahan pada peserta_gab_copy tidak akan memengaruhi peserta_gab dan sebaliknya.