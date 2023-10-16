# List itu array
# Bisa berisi number / string atau kombinasi keduanya
list_num =[1,2,3,4,5]
print(list_num)
print(f'Ini array {list_num}')

print()

list_string=['a','b','c']
print(list_string)
print(f'Ini array {list_string}')

print()

list_mix=['a',1,'c']
print(list_mix)
print(f'Ini array {list_mix}')

# Range itu adalah array
print()

data_range=range(0,5)
list_range=list(data_range)
print(list_range)

print()

data_range=range(0,10,2)
list_range=list(data_range)
print(list_range)

print()

list_for=[i for i in range(0,4)]
print(list_for)
list_for=[i+5 for i in range(0,4)]
print(list_for)
list_for=[i for i in range(1,5) if i !=2]
print(list_for)
list_for=[i for i in range(1,10) if i % 2 !=1]
print(list_for)

print()
data=['Ali',100,'230 kg',123,555]
print('Berat badan',data[0],f'kurang dari {data[2]}')
print(f'Array terakhir {data[-1]} /n array awal(0) + 1 {data[+1]}')
print('jumlah array Data ada',len(data),'data')

print()
print('Sebelum =',data)
# insert untuk menambah di depan 
data.insert(0,'oi')
print('Sesudah =',data)
# append untuk menambah di depan
tambah=data.append(999)
print('Sesudah =',data)

print()
# Menambah 2 data
data_baru=['NEW','BARU']
data.extend(data_baru)
print('Gabungan =',data)
# Merubah data terakhir
data[-1]='LAST'
print('Berubah =',data)

print()
# hapus data berdasarkan input
data.remove('LAST')
print('Hapus Last =',data)
# hapus data terakhir
data.pop()
print('Hapus Terakhir =',data)

print()
# Mencari jumlah data
d=['otong','surotong','otong',1,2,2,1,3,1]
jum_d= d.count('otong')
print('Jumlah otong ada',jum_d)
jum_d= d.count(1)
print('Jumlah angka 1 ada',jum_d)

# Mencari index data
cari_data=d.index('surotong')
print('surotong ada di index ke',cari_data)

print()
# mengurutkan
dd=[2,2,3,1,3,4,2,5,1,1,6,2,3]
dd.sort()
print(dd)

dd=[2,2,3,1,3,4,2,5,1,1,6,2,3]
dd.sort(reverse=True)
print(dd)

dd=['D','A','F','X','H','Z','C','K']
dd.sort()
print(dd)

# membalik
dd.reverse()
print(dd)